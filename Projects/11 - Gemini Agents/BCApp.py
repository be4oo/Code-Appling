# File: business_consultant_app.py

import streamlit as st
import json
from ai_business_consultant import business_consultant

def main():
    st.title("AI Business Consultant")

    # User input for business idea
    idea = st.text_area("Describe your business idea:", height=150)

    if st.button("Analyze Idea"):
        if idea:
            with st.spinner("Analyzing your business idea..."):
                result = business_consultant(idea)

            if "error" in result:
                st.error(result["error"])
            else:
                # Display analysis
                st.subheader("Analysis")
                st.write(result["analysis"])

                # Display success probability
                st.subheader("Success Probability")
                st.progress(int(result["success_probability"].rstrip('%')))
                st.write(f"{result['success_probability']} chance of success")

                # Display team skills
                st.subheader("Required Team Skills")
                for skill in result["team_skills"]:
                    st.write(f"- {skill}")

                # Display MVP tips
                st.subheader("MVP Tips")
                for tip in result["mvp_tips"]:
                    st.write(f"- {tip}")

                # Display business model
                st.subheader("Suggested Business Model")
                st.write(result["business_model"])

                # Display SWOT analysis
                st.subheader("SWOT Analysis")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Strengths")
                    for strength in result["swot_analysis"]["strengths"]:
                        st.write(f"- {strength}")
                    st.write("Opportunities")
                    for opportunity in result["swot_analysis"]["opportunities"]:
                        st.write(f"- {opportunity}")
                with col2:
                    st.write("Weaknesses")
                    for weakness in result["swot_analysis"]["weaknesses"]:
                        st.write(f"- {weakness}")
                    st.write("Threats")
                    for threat in result["swot_analysis"]["threats"]:
                        st.write(f"- {threat}")

                # Option to download the analysis as JSON
                st.subheader("Download Analysis")
                json_str = json.dumps(result, indent=2)
                st.download_button(
                    label="Download JSON",
                    data=json_str,
                    file_name="business_analysis.json",
                    mime="application/json"
                )
        else:
            st.warning("Please enter a business idea to analyze.")

if __name__ == "__main__":
    main()