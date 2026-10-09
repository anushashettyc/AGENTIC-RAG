from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

def create_rag_pdf():
    """Create a comprehensive PDF about RAG (Retrieval-Augmented Generation)"""

    doc = SimpleDocTemplate("data/pdfs/sample1.pdf", pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a5490'),
        spaceAfter=30,
        alignment=TA_CENTER
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2c5aa0'),
        spaceAfter=12,
        spaceBefore=12
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )

    # Title
    story.append(Paragraph("Retrieval-Augmented Generation (RAG)", title_style))
    story.append(Spacer(1, 0.3*inch))

    # Introduction
    story.append(Paragraph("Introduction to RAG", heading_style))
    story.append(Paragraph(
        "Retrieval-Augmented Generation (RAG) is a powerful technique that combines the strengths of "
        "large language models (LLMs) with external knowledge retrieval systems. This hybrid approach "
        "enables AI systems to generate more accurate, contextually relevant, and up-to-date responses "
        "by accessing domain-specific information stored in vector databases.",
        body_style
    ))

    story.append(Paragraph(
        "Unlike traditional LLMs that rely solely on their training data, RAG systems dynamically retrieve "
        "relevant information from external sources, reducing hallucinations and providing verifiable, "
        "source-backed responses.",
        body_style
    ))

    # Core Components
    story.append(Paragraph("Core Components of RAG Systems", heading_style))

    components = [
        ["Component", "Description", "Purpose"],
        ["Document Ingestion", "Process of loading and chunking documents into manageable pieces",
         "Prepare data for embedding"],
        ["Embedding Model", "Converts text chunks into dense vector representations",
         "Enable semantic similarity search"],
        ["Vector Database", "Stores embeddings with efficient similarity search capabilities",
         "Fast retrieval of relevant context"],
        ["Retriever", "Fetches top-k most relevant documents based on query",
         "Provide context to LLM"],
        ["Language Model", "Generates responses using retrieved context",
         "Produce accurate answers"]
    ]

    table = Table(components, colWidths=[1.8*inch, 2.5*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))

    story.append(table)
    story.append(Spacer(1, 0.3*inch))

    # RAG Pipeline
    story.append(Paragraph("The RAG Pipeline", heading_style))
    story.append(Paragraph(
        "<b>1. Indexing Phase:</b> During this phase, documents are processed and stored for later retrieval:",
        body_style
    ))

    story.append(Paragraph(
        "• <b>Document Loading:</b> Raw documents (PDFs, text files, web pages) are ingested<br/>"
        "• <b>Text Splitting:</b> Large documents are chunked into smaller, overlapping segments<br/>"
        "• <b>Embedding Generation:</b> Each chunk is converted to a vector representation<br/>"
        "• <b>Vector Storage:</b> Embeddings are stored in a vector database with metadata",
        body_style
    ))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>2. Retrieval Phase:</b> When a user query arrives, the system retrieves relevant context:",
        body_style
    ))

    story.append(Paragraph(
        "• <b>Query Embedding:</b> User question is converted to the same vector space<br/>"
        "• <b>Similarity Search:</b> Vector database finds the most similar document chunks<br/>"
        "• <b>Context Assembly:</b> Top-k results are compiled as context<br/>"
        "• <b>Reranking (Optional):</b> Results may be reordered for better relevance",
        body_style
    ))

    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "<b>3. Generation Phase:</b> The LLM generates a response using retrieved context:",
        body_style
    ))

    story.append(Paragraph(
        "• <b>Prompt Construction:</b> Query and context are combined into a prompt<br/>"
        "• <b>LLM Processing:</b> Language model generates contextually grounded response<br/>"
        "• <b>Response Delivery:</b> Answer is returned, often with source citations",
        body_style
    ))

    # Benefits
    story.append(PageBreak())
    story.append(Paragraph("Benefits of RAG", heading_style))

    benefits = [
        ("Reduced Hallucinations",
         "By grounding responses in retrieved documents, RAG significantly reduces factual errors and hallucinations."),
        ("Up-to-Date Information",
         "External knowledge bases can be updated without retraining the entire model."),
        ("Domain Specificity",
         "RAG enables LLMs to answer questions about proprietary or specialized knowledge."),
        ("Source Attribution",
         "Responses can include citations and references to source documents."),
        ("Cost Efficiency",
         "Avoids expensive fine-tuning while achieving domain adaptation."),
        ("Transparency",
         "Users can verify information by examining retrieved sources.")
    ]

    for benefit, description in benefits:
        story.append(Paragraph(f"<b>{benefit}:</b> {description}", body_style))

    # Challenges
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Challenges and Considerations", heading_style))

    story.append(Paragraph(
        "<b>Retrieval Quality:</b> The system's performance heavily depends on retrieving the right "
        "documents. Poor chunking strategies or inadequate embeddings can lead to irrelevant context being "
        "passed to the LLM.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Context Window Limitations:</b> LLMs have finite context windows, requiring careful selection "
        "of which retrieved documents to include.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Latency:</b> Adding retrieval steps increases response time compared to direct LLM inference.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Document Quality:</b> The system can only be as good as the documents in its knowledge base. "
        "Outdated or incorrect source material will lead to poor responses.",
        body_style
    ))

    # Use Cases
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Common Use Cases", heading_style))

    story.append(Paragraph(
        "• <b>Customer Support:</b> Answer queries using product documentation and FAQs<br/>"
        "• <b>Research Assistance:</b> Help researchers find and synthesize information from papers<br/>"
        "• <b>Legal Analysis:</b> Query case law and regulatory documents<br/>"
        "• <b>Technical Documentation:</b> Provide code examples and API documentation<br/>"
        "• <b>Enterprise Knowledge Management:</b> Make internal documents searchable and accessible<br/>"
        "• <b>Educational Tutoring:</b> Answer questions based on course materials",
        body_style
    ))

    # Conclusion
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Conclusion", heading_style))
    story.append(Paragraph(
        "RAG represents a significant advancement in making LLMs more practical and reliable for real-world "
        "applications. By combining the generative capabilities of large language models with the precision "
        "of information retrieval systems, RAG enables AI systems that are both knowledgeable and verifiable. "
        "As the technology continues to evolve, we can expect even more sophisticated retrieval mechanisms and "
        "integration patterns.",
        body_style
    ))

    doc.build(story)
    print("Created sample1.pdf: Introduction to RAG")


