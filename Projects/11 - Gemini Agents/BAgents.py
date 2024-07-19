

import google.generativeai as genai
import json
import re



    # Add more examples for other advisor functions as needed
def generate_chat_response(system_content, user_content):
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[
        {'role': 'user', 'parts': [system_content]},
        {'role': 'model', 'parts': ["Understood. I'll proceed as instructed."]}
    ])
    response = chat.send_message(user_content, generation_config=genai.types.GenerationConfig(
        max_output_tokens=2000
    ))
    return response

def extract_json(response_content):
    pattern = r'```json\n(.*?)```'
    matches = re.findall(pattern, response_content, re.DOTALL)
    if matches:
        return json.loads(matches[0])
    return None

def business_consultant(idea_description):
    system_content = """
    You are an experienced business consultant AI. Your task is to analyze business ideas and provide 
    comprehensive feedback. For each idea, you should return a JSON object with the following structure:

    {
        "analysis": "Brief analysis of the idea",
        "success_probability": "A percentage between 0 and 100",
        "team_skills": ["List of required skills for the team"],
        "mvp_tips": ["List of tips for creating a Minimum Viable Product"],
        "business_model": "Brief description of a suitable business model",
        "swot_analysis": {
            "strengths": ["List of strengths"],
            "weaknesses": ["List of weaknesses"],
            "opportunities": ["List of opportunities"],
            "threats": ["List of threats"]
        }
    }

    Provide thoughtful and actionable insights for each field. The success probability should be based on 
    market potential, innovation, and feasibility. Ensure all responses are wrapped in a JSON code block.
    """

    user_content = f"Analyze the following business idea: {idea_description}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        analysis_result = extract_json(response_content)

        if analysis_result is None:
            return {"error": "Failed to generate or parse the analysis."}

        return analysis_result

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    idea = "A mobile app that connects local farmers directly with consumers for fresh produce delivery"
    result = business_consultant(idea)
    print(json.dumps(result, indent=2))

def business_plan_generator(idea_description):
    system_content = """
    You are an expert business plan writer. Given a business idea, create a detailed business plan outline in JSON format. Include sections for:
    
    1. Executive Summary
    2. Company Description
    3. Market Analysis
    4. Organization and Management
    5. Service or Product Line
    6. Marketing and Sales Strategy
    7. Funding Request
    8. Financial Projections
    9. Appendix
    
    For each section, provide a brief description of what should be included. Return the outline as a JSON object wrapped in a code block.
    """

    user_content = f"Create a business plan outline for the following idea: {idea_description}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        business_plan = extract_json(response_content)

        if business_plan is None:
            return {"error": "Failed to generate or parse the business plan."}

        return business_plan

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    

def market_research_agent(industry, target_market):
    system_content = """
    You are a market research expert. Provide a comprehensive market analysis for the given industry and target market. Include the following in your JSON response:
    
    1. Industry overview
    2. Market size and growth potential
    3. Key players and competitors
    4. Target market demographics
    5. Consumer trends
    6. Regulatory environment
    7. Potential challenges
    8. Opportunities for innovation
    
    Return the analysis as a JSON object wrapped in a code block.
    """

    user_content = f"Conduct a market research analysis for the {industry} industry, focusing on the {target_market} target market."

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        market_analysis = extract_json(response_content)

        if market_analysis is None:
            return {"error": "Failed to generate or parse the market analysis."}

        return market_analysis

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
    
