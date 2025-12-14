import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Email Generator")
    st.write("Generate personalized cold emails from job postings")

    url_input = st.text_input(
        "Enter Job Posting URL:",
        value="https://careers.nike.com/software-engineer/job/R-72423",
        placeholder="https://example.com/job/12345"
    )
    submit_button = st.button("Generate Email", type="primary")

    if submit_button:
        if not url_input:
            st.error("⚠️ Please enter a URL")
            return

        try:
            with st.spinner("🔍 Scraping job posting..."):
                loader = WebBaseLoader([url_input])
                page_data = loader.load().pop().page_content
                data = clean_text(page_data)

            with st.spinner("📊 Loading portfolio..."):
                portfolio.load_portfolio()

            with st.spinner("🔎 Extracting job details..."):
                jobs = llm.extract_jobs(data)

            if not jobs:
                st.warning("No jobs found in the provided URL")
                return

            st.success(f"✅ Found {len(jobs)} job(s)!")

            for idx, job in enumerate(jobs, 1):
                with st.expander(f"📋 Job {idx}: {job.get('role', 'Unknown Role')}"):
                    st.json(job)

                with st.spinner(f"✍️ Generating email for Job {idx}..."):
                    skills = job.get("skills", [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)

                st.markdown(f"### 📧 Generated Email {idx}")
                st.code(email, language="markdown")

        except Exception as e:
            st.error(f"❌ An Error Occurred: {str(e)}")
            st.exception(e)


if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator",
        page_icon="📧"
    )

    chain = Chain()
    portfolio_obj = Portfolio()
    create_streamlit_app(chain, portfolio_obj, clean_text)