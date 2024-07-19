# File: business_consultant_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import traceback
import json
from BAgents import startup_advisor_hub

def main():
    st.title("AI Startup Advisor")

    # Sidebar for selecting advisor function
    advisor_function = st.sidebar.selectbox(
        "Choose Advisor Function",
        ["business_consultant", "market_research", "competitive_analysis"]
    )

    # Main content area
    if advisor_function == "business_consultant":
        business_consultant_view()
    elif advisor_function == "market_research":
        market_research_view()
    elif advisor_function == "competitive_analysis":
        competitive_analysis_view()

def business_consultant_view():
    st.subheader("AI Business Consultant")
    idea = st.text_area("Describe your business idea:", height=150)

    if st.button("Analyze Idea"):
        if idea:
            with st.spinner("Analyzing your business idea..."):
                result = startup_advisor_hub("business_consultant", idea_description=idea)
            display_business_consultant_result(result)
        else:
            st.warning("Please enter a business idea to analyze.")

def market_research_view():
    st.subheader("Market Research")
    industry = st.text_input("Industry:")
    target_market = st.text_input("Target Market:")

    if st.button("Conduct Market Research"):
        if industry and target_market:
            with st.spinner("Conducting market research..."):
                result = startup_advisor_hub("market_research", industry=industry, target_market=target_market)
            display_market_research_result(result)
        else:
            st.warning("Please enter both industry and target market.")

def competitive_analysis_view():
    st.subheader("Competitive Analysis")
    business_idea = st.text_area("Describe your business idea:", height=100)
    competitors = st.text_input("Enter competitors (comma-separated):")

    if st.button("Analyze Competitors"):
        if business_idea and competitors:
            competitor_list = [comp.strip() for comp in competitors.split(',')]
            with st.spinner("Analyzing competitors..."):
                result = startup_advisor_hub("competitive_analysis", business_idea=business_idea, competitors=competitor_list)
            display_competitive_analysis_result(result)
        else:
            st.warning("Please enter both business idea and competitors.")

def display_business_consultant_result(result):
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("Analysis")
        st.write(result["analysis"])

        st.subheader("Success Probability")
        st.progress(int(result["success_probability"].rstrip('%')))
        st.write(f"{result['success_probability']} chance of success")

        st.subheader("Required Team Skills")
        for skill in result["team_skills"]:
            st.write(f"- {skill}")

        st.subheader("MVP Tips")
        for tip in result["mvp_tips"]:
            st.write(f"- {tip}")

        st.subheader("Suggested Business Model")
        st.write(result["business_model"])

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

        st.subheader("Download Analysis")
        json_str = json.dumps(result, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="business_analysis.json",
            mime="application/json"
        )

def display_market_research_result(result):
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("Industry Overview")
        st.write(result["industry_overview"])

        st.subheader("Market Size and Growth Potential")
        st.write(result["market_size_and_growth"])

        st.subheader("Key Players and Competitors")
        for player in result["key_players"]:
            st.write(f"- {player}")

        st.subheader("Target Market Demographics")
        st.write(result["target_market_demographics"])

        st.subheader("Consumer Trends")
        for trend in result["consumer_trends"]:
            st.write(f"- {trend}")

        st.subheader("Regulatory Environment")
        st.write(result["regulatory_environment"])

        st.subheader("Potential Challenges")
        for challenge in result["potential_challenges"]:
            st.write(f"- {challenge}")

        st.subheader("Opportunities for Innovation")
        for opportunity in result["innovation_opportunities"]:
            st.write(f"- {opportunity}")

        st.subheader("Download Market Research")
        json_str = json.dumps(result, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="market_research.json",
            mime="application/json"
        )

def display_competitive_analysis_result(result):
    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("Competitive Landscape Overview")
        st.write(result["competitive_landscape_overview"])

        st.subheader("Competitor Analysis")
        for competitor, analysis in result["competitor_analysis"].items():
            st.write(f"**{competitor}**")
            st.write(f"Company Profile: {analysis['company_profile']}")
            st.write(f"Products/Services: {analysis['products_services']}")
            st.write(f"Target Market: {analysis['target_market']}")
            st.write(f"Pricing Strategy: {analysis['pricing_strategy']}")
            st.write(f"Marketing Approach: {analysis['marketing_approach']}")
            st.write("Strengths:")
            for strength in analysis['strengths']:
                st.write(f"- {strength}")
            st.write("Weaknesses:")
            for weakness in analysis['weaknesses']:
                st.write(f"- {weakness}")
            st.write("---")

        st.subheader("Comparison Matrix")
        st.table(result["comparison_matrix"])

        st.subheader("Market Positioning Map")
        st.image(result["market_positioning_map"])

        st.subheader("Opportunities for Differentiation")
        for opportunity in result["differentiation_opportunities"]:
            st.write(f"- {opportunity}")

        st.subheader("Potential Threats from Competitors")
        for threat in result["competitor_threats"]:
            st.write(f"- {threat}")

        st.subheader("Recommendations for Competitive Advantage")
        for recommendation in result["competitive_advantage_recommendations"]:
            st.write(f"- {recommendation}")

        st.subheader("Download Competitive Analysis")
        json_str = json.dumps(result, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="competitive_analysis.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()