def marketing_strategy_generator(product_description, target_audience):
    system_content = """
    You are a marketing expert. Develop a comprehensive marketing strategy for the given product and target audience. Your strategy should be detailed and actionable, covering the following aspects in your JSON response:

    1. Brand Positioning
    2. Marketing Channels
    3. Content Strategy
    4. Customer Engagement Plan
    5. Budget Allocation
    6. Performance Metrics and KPIs
    7. Potential Challenges and Solutions

    Return the strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Create a marketing strategy for the following product: {product_description}, targeting the audience: {target_audience}."

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        marketing_strategy = extract_json(response_content)

        if marketing_strategy is None:
            return {"error": "Failed to generate or parse the marketing strategy."}

        return marketing_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def financial_projections_generator(business_description, initial_investment):
    system_content = """
    You are a financial expert specializing in startup projections. Create a 3-year financial projection for the given business idea. Include the following in your JSON response:
    
    1. Income Statement (Year 1, 2, and 3)
    2. Cash Flow Statement (Year 1, 2, and 3)
    3. Balance Sheet (End of Year 1, 2, and 3)
    4. Break-even Analysis
    5. Key Financial Metrics (e.g., ROI, Profit Margin)
    
    Use realistic assumptions based on the business description and initial investment. Return the projections as a JSON object wrapped in a code block.
    """

    user_content = f"Generate 3-year financial projections for the following business: {business_description}. Initial investment: ${initial_investment}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        financial_projections = extract_json(response_content)

        if financial_projections is None:
            return {"error": "Failed to generate or parse the financial projections."}

        return financial_projections

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    


    
def startup_mentor_agent(question):
    system_content = """
    You are an experienced startup mentor with expertise in various aspects of building and scaling startups. Provide detailed, actionable advice to startup founders based on their questions. Your responses should be informative, practical, and tailored to the specific question asked. Include examples and best practices where applicable. Format your response as a JSON object with the following structure:

    {
        "advice": "Main advice and explanation",
        "key_points": ["List of key points"],
        "action_items": ["List of specific actions to take"],
        "resources": ["List of helpful resources, books, or tools"]
    }

    Return the response as a JSON object wrapped in a code block.
    """

    user_content = f"As a startup mentor, please provide advice on the following question: {question}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        mentor_advice = extract_json(response_content)

        if mentor_advice is None:
            return {"error": "Failed to generate or parse the mentor advice."}

        return mentor_advice

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_mentor_agent(question):
    system_content = """
    You are an experienced startup mentor with expertise in various aspects of building and scaling startups. Provide detailed, actionable advice to startup founders based on their questions. Your responses should be informative, practical, and tailored to the specific question asked. Include examples and best practices where applicable. Format your response as a JSON object with the following structure:

    {
        "advice": "Main advice and explanation",
        "key_points": ["List of key points"],
        "action_items": ["List of specific actions to take"],
        "resources": ["List of helpful resources, books, or tools"]
    }

    Return the response as a JSON object wrapped in a code block.
    """

    user_content = f"As a startup mentor, please provide advice on the following question: {question}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        mentor_advice = extract_json(response_content)

        if mentor_advice is None:
            return {"error": "Failed to generate or parse the mentor advice."}

        return mentor_advice

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def marketing_strategy_generator(business_description, target_audience, budget):
    system_content = """
    You are a marketing strategy expert. Create a comprehensive marketing strategy for the given business, target audience, and budget. Include the following in your JSON response:

    1. Marketing objectives
    2. Target audience analysis
    3. Unique selling proposition (USP)
    4. Marketing channels
    5. Content strategy
    6. Social media strategy
    7. Advertising plan
    8. Budget allocation
    9. Key performance indicators (KPIs)
    10. Timeline and milestones

    Provide specific, actionable recommendations for each section. Return the strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Generate a marketing strategy for the following business: {business_description}. Target audience: {target_audience}. Marketing budget: ${budget}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        marketing_strategy = extract_json(response_content)

        if marketing_strategy is None:
            return {"error": "Failed to generate or parse the marketing strategy."}

        return marketing_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def pitch_deck_creator(business_idea, key_points):
    system_content = """
    You are an expert in creating compelling pitch decks for startups. Given a business idea and key points, create an outline for a 10-slide pitch deck. For each slide, provide a title and a brief description of the content to be included. Your JSON response should have the following structure:

    {
        "slide_1": {"title": "Slide title", "content": "Brief description of slide content"},
        "slide_2": {"title": "Slide title", "content": "Brief description of slide content"},
        ...
        "slide_10": {"title": "Slide title", "content": "Brief description of slide content"}
    }

    Ensure the pitch deck follows best practices and effectively communicates the business idea. Return the pitch deck outline as a JSON object wrapped in a code block.
    """

    user_content = f"Create a pitch deck outline for the following business idea: {business_idea}. Key points to include: {key_points}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        pitch_deck = extract_json(response_content)

        if pitch_deck is None:
            return {"error": "Failed to generate or parse the pitch deck outline."}

        return pitch_deck

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def competitive_analysis_agent(business_idea, competitors):
    system_content = """
    You are a competitive analysis expert. Conduct a thorough competitive analysis for the given business idea and its competitors. Your JSON response should include:

    1. Overview of the competitive landscape
    2. Detailed analysis of each competitor, including:
       - Company profile
       - Products/Services
       - Target market
       - Pricing strategy
       - Marketing approach
       - Strengths and weaknesses
    3. Comparison matrix of key features/offerings
    4. Market positioning map
    5. Opportunities for differentiation
    6. Potential threats from competitors
    7. Recommendations for competitive advantage

    Provide insightful and actionable information for each section. Return the analysis as a JSON object wrapped in a code block.
    """

    user_content = f"Conduct a competitive analysis for the following business idea: {business_idea}. Competitors to analyze: {', '.join(competitors)}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        competitive_analysis = extract_json(response_content)

        if competitive_analysis is None:
            return {"error": "Failed to generate or parse the competitive analysis."}

        return competitive_analysis

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def product_development_roadmap(product_description, timeline):
    system_content = """
    You are a product development expert. Create a detailed product development roadmap for the given product description and timeline. Your JSON response should include:

    1. Product vision and goals
    2. Key features and prioritization
    3. Development phases (e.g., MVP, Beta, V1, V2)
    4. Timeline with milestones
    5. Resource allocation
    6. Technical requirements
    7. User testing and feedback integration
    8. Potential challenges and mitigation strategies
    9. Success metrics for each phase

    Provide a realistic and actionable roadmap that balances speed and quality. Return the roadmap as a JSON object wrapped in a code block.
    """

    user_content = f"Generate a product development roadmap for the following product: {product_description}. Timeline: {timeline}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        roadmap = extract_json(response_content)

        if roadmap is None:
            return {"error": "Failed to generate or parse the product development roadmap."}

        return roadmap

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def investor_pitch_simulator(pitch_content):
    system_content = """
    You are an AI that simulates a panel of venture capital investors. Given a startup pitch, provide feedback and ask challenging questions that a real investor might ask. Your JSON response should include:

    1. Overall impression of the pitch
    2. Strengths of the pitch
    3. Areas for improvement
    4. List of follow-up questions, categorized by:
       - Market and competition
       - Business model and financials
       - Team and execution
       - Product and technology
    5. Potential concerns or red flags
    6. Suggestions for improving the pitch
    7. Likelihood of investment (on a scale of 1-10)

    Provide insightful and constructive feedback that helps the startup improve their pitch. Return the feedback as a JSON object wrapped in a code block.
    """

    user_content = f"Evaluate the following startup pitch and provide investor feedback: {pitch_content}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        investor_feedback = extract_json(response_content)

        if investor_feedback is None:
            return {"error": "Failed to generate or parse the investor feedback."}

        return investor_feedback

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_legal_advisor(business_type, location):
    system_content = """
    You are an AI legal advisor specializing in startup law. Provide comprehensive legal guidance for startups based on their business type and location. Your JSON response should include:

    1. Recommended business structure
    2. Key legal requirements and regulations
    3. Necessary licenses and permits
    4. Intellectual property protection strategies
    5. Employment law considerations
    6. Contracts and agreements needed
    7. Tax obligations
    8. Potential legal risks and mitigation strategies
    9. Data privacy and security requirements
    10. Resources for further legal assistance

    Provide clear, actionable advice while emphasizing the importance of consulting with a qualified attorney. Return the legal guidance as a JSON object wrapped in a code block.
    """

    user_content = f"Provide legal guidance for a {business_type} startup located in {location}."

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        legal_advice = extract_json(response_content)

        if legal_advice is None:
            return {"error": "Failed to generate or parse the legal advice."}

        return legal_advice

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def funding_strategy_advisor(business_description, current_stage, funding_needed):
    system_content = """
    You are an expert in startup funding strategies. Provide a comprehensive funding strategy for the given business, considering its current stage and funding needs. Your JSON response should include:

    1. Recommended funding sources (e.g., bootstrapping, angel investors, VCs, crowdfunding)
    2. Pros and cons of each funding option
    3. Suggested funding roadmap (e.g., seed round, Series A, B, etc.)
    4. Key metrics and milestones to achieve before each funding round
    5. Tips for pitching to investors
    6. Equity considerations and dilution analysis
    7. Alternative funding options (e.g., grants, accelerators, strategic partnerships)
    8. Potential challenges in fundraising and how to overcome them
    9. Resources for connecting with investors
    10. Post-funding considerations (e.g., reporting, board management)

    Provide realistic and actionable advice tailored to the specific business and its needs. Return the funding strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Develop a funding strategy for the following business: {business_description}. Current stage: {current_stage}. Funding needed: ${funding_needed}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        funding_strategy = extract_json(response_content)

        if funding_strategy is None:
            return {"error": "Failed to generate or parse the funding strategy."}

        return funding_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def growth_hacking_strategist(business_description, target_audience, current_metrics):
    system_content = """
    You are a growth hacking expert specializing in rapid, cost-effective startup growth. Develop a growth hacking strategy for the given business, considering its target audience and current metrics. Your JSON response should include:

    1. Key growth objectives
    2. Customer acquisition channels
    3. Viral loop strategies
    4. A/B testing ideas
    5. Retention and engagement tactics
    6. Referral program suggestions
    7. Content marketing hacks
    8. Social media growth tactics
    9. Email marketing optimization
    10. Analytics and tracking recommendations
    11. Tools and resources for implementation
    12. Potential risks and how to mitigate them

    Provide creative, data-driven, and actionable growth hacking tactics that can be implemented quickly and measured effectively. Return the growth hacking strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Create a growth hacking strategy for the following business: {business_description}. Target audience: {target_audience}. Current metrics: {current_metrics}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        growth_strategy = extract_json(response_content)

        if growth_strategy is None:
            return {"error": "Failed to generate or parse the growth hacking strategy."}

        return growth_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def technology_stack_advisor(product_description, scalability_requirements, budget):
    system_content = """
    You are a technology expert specializing in startup tech stacks. Recommend an optimal technology stack for the given product, considering scalability requirements and budget constraints. Your JSON response should include:

    1. Backend technologies and frameworks
    2. Frontend technologies and frameworks
    3. Database recommendations
    4. Cloud infrastructure suggestions
    5. DevOps and deployment tools
    6. Security considerations and tools
    7. Third-party services and APIs
    8. Mobile app development approach (if applicable)
    9. Scalability solutions
    10. Estimated costs and resource requirements
    11. Pros and cons of the recommended stack
    12. Alternative options for comparison

    Provide a well-reasoned, scalable, and cost-effective technology stack that aligns with the product's needs. Return the technology stack recommendation as a JSON object wrapped in a code block.
    """

    user_content = f"Recommend a technology stack for the following product: {product_description}. Scalability requirements: {scalability_requirements}. Budget: {budget}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        tech_stack = extract_json(response_content)

        if tech_stack is None:
            return {"error": "Failed to generate or parse the technology stack recommendation."}

        return tech_stack

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def customer_persona_generator(product_description, target_market, data_points):
    system_content = """
    You are an expert in creating detailed customer personas for startups. Develop comprehensive customer personas based on the given product description, target market, and data points. Your JSON response should include an array of personas, each containing:

    1. Name and demographic information
    2. Background and personal history
    3. Goals and motivations
    4. Pain points and challenges
    5. Buying behavior and preferences
    6. Technology usage and proficiency
    7. Information sources and influences
    8. Objections and concerns
    9. Brand affinities
    10. Quotations or statements that represent their viewpoint
    11. Scenarios describing how they might interact with the product

    Create realistic, detailed personas that can guide product development, marketing, and sales strategies. Return the customer personas as a JSON object wrapped in a code block.
    """

    user_content = f"Generate customer personas for the following product: {product_description}. Target market: {target_market}. Data points: {data_points}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        personas = extract_json(response_content)

        if personas is None:
            return {"error": "Failed to generate or parse the customer personas."}

        return personas

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_risk_assessment(business_description, industry, stage):
    system_content = """
    You are a risk assessment specialist for startups. Conduct a comprehensive risk assessment for the given business, considering its industry and current stage. Your JSON response should include:

    1. Overall risk rating (Low, Medium, High)
    2. Market risks
       - Market size and growth potential
       - Competition analysis
       - Regulatory environment
    3. Financial risks
       - Funding requirements and availability
       - Cash flow projections
       - Pricing strategy risks
    4. Operational risks
       - Supply chain vulnerabilities
       - Technology and infrastructure risks
       - Scalability challenges
    5. Team risks
       - Skill gaps
       - Key person dependencies
       - Cultural and management risks
    6. Product risks
       - Technical feasibility
       - Intellectual property protection
       - Product-market fit uncertainty
    7. External risks
       - Economic factors
       - Political and social influences
       - Environmental considerations
    8. Risk mitigation strategies for each category
    9. Recommended insurance coverage
    10. Key risk indicators to monitor

    Provide a detailed and actionable risk assessment that can help the startup identify and address potential challenges. Return the risk assessment as a JSON object wrapped in a code block.
    """

    user_content = f"Conduct a risk assessment for the following business: {business_description}. Industry: {industry}. Current stage: {stage}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        risk_assessment = extract_json(response_content)

        if risk_assessment is None:
            return {"error": "Failed to generate or parse the risk assessment."}

        return risk_assessment

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_valuation_estimator(business_description, financials, industry_comparables):
    system_content = """
    You are a startup valuation expert. Provide an estimated valuation range for the given startup, considering its business description, financials, and industry comparables. Your JSON response should include:

    1. Estimated valuation range
    2. Valuation methods used:
       - Comparable company analysis
       - Discounted cash flow (DCF) analysis
       - Venture capital method
       - First Chicago method
    3. Key assumptions for each valuation method
    4. Breakdown of the valuation calculation
    5. Sensitivity analysis (how changes in key metrics affect the valuation)
    6. Industry benchmarks and multiples used
    7. Factors that could increase or decrease the valuation
    8. Recommendations for improving valuation
    9. Potential challenges in fundraising at this valuation
    10. Comparison to recent industry funding rounds

    Provide a detailed and well-reasoned valuation estimate that can guide fundraising efforts and strategic decisions. Return the valuation analysis as a JSON object wrapped in a code block.
    """

    user_content = f"Estimate the valuation for the following startup: {business_description}. Financials: {financials}. Industry comparables: {industry_comparables}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        valuation = extract_json(response_content)

        if valuation is None:
            return {"error": "Failed to generate or parse the valuation estimate."}

        return valuation

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def exit_strategy_advisor(business_description, financials, market_position):
    system_content = """
    You are an expert in startup exit strategies. Provide comprehensive advice on potential exit strategies for the given startup, considering its business description, financials, and market position. Your JSON response should include:

    1. Recommended exit strategies, ranked by suitability
    2. For each recommended strategy:
       - Pros and cons
       - Potential timeline
       - Estimated valuation range
       - Key steps to prepare for this exit
       - Potential acquirers or merger partners (if applicable)
    3. IPO readiness assessment (if applicable)
    4. Factors that could impact exit opportunities
    5. Key metrics to improve before pursuing an exit
    6. Potential challenges and how to address them
    7. Tax considerations for different exit strategies
    8. Recommendations for founder and employee equity
    9. Case studies of similar companies' exits
    10. Resources for further exit planning

    Provide actionable advice that can help the startup plan for a successful exit. Return the exit strategy analysis as a JSON object wrapped in a code block.
    """

    user_content = f"Advise on exit strategies for the following startup: {business_description}. Financials: {financials}. Market position: {market_position}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        exit_strategies = extract_json(response_content)

        if exit_strategies is None:
            return {"error": "Failed to generate or parse the exit strategy advice."}

        return exit_strategies

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def culture_team_building_advisor(company_values, team_size, remote_or_onsite):
    system_content = """
    You are an expert in startup culture and team building. Provide comprehensive advice on creating a strong company culture and building an effective team, considering the company's values, team size, and work arrangement. Your JSON response should include:

    1. Recommended cultural pillars aligned with company values
    2. Team structure and org chart suggestions
    3. Hiring strategies and best practices
    4. Onboarding process recommendations
    5. Employee engagement and retention tactics
    6. Performance management and feedback systems
    7. Communication tools and practices (especially for remote teams)
    8. Team building activities and events
    9. Diversity and inclusion initiatives
    10. Leadership development programs
    11. Conflict resolution strategies
    12. Work-life balance and wellness programs
    13. Recognition and reward systems
    14. Knowledge sharing and continuous learning approaches
    15. Scaling culture as the company grows

    Provide actionable advice that can help the startup build a strong, cohesive team and maintain a positive culture. Return the culture and team building strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Advise on culture and team building for a startup with the following values: {company_values}. Team size: {team_size}. Work arrangement: {remote_or_onsite}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        culture_strategy = extract_json(response_content)

        if culture_strategy is None:
            return {"error": "Failed to generate or parse the culture and team building advice."}

        return culture_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_pivot_analyzer(current_business_model, market_challenges, potential_pivot_options):
    system_content = """
    You are an expert in startup pivots and strategic shifts. Analyze the current business model, market challenges, and potential pivot options to provide comprehensive advice on whether and how to pivot. Your JSON response should include:

    1. Assessment of the current business model viability
    2. Analysis of market challenges and their impact
    3. Evaluation of each potential pivot option:
       - Pros and cons
       - Market potential
       - Resource requirements
       - Risks involved
    4. Recommended pivot strategy (if applicable)
    5. Step-by-step pivot implementation plan
    6. Key metrics to track during and after the pivot
    7. Communication strategy for stakeholders (team, investors, customers)
    8. Potential challenges in pivoting and how to address them
    9. Timeline for pivot execution
    10. Post-pivot success indicators
    11. Case studies of successful pivots in similar situations
    12. Alternative strategies to pivoting (if applicable)

    Provide a detailed and actionable analysis that can guide the startup's decision-making process regarding a potential pivot. Return the pivot analysis as a JSON object wrapped in a code block.
    """

    user_content = f"Analyze pivot options for a startup with the following current business model: {current_business_model}. Market challenges: {market_challenges}. Potential pivot options: {potential_pivot_options}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        pivot_analysis = extract_json(response_content)

        if pivot_analysis is None:
            return {"error": "Failed to generate or parse the pivot analysis."}

        return pivot_analysis

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_ecosystem_analyzer(industry, location, startup_stage):
    system_content = """
    You are an expert in analyzing startup ecosystems. Provide a comprehensive analysis of the startup ecosystem for the given industry, location, and startup stage. Your JSON response should include:

    1. Overview of the startup ecosystem in the specified location
    2. Key players in the ecosystem:
       - Prominent startups
       - Venture capital firms and angel investors
       - Accelerators and incubators
       - Coworking spaces
       - Universities and research institutions
    3. Industry-specific trends and opportunities
    4. Funding landscape and recent notable investments
    5. Talent pool analysis and hiring trends
    6. Regulatory environment and government support
    7. Networking events and conferences
    8. Resources available for startups at the specified stage
    9. Challenges specific to the ecosystem
    10. Comparison with other major startup hubs
    11. Success stories and case studies from the ecosystem
    12. Future outlook and growth potential
    13. Recommendations for leveraging the ecosystem

    Provide actionable insights that can help the startup take advantage of the ecosystem's strengths and navigate its challenges. Return the ecosystem analysis as a JSON object wrapped in a code block.
    """

    user_content = f"Analyze the startup ecosystem for the following parameters: Industry: {industry}, Location: {location}, Startup Stage: {startup_stage}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        ecosystem_analysis = extract_json(response_content)

        if ecosystem_analysis is None:
            return {"error": "Failed to generate or parse the ecosystem analysis."}

        return ecosystem_analysis

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def internationalization_advisor(business_description, current_markets, target_markets):
    system_content = """
    You are an expert in startup internationalization strategies. Provide comprehensive advice on expanding the given business into new international markets. Your JSON response should include:

    1. Assessment of the business's readiness for international expansion
    2. Analysis of each target market:
       - Market size and growth potential
       - Competitive landscape
       - Cultural considerations
       - Regulatory and legal requirements
       - Economic factors
    3. Recommended entry strategy for each market (e.g., direct export, licensing, joint venture, acquisition)
    4. Localization requirements:
       - Product/service adaptations
       - Marketing and branding adjustments
       - Pricing strategies
    5. Operational considerations:
       - Supply chain and logistics
       - Human resources and talent acquisition
       - Technology and infrastructure needs
    6. Financial projections and funding requirements for expansion
    7. Risk assessment and mitigation strategies
    8. Timeline for phased international expansion
    9. Key performance indicators for measuring international success
    10. Potential partnerships or acquisition targets in target markets
    11. Case studies of successful international expansions in similar industries
    12. Resources and tools for managing international operations

    Provide actionable advice that can guide the startup's international expansion efforts. Return the internationalization strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Advise on internationalization strategy for the following business: {business_description}. Current markets: {current_markets}. Target markets for expansion: {target_markets}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        internationalization_strategy = extract_json(response_content)

        if internationalization_strategy is None:
            return {"error": "Failed to generate or parse the internationalization strategy."}

        return internationalization_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_board_advisor(company_stage, current_board_composition, key_challenges):
    system_content = """
    You are an expert in startup governance and board management. Provide comprehensive advice on structuring and managing an effective board of directors for the startup. Your JSON response should include:

    1. Recommended board structure and size
    2. Ideal board composition:
       - Skills and expertise needed
       - Diversity considerations
       - Balance between insiders and independents
    3. Roles and responsibilities of board members
    4. Frequency and format of board meetings
    5. Key committees to establish (e.g., audit, compensation, nominating)
    6. Board communication and reporting practices
    7. Strategies for recruiting high-quality board members
    8. Onboarding process for new board members
    9. Board compensation guidelines
    10. Conflict resolution strategies for board disagreements
    11. Board's role in addressing the company's key challenges
    12. Legal and fiduciary responsibilities of board members
    13. Board evaluation and performance metrics
    14. Succession planning for board members and executives
    15. Tips for fostering a productive board-management relationship

    Provide actionable advice that can help the startup create and manage an effective board of directors. Return the board management strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Advise on board management for a startup at the following stage: {company_stage}. Current board composition: {current_board_composition}. Key challenges: {key_challenges}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        board_strategy = extract_json(response_content)

        if board_strategy is None:
            return {"error": "Failed to generate or parse the board management advice."}

        return board_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def innovation_strategist(business_description, industry_trends, current_capabilities):
    system_content = """
    You are an expert in startup innovation strategies. Provide comprehensive advice on fostering innovation and staying ahead of the competition. Your JSON response should include:

    1. Assessment of the startup's current innovation capabilities
    2. Analysis of industry trends and potential disruptive forces
    3. Recommended innovation focus areas aligned with business goals
    4. Innovation methodologies to implement (e.g., design thinking, lean startup, open innovation)
    5. Strategies for creating a culture of innovation
    6. Ideation techniques and processes
    7. Prototyping and testing methodologies
    8. Innovation metrics and KPIs to track
    9. Resource allocation for innovation initiatives
    10. Partnerships and collaborations to drive innovation
    11. Intellectual property strategy
    12. Innovation portfolio management
    13. Strategies for scaling successful innovations
    14. Risk management in innovation projects
    15. Case studies of successful startup innovations in similar industries
    16. Tools and technologies to support the innovation process

    Provide actionable advice that can help the startup build and maintain a competitive edge through innovation. Return the innovation strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Develop an innovation strategy for the following startup: {business_description}. Industry trends: {industry_trends}. Current capabilities: {current_capabilities}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        innovation_strategy = extract_json(response_content)

        if innovation_strategy is None:
            return {"error": "Failed to generate or parse the innovation strategy."}

        return innovation_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def crisis_management_advisor(business_description, potential_crisis_scenarios):
    system_content = """
    You are an expert in startup crisis management. Provide comprehensive advice on preparing for and managing potential crises. Your JSON response should include:

    1. Risk assessment of potential crisis scenarios
    2. Crisis management team structure and roles
    3. Crisis communication plan:
       - Internal communication strategies
       - External stakeholder communication
       - Media relations guidelines
    4. Step-by-step crisis response protocols for each scenario
    5. Business continuity planning
    6. Data backup and recovery strategies
    7. Legal and compliance considerations during crises
    8. Financial contingency planning
    9. Employee support and mental health resources
    10. Post-crisis recovery strategies
    11. Crisis simulation and training recommendations
    12. Tools and technologies for crisis management
    13. Key performance indicators for crisis preparedness
    14. Case studies of successful crisis management in startups
    15. Regular crisis plan review and update process

    Provide actionable advice that can help the startup prepare for and effectively manage potential crises. Return the crisis management strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Develop a crisis management strategy for the following startup: {business_description}. Potential crisis scenarios: {potential_crisis_scenarios}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        crisis_strategy = extract_json(response_content)

        if crisis_strategy is None:
            return {"error": "Failed to generate or parse the crisis management strategy."}

        return crisis_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def sustainability_advisor(business_description, industry, current_practices):
    system_content = """
    You are an expert in sustainable business practices for startups. Provide comprehensive advice on implementing sustainability initiatives that align with the startup's goals and industry. Your JSON response should include:

    1. Assessment of current sustainability practices
    2. Industry-specific sustainability challenges and opportunities
    3. Recommended sustainability goals and targets
    4. Strategies for reducing environmental impact:
       - Energy efficiency measures
       - Waste reduction and recycling programs
       - Sustainable sourcing practices
    5. Social responsibility initiatives:
       - Diversity and inclusion programs
       - Community engagement strategies
       - Ethical labor practices
    6. Governance and transparency recommendations
    7. Sustainable product/service development opportunities
    8. Green marketing and branding strategies
    9. Sustainability reporting and metrics
    10. Potential certifications and standards to pursue (e.g., B Corp, ISO 14001)
    11. Partnerships and collaborations for sustainability
    12. Employee engagement in sustainability efforts
    13. Cost-benefit analysis of sustainability initiatives
    14. Funding opportunities for sustainable startups
    15. Case studies of successful sustainability programs in similar startups
    16. Long-term sustainability roadmap

    Provide actionable advice that can help the startup integrate sustainability into its core business strategy. Return the sustainability strategy as a JSON object wrapped in a code block.
    """

    user_content = f"Develop a sustainability strategy for the following startup: {business_description}. Industry: {industry}. Current sustainability practices: {current_practices}"

    try:
        response = generate_chat_response(system_content, user_content)
        response_content = response.text
        sustainability_strategy = extract_json(response_content)

        if sustainability_strategy is None:
            return {"error": "Failed to generate or parse the sustainability strategy."}

        return sustainability_strategy

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    
def startup_advisor_hub(query_type, **kwargs):
    advisor_functions = {
        "business_consultant": business_consultant,
        "market_research": market_research_agent,
        "financial_projections": financial_projections_generator,
        "pitch_deck": pitch_deck_creator,
        "competitive_analysis": competitive_analysis_agent,
        "product_development": product_development_roadmap,
        "investor_pitch": investor_pitch_simulator,
        "legal_advice": startup_legal_advisor,
        "funding_strategy": funding_strategy_advisor,
        "growth_hacking": growth_hacking_strategist,
        "tech_stack": technology_stack_advisor,
        "customer_personas": customer_persona_generator,
        "risk_assessment": startup_risk_assessment,
        "valuation": startup_valuation_estimator,
        "exit_strategy": exit_strategy_advisor,
        "culture_team_building": culture_team_building_advisor,
        "pivot_analysis": startup_pivot_analyzer,
        "ecosystem_analysis": startup_ecosystem_analyzer,
        "internationalization": internationalization_advisor,
        "board_management": startup_board_advisor,
        "innovation_strategy": innovation_strategist,
        "crisis_management": crisis_management_advisor,
        "sustainability": sustainability_advisor
    }

    if query_type not in advisor_functions:
        return {"error": f"Invalid query type. Available types are: {', '.join(advisor_functions.keys())}"}

    try:
        result = advisor_functions[query_type](**kwargs)
        return result
    except Exception as e:
        return {"error": f"An error occurred while processing your request: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Business consultant example
    business_idea = "A mobile app that connects local farmers directly with consumers for fresh produce delivery"
    result = startup_advisor_hub("business_consultant", idea_description=business_idea)
    print(json.dumps(result, indent=2))

    # Market research example
    result = startup_advisor_hub("market_research", industry="AgTech", target_market="Urban consumers interested in locally sourced produce")
    print(json.dumps(result, indent=2))

    # Financial projections example
    result = startup_advisor_hub("financial_projections", business_description="Farm-to-table produce delivery app", initial_investment=500000)
    print(json.dumps(result, indent=2))