def create_agentic_rag_pdf():
    """Create a comprehensive PDF about Agentic RAG"""

    doc = SimpleDocTemplate("data/pdfs/sample2.pdf", pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#8b3a62'),
        spaceAfter=30,
        alignment=TA_CENTER
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#a0466b'),
        spaceAfter=12,
        spaceBefore=12
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )

    # Title
    story.append(Paragraph("Agentic RAG: The Next Evolution", title_style))
    story.append(Spacer(1, 0.3*inch))

    # Introduction
    story.append(Paragraph("What is Agentic RAG?", heading_style))
    story.append(Paragraph(
        "Agentic RAG extends traditional RAG by incorporating autonomous agent capabilities, enabling the "
        "system to make intelligent decisions about information retrieval and processing. Rather than following "
        "a fixed pipeline, Agentic RAG systems can reason about what information they need, choose appropriate "
        "retrieval strategies, and iteratively refine their approach based on intermediate results.",
        body_style
    ))

    story.append(Paragraph(
        "This paradigm shift transforms RAG from a reactive retrieval-generation system into a proactive, "
        "goal-oriented agent that can plan, execute, and adapt its information-gathering strategy.",
        body_style
    ))

    # Key Differences
    story.append(Paragraph("Traditional RAG vs. Agentic RAG", heading_style))

    comparison = [
        ["Aspect", "Traditional RAG", "Agentic RAG"],
        ["Retrieval Strategy", "Single-step, fixed approach", "Multi-step, adaptive reasoning"],
        ["Query Processing", "Direct query embedding", "Query decomposition and planning"],
        ["Information Sources", "Single vector database", "Multiple tools and sources"],
        ["Decision Making", "Predetermined pipeline", "Autonomous tool selection"],
        ["Iteration", "One-shot retrieval", "Iterative refinement"],
        ["Error Handling", "Limited or none", "Self-correction and verification"]
    ]

    table = Table(comparison, colWidths=[1.8*inch, 2.3*inch, 2.3*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#a0466b')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0e6eb')),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))

    story.append(table)
    story.append(Spacer(1, 0.3*inch))

    # Core Capabilities
    story.append(Paragraph("Core Capabilities of Agentic RAG", heading_style))

    story.append(Paragraph(
        "<b>1. Reasoning and Planning:</b> The agent can analyze complex queries and break them down into "
        "sub-tasks. For example, a question like 'Compare the revenue growth of Tesla and Ford over the last "
        "5 years' would be decomposed into multiple retrieval and analysis steps.",
        body_style
    ))

    story.append(Paragraph(
        "<b>2. Tool Selection:</b> Unlike traditional RAG that only queries a vector database, Agentic RAG "
        "can choose from multiple tools including:",
        body_style
    ))

    story.append(Paragraph(
        "• Vector search for semantic similarity<br/>"
        "• SQL queries for structured data<br/>"
        "• Web search for current information<br/>"
        "• Calculator for mathematical operations<br/>"
        "• Code execution for data analysis<br/>"
        "• API calls to external services",
        body_style
    ))

    story.append(Paragraph(
        "<b>3. Iterative Refinement:</b> The agent can evaluate intermediate results and decide whether "
        "additional information is needed. If initial retrieval is insufficient, it can reformulate queries "
        "or try alternative approaches.",
        body_style
    ))

    story.append(Paragraph(
        "<b>4. Self-Verification:</b> Agentic RAG systems can validate their own outputs by cross-referencing "
        "multiple sources or performing consistency checks before presenting final answers.",
        body_style
    ))

    # Architecture
    story.append(PageBreak())
    story.append(Paragraph("Agentic RAG Architecture", heading_style))

    story.append(Paragraph(
        "An Agentic RAG system typically consists of the following components:",
        body_style
    ))

    architecture = [
        ["Layer", "Components", "Function"],
        ["Agent Core", "LLM with reasoning prompts, Memory module",
         "Decision making and state management"],
        ["Tool Registry", "Vector DB, Web search, Calculator, SQL, APIs",
         "Available tools for information access"],
        ["Planning Module", "Query analyzer, Task decomposer, Strategy selector",
         "Breaks down complex queries"],
        ["Execution Engine", "Tool caller, Result aggregator, Error handler",
         "Executes selected tools"],
        ["Reflection Module", "Output validator, Confidence scorer, Retry logic",
         "Evaluates and improves results"]
    ]

    table = Table(architecture, colWidths=[1.5*inch, 2.5*inch, 2.3*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#a0466b')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0e6eb')),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))

    story.append(table)
    story.append(Spacer(1, 0.3*inch))

    # Implementation Patterns
    story.append(Paragraph("Implementation Patterns", heading_style))

    story.append(Paragraph(
        "<b>ReAct Pattern (Reasoning + Acting):</b> The agent alternates between reasoning about what to do "
        "next and taking actions (using tools). Each cycle includes: Thought → Action → Observation → Repeat.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Chain-of-Thought with Tools:</b> The agent explicitly writes out its reasoning process before "
        "deciding which tool to use, improving transparency and accuracy.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Multi-Agent Collaboration:</b> Complex queries can be handled by multiple specialized agents "
        "working together, each with its own expertise and tool access.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Hierarchical Planning:</b> Large tasks are decomposed into a hierarchy of sub-tasks, with "
        "high-level planning separated from low-level execution.",
        body_style
    ))

    # Advanced Features
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Advanced Features", heading_style))

    story.append(Paragraph(
        "<b>Memory Systems:</b> Agentic RAG can maintain short-term memory (conversation context) and "
        "long-term memory (learned patterns and user preferences) to improve over time.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Dynamic Prompt Engineering:</b> The system can modify its own prompts based on the task at hand, "
        "adapting its behavior to different domains or query types.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Confidence Scoring:</b> Each retrieval and generation step can be assigned a confidence score, "
        "helping the agent decide when to seek additional information.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Query Routing:</b> Intelligent routing of queries to the most appropriate retrieval strategy or "
        "tool based on query type, complexity, and required accuracy.",
        body_style
    ))

    # Challenges
    story.append(PageBreak())
    story.append(Paragraph("Challenges in Agentic RAG", heading_style))

    story.append(Paragraph(
        "<b>Complexity Management:</b> The increased flexibility comes with added complexity in design, "
        "implementation, and debugging. Tool selection logic must be carefully crafted to avoid inefficient "
        "or incorrect retrieval paths.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Cost and Latency:</b> Multiple LLM calls for reasoning and planning can significantly increase "
        "both cost and response time compared to single-step RAG.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Reliability:</b> Autonomous agents can sometimes make unexpected decisions or get stuck in loops. "
        "Robust error handling and fallback mechanisms are essential.",
        body_style
    ))

    story.append(Paragraph(
        "<b>Evaluation:</b> Measuring the performance of Agentic RAG systems is more complex than traditional "
        "RAG, as success depends not just on final answers but on the quality of intermediate reasoning steps.",
        body_style
    ))

    # Use Cases
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Use Cases for Agentic RAG", heading_style))

    story.append(Paragraph(
        "• <b>Complex Research Tasks:</b> Academic literature review requiring synthesis across multiple papers<br/>"
        "• <b>Multi-Step Problem Solving:</b> Technical troubleshooting that requires checking logs, documentation, "
        "and system state<br/>"
        "• <b>Data Analysis:</b> Business intelligence queries requiring data retrieval, calculation, and visualization<br/>"
        "• <b>Competitive Intelligence:</b> Gathering and comparing information from multiple sources<br/>"
        "• <b>Automated Report Generation:</b> Creating comprehensive reports by pulling data from various systems<br/>"
        "• <b>Personalized Recommendations:</b> Considering user history, preferences, and current context",
        body_style
    ))

    # Best Practices
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Best Practices", heading_style))

    story.append(Paragraph(
        "1. <b>Start Simple:</b> Begin with traditional RAG and add agentic capabilities incrementally<br/>"
        "2. <b>Clear Tool Descriptions:</b> Provide detailed descriptions of when and how to use each tool<br/>"
        "3. <b>Implement Guardrails:</b> Set maximum iteration limits and validation checks<br/>"
        "4. <b>Monitor Agent Behavior:</b> Log all reasoning steps for debugging and improvement<br/>"
        "5. <b>Human-in-the-Loop:</b> For critical applications, include confirmation steps<br/>"
        "6. <b>Graceful Degradation:</b> Fall back to simpler methods when agent reasoning fails",
        body_style
    ))

    # Future Directions
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Future Directions", heading_style))

    story.append(Paragraph(
        "The future of Agentic RAG is promising, with emerging trends including: integration with multimodal "
        "models for processing images and videos; federated learning approaches for privacy-preserving retrieval; "
        "more sophisticated planning algorithms inspired by classical AI; and standardized frameworks for building "
        "and deploying agentic systems.",
        body_style
    ))

    # Conclusion
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Conclusion", heading_style))
    story.append(Paragraph(
        "Agentic RAG represents a significant leap forward from traditional RAG systems, bringing autonomous "
        "reasoning and adaptive behavior to information retrieval and generation. While it introduces new challenges "
        "in terms of complexity and resource requirements, the benefits of improved accuracy, flexibility, and "
        "capability for handling complex queries make it an exciting frontier in AI application development. As "
        "tools and frameworks mature, Agentic RAG will likely become the standard approach for sophisticated "
        "AI-powered knowledge systems.",
        body_style
    ))

    doc.build(story)
    print("Created sample2.pdf: Agentic RAG - The Next Evolution")


if __name__ == "__main__":
    create_rag_pdf()
    create_agentic_rag_pdf()
    print("\nBoth PDFs created successfully in data/pdfs/")
