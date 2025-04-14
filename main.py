import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Microplastics Awareness",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 28px;
        font-weight: bold;
        color: #005cb2;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .section {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .citation {
        font-size: 14px;
        font-style: italic;
        color: #616161;
    }
    .highlight {
        background-color: #fff9c4;
        padding: 2px 5px;
        border-radius: 3px;
    }
    .formula {
        font-family: monospace;
        background-color: #f1f1f1;
        padding: 5px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Navigation sidebar
st.sidebar.markdown("# Navigation")
page = st.sidebar.radio("Go to", [
    "Home",
    "Types of Plastics",
    "Microplastics Formation",
    "Environmental & Health Impacts",
    "Common Plastic Items Analysis",
    "Interactive Microplastic Journey",
    "Solutions & Approaches",
    "References"
])

# Display the selected page
if page == "Home":
    st.markdown("<div class='main-header'>Microplastics: The Invisible Threat</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        Welcome to our comprehensive resource on microplastics, their formation, impacts, and potential solutions.
        
        Plastic pollution has become one of the most pressing environmental challenges of our time, with microplastics emerging as a particularly concerning aspect of this global issue.
        
        This website aims to provide scientific information about microplastics, focusing on the chemistry behind plastic materials, how they break down into microplastics, and the various approaches being taken to address this growing problem.
        
        ### What are Microplastics?
        
        <div class='info-box'>
        Microplastics are tiny plastic particles less than 5 millimeters (0.2 inches) in diameter that result from the breakdown of larger plastic items or are manufactured at that small size for specific purposes.
        </div>
        
        They have been found throughout our environment - in oceans, freshwater systems, soil, air, and even in human and animal bodies. The ubiquity of these particles raises important questions about their long-term impact on ecosystems and human health.
        
        Use the navigation panel on the left to explore different aspects of microplastics and learn about the chemistry, environmental impacts, and potential solutions to this global challenge.
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://via.placeholder.com/400x300?text=Microplastics+Image", caption="Visualization of microplastics found in the environment")
        
        st.markdown("""
        <div class='info-box'>
        <strong>Did you know?</strong> Scientists estimate that more than <span class='highlight'>14 million tons</span> of plastic end up in the ocean every year, much of which degrades into microplastics over time.
        </div>
        """, unsafe_allow_html=True)

elif page == "Types of Plastics":
    st.markdown("<div class='main-header'>Types of Plastics and Their Chemical Structure</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='section'>
    Plastics are synthetic or semi-synthetic materials made from polymers - long chains of repeating molecular units. 
    Different types of plastics have unique chemical structures that determine their properties and applications.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='sub-header'>Major Types of Plastics</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Thermoplastics
        These plastics can be melted and reformed repeatedly when heated.
        
        1. **Polyethylene (PE)**
           - **Chemical Structure**: (C₂H₄)n
           - **Formation**: Polymerization of ethylene monomers
           - **Types**: HDPE (High-Density), LDPE (Low-Density)
           - **Applications**: Plastic bags, bottles, toys
        
        2. **Polypropylene (PP)**
           - **Chemical Structure**: (C₃H₆)n
           - **Formation**: Polymerization of propylene monomers
           - **Applications**: Food containers, automotive parts
        
        3. **Polyethylene Terephthalate (PET)**
           - **Chemical Structure**: (C₁₀H₈O₄)n
           - **Formation**: Condensation polymerization of terephthalic acid and ethylene glycol
           - **Applications**: Beverage bottles, food packaging
        
        4. **Polyvinyl Chloride (PVC)**
           - **Chemical Structure**: (C₂H₃Cl)n
           - **Formation**: Polymerization of vinyl chloride monomers
           - **Applications**: Pipes, wire insulation, flooring
        """)
    
    with col2:
        st.markdown("""
        ### Thermosetting Plastics
        These plastics cannot be melted and reformed once shaped.
        
        1. **Polyurethane (PUR)**
           - **Chemical Structure**: Complex, containing urethane links
           - **Formation**: Reaction of diisocyanates with polyols
           - **Applications**: Foams, insulation, coatings
        
        2. **Epoxy Resins**
           - **Chemical Structure**: Contains epoxide groups
           - **Formation**: Reaction of epichlorohydrin with bisphenol A
           - **Applications**: Adhesives, coatings, composites
        
        3. **Phenolic Resins**
           - **Chemical Structure**: Based on phenol-formaldehyde polymers
           - **Formation**: Condensation of phenol with formaldehyde
           - **Applications**: Electric insulators, adhesives
        
        ### Bioplastics
        
        - **Polylactic Acid (PLA)**
           - **Chemical Structure**: (C₃H₄O₂)n
           - **Formation**: Polymerization of lactic acid derived from plants
           - **Applications**: Food packaging, medical implants
        """)
    
    st.markdown("<div class='sub-header'>Polymerization Reactions</div>", unsafe_allow_html=True)
    
    st.markdown("""
    ### Addition Polymerization
    
    <div class='formula'>
    nCH₂=CH₂ → -(CH₂-CH₂)n-
    </div>
    
    In addition polymerization, monomers with double bonds (like ethylene) join together without producing any byproducts. This process typically requires catalysts and specific conditions of temperature and pressure.
    
    ### Condensation Polymerization
    
    <div class='formula'>
    nHOOC-R-COOH + nHO-R'-OH → -(OOC-R-COO-R')n- + nH₂O
    </div>
    
    In condensation polymerization, monomers with functional groups react, typically producing water or another small molecule as a byproduct. This is how polyesters like PET are formed.
    
    <div class='info-box'>
    The unique chemical structure of each plastic type determines its properties, including durability, flexibility, transparency, and resistance to heat and chemicals. These properties make plastics versatile but also contribute to their persistence in the environment when they become waste.
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive element: Polymer structure visualization
    st.markdown("<div class='sub-header'>Interactive: Explore Polymer Structures</div>", unsafe_allow_html=True)
    
    polymer_type = st.selectbox(
        "Select a polymer to view its structure:",
        ["Polyethylene (PE)", "Polypropylene (PP)", "Polyethylene Terephthalate (PET)", "Polyvinyl Chloride (PVC)"]
    )
    
    polymer_structures = {
        "Polyethylene (PE)": "https://via.placeholder.com/600x200?text=Polyethylene+Structure",
        "Polypropylene (PP)": "https://via.placeholder.com/600x200?text=Polypropylene+Structure",
        "Polyethylene Terephthalate (PET)": "https://via.placeholder.com/600x200?text=PET+Structure",
        "Polyvinyl Chloride (PVC)": "https://via.placeholder.com/600x200?text=PVC+Structure"
    }
    
    st.image(polymer_structures[polymer_type], caption=f"Chemical structure of {polymer_type}")

elif page == "Microplastics Formation":
    st.markdown("<div class='main-header'>How Microplastics Form and Enter the Body</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='section'>
    Microplastics are classified based on their source as either primary or secondary microplastics. Understanding how they form and enter biological systems is crucial to assessing their impact.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("<div class='sub-header'>Primary vs. Secondary Microplastics</div>", unsafe_allow_html=True)
        
        st.markdown("""
        ### Primary Microplastics
        These are plastics manufactured at microscopic size for specific purposes:
        
        - Microbeads in personal care products (face scrubs, toothpastes)
        - Pre-production plastic pellets (nurdles)
        - Microfibers from synthetic textiles
        - Tire wear particles from vehicle tires
        
        ### Secondary Microplastics
        These result from the degradation of larger plastic items due to:
        
        - **Photodegradation**: UV radiation from sunlight breaks polymer bonds
        - **Mechanical Degradation**: Physical forces (waves, friction) fragment plastics
        - **Thermal Degradation**: Temperature fluctuations cause brittleness and fragmentation
        - **Biodegradation**: Partial breakdown by microorganisms
        
        <div class='info-box'>
        The chemical degradation process of plastics often involves:
        <ul>
            <li>Chain scission: Breaking of the polymer chains</li>
            <li>Oxidation: Reaction with oxygen, often catalyzed by UV light</li>
            <li>Hydrolysis: Reaction with water molecules</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://via.placeholder.com/350x400?text=Microplastic+Formation+Process", caption="Formation process of microplastics from larger plastic debris")
    
    st.markdown("<div class='sub-header'>Pathways into the Human Body</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Ingestion
        - Consumption of contaminated food (especially seafood)
        - Drinking water containing microplastics
        - Contaminated table salt, sugar, honey
        - Consumption of food stored in plastic containers
        
        <div class='formula'>
        Average person may ingest ~5g of plastic weekly (equivalent to a credit card)
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### Inhalation
        - Airborne microplastic particles
        - Microfibers from synthetic textiles
        - Tire wear particles in urban environments
        - Indoor dust containing plastic fragments
        
        <div class='formula'>
        Microplastic concentration in urban air: 0.3-1.5 particles/m³
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        ### Dermal Contact
        - Cosmetics containing microbeads
        - Synthetic clothing fibers
        - Dust particles settled on skin
        - Personal care products in plastic packaging
        
        <div class='formula'>
        Microplastics < 20 μm may potentially penetrate skin
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div class='sub-header'>Chemical Mechanisms of Degradation</div>", unsafe_allow_html=True)
    
    st.markdown("""
    ### Photodegradation Process
    
    <div class='formula'>
    R-CH₂-CH₂-R' + O₂ + hν → R-CH₂-CH(OO•)-R' → R-CH₂-C(=O)-R' + •OH
    </div>
    
    UV radiation from sunlight provides energy to break chemical bonds in polymers, often initiating a process called photo-oxidation, where oxygen reacts with the free radicals formed during bond cleavage.
    
    ### Hydrolysis of Polyesters
    
    <div class='formula'>
    -(O-R-COO-R'-)n- + H₂O → HO-R-COOH + HO-R'-OH
    </div>
    
    For certain plastics like PET or PLA, water molecules can attack the ester bonds, leading to chain breakage and the formation of smaller fragments.
    
    <div class='info-box'>
    The degradation rate varies significantly between plastic types. For example, PET may take 450+ years to fully degrade in the environment, while polystyrene can persist for thousands of years.
    </div>
    """, unsafe_allow_html=True)
    
    # Add interactive element
    st.markdown("<div class='sub-header'>Interactive: Explore Entry Pathways</div>", unsafe_allow_html=True)
    
    pathway = st.selectbox(
        "Select a pathway to learn more about how microplastics enter:",
        ["Food Chain", "Water Systems", "Air/Inhalation", "Consumer Products"]
    )
    
    pathway_info = {
        "Food Chain": {
            "text": """
            **Microplastics in the Food Chain**
            
            The bioaccumulation process starts with plankton and small aquatic organisms ingesting microplastics. These are then consumed by larger species, with concentration increasing at each trophic level.
            
            Studies have found microplastics in:
            - 114 aquatic species, with over half being commercially important for fisheries
            - 100% of mussels samples from certain coastal areas
            - Up to 300 microplastic particles per fish in some heavily polluted areas
            
            The chemical process of bioaccumulation involves hydrophobic organic contaminants (like PCBs and PAHs) adsorbing to plastic surfaces, increasing their concentration before being ingested.
            """,
            "image": "https://via.placeholder.com/800x300?text=Food+Chain+Microplastic+Transfer"
        },
        "Water Systems": {
            "text": """
            **Microplastics in Water Systems**
            
            Microplastics enter water systems through:
            - Wastewater treatment plant effluent (microfibers from laundry, microbeads from products)
            - Runoff from urban areas and roads (tire particles, litter fragmentation)
            - Atmospheric deposition
            
            Chemical interactions in water include:
            - Leaching of plasticizers and additives
            - Sorption of environmental pollutants
            - Surface weathering increasing the surface area for chemical reactions
            
            Studies have found 10-20 microplastic particles per liter in many municipal water supplies worldwide.
            """,
            "image": "https://via.placeholder.com/800x300?text=Water+Systems+Microplastic+Distribution"
        },
        "Air/Inhalation": {
            "text": """
            **Airborne Microplastics**
            
            Microplastics become airborne through:
            - Weathering and fragmentation of larger plastics
            - Tire wear particles from road traffic
            - Synthetic fiber release during textile manufacturing and use
            - Industrial processes involving plastics
            
            Particle size determines respirability:
            - Particles > 10 μm: Trapped in upper respiratory tract
            - Particles 2.5-10 μm: Can reach bronchi
            - Particles < 2.5 μm: Can reach alveoli
            - Particles < 0.1 μm (nanoplastics): Potential to enter bloodstream
            
            Indoor air concentrations can be 2-5 times higher than outdoor concentrations due to synthetic carpets, furnishings, and limited air circulation.
            """,
            "image": "https://via.placeholder.com/800x300?text=Airborne+Microplastic+Pathways"
        },
        "Consumer Products": {
            "text": """
            **Consumer Products as Sources**
            
            Many everyday products contain or release microplastics:
            
            - Cosmetics: Microbeads in exfoliants, toothpaste (typically polyethylene)
            - Synthetic clothing: Each wash can release 700,000-12,000,000 microfibers
            - Food packaging: Migration of plastic particles into food
            - Tea bags: Some "silken" tea bags can release billions of nanoplastic particles
            
            Chemical concerns include:
            - Phthalates and BPA leaching from packaging
            - Flame retardants from textiles
            - Colorants and other additives from consumer plastics
            
            A 2019 study estimated that humans may consume 39,000-52,000 microplastic particles annually from these sources.
            """,
            "image": "https://via.placeholder.com/800x300?text=Consumer+Products+Microplastic+Sources"
        }
    }
    
    st.markdown(pathway_info[pathway]["text"], unsafe_allow_html=True)
    st.image(pathway_info[pathway]["image"], caption=f"Visualization of {pathway} pathway")

elif page == "Environmental & Health Impacts":
    st.markdown("<div class='main-header'>Environmental and Human Health Impacts of Microplastics</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='section'>
    The widespread distribution of microplastics has raised significant concerns about their potential impacts on ecosystems and human health. These impacts are linked to both the physical presence of plastic particles and the chemicals associated with them.
    </div>
    """, unsafe_allow_html=True)
    
    # Environmental impacts
    st.markdown("<div class='sub-header'>Environmental Impacts</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### Aquatic Ecosystems
        
        - **Physical Effects**: Ingestion by marine organisms causing intestinal blockage, false satiation, reduced feeding
        - **Trophic Transfer**: Microplastics transfer up food chains, with biomagnification potential
        - **Habitat Alteration**: Plastic particles can change sediment properties, affecting benthic communities
        
        ### Terrestrial Ecosystems
        
        - **Soil Quality**: Microplastics alter soil structure, water holding capacity, and bulk density
        - **Earthworm and Arthropod Impacts**: Reduced growth, reproduction, and burrowing ability
        - **Plant Growth**: Studies show altered root growth and reduced germination rates in contaminated soils
        
        ### Chemical Effects
        
        - **Leaching**: Release of plastic additives (plasticizers, flame retardants, stabilizers)
        - **Vector Effect**: Microplastics can adsorb and transport persistent organic pollutants (POPs)
        - **Chemical Formula Example**: Leaching of bisphenol A (BPA, C₁₅H₁₆O₂) from polycarbonate plastics:
        
        <div class='formula'>
        (C₁₆H₁₄O₃)n + H₂O → (C₁₆H₁₄O₃)n-1 + C₁₅H₁₆O₂
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Create a simple bar chart for visualization
        ecosystem_types = ['Marine', 'Freshwater', 'Terrestrial']
        microplastic_concentration = [1245, 890, 425]  # particles/kg (example data)
        
        fig, ax = plt.subplots()
        ax.bar(ecosystem_types, microplastic_concentration, color='#1E88E5')
        ax.set_ylabel('Average microplastic particles per kg')
        ax.set_title('Microplastic Prevalence by Ecosystem Type')
        st.pyplot(fig)
        
        st.markdown("""
        <div class='info-box'>
        Studies have found microplastics in the deepest ocean trenches, on Mount Everest, in Arctic ice, and in remote uninhabited islands - demonstrating their global reach and persistence.
        </div>
        """, unsafe_allow_html=True)
    
    # Human health impacts
    st.markdown("<div class='sub-header'>Human Health Impacts</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### Physiological Effects
        
        - **Respiratory System**: Inhalation of microplastics may cause inflammation, respiratory distress
        - **Digestive System**: Potential for intestinal inflammation, gut microbiome disturbance
        - **Cellular Level**: Evidence of oxidative stress, cytotoxicity, genotoxicity
        - **Particle Translocation**: Particles <150 μm can potentially penetrate tissue and enter circulation
        
        ### Chemical Toxicity
        
        - **Endocrine Disruption**: Chemicals like BPA and phthalates can interfere with hormone systems
        - **Carcinogenic Potential**: Some plastic additives are classified as possible carcinogens
        - **Reproductive Effects**: Studies indicate potential impacts on fertility and fetal development
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### Emerging Research Areas
        
        - **Immune System Effects**: Potential for inflammatory responses and immune modulation
        - **Neurotoxicity**: Possible impacts on nervous system development and function
        - **Microbiome Disruption**: Alteration of gut microbial communities and metabolic processes
        
        ### Chemical Mechanisms of Toxicity
        
        - **Free Radical Generation**: Particles trigger oxidative stress via reaction:
        
        <div class='formula'>
        O₂ + e⁻ → O₂•⁻ (superoxide radical)
        2O₂•⁻ + 2H⁺ → H₂O₂ + O₂
        H₂O₂ + Fe²⁺ → OH• + OH⁻ + Fe³⁺
        </div>
        
        - **Membrane Disruption**: Physical interaction with cell membranes leading to damage
        """, unsafe_allow_html=True)
    
    # Research data visualization
    st.markdown("<div class='sub-header'>Research Evidence: Microplastic Occurrence in Human Systems</div>", unsafe_allow_html=True)
    
    # Create sample data for visualization
    human_systems = ['Blood', 'Lung Tissue', 'Placenta', 'Colon', 'Stool']
    detection_percentages = [77, 87, 60, 95, 94]
    
    fig = px.bar(
        x=human_systems,
        y=detection_percentages,
        labels={'x': 'Human Biological System', 'y': 'Detection Rate (%)'},
        title='Microplastic Detection Rates in Human Biological Samples',
        color=detection_percentages,
        color_continuous_scale='Blues'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class='info-box'>
    <strong>Research Challenge:</strong> While presence of microplastics in human systems has been confirmed, establishing clear causal relationships between exposure and specific health outcomes remains challenging due to:
    <ul>
        <li>Difficulties in controlling for other environmental factors</li>
        <li>Ethical limitations on human experimental studies</li>
        <li>Long latency periods for chronic health effects</li>
        <li>Complex mixtures of plastic types and associated chemicals</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Add interactive element
    st.markdown("<div class='sub-header'>Interactive: Explore Chemical Impacts</div>", unsafe_allow_html=True)
    
    chemical = st.selectbox(
        "Select a plastic-associated chemical to learn about its impacts:",
        ["Bisphenol A (BPA)", "Phthalates", "Polybrominated diphenyl ethers (PBDEs)", "Styrene"]
    )
    
    chemical_info = {
        "Bisphenol A (BPA)": {
            "formula": "C₁₅H₁₆O₂",
            "structure": "https://via.placeholder.com/400x200?text=BPA+Structure",
            "impacts": """
                - **Endocrine disruption**: Mimics estrogen, binding to estrogen receptors
                - **Reproductive effects**: Linked to reduced sperm quality, altered puberty timing
                - **Metabolic impacts**: Associated with obesity, insulin resistance
                - **Neurodevelopmental concerns**: Potential impacts on brain development
                
                **Reaction in body**: BPA can bind to nuclear estrogen receptors (ERα, ERβ) and membrane-bound estrogen receptors, activating estrogen response elements (EREs) and altering gene expression.
            """
        },
        "Phthalates": {
            "formula": "C₈H₄O₄(R)₂ (general structure)",
            "structure": "https://via.placeholder.com/400x200?text=Phthalates+Structure",
            "impacts": """
                - **Anti-androgenic activity**: Can reduce testosterone production
                - **Reproductive development**: Associated with genital malformations
                - **Respiratory effects**: Linked to asthma and allergies
                - **Neurological impacts**: Potential effects on cognitive development
                
                **Metabolism**: Phthalates undergo phase I hydrolysis to monoesters:
                C₈H₄O₄(R)₂ + H₂O → C₈H₄O₄(R)(H) + ROH
                
                These monoesters can then undergo further oxidation and conjugation.
            """
        },
        "Polybrominated diphenyl ethers (PBDEs)": {
            "formula": "C₁₂H(10-x)BrₓO (x = 1-10)",
            "structure": "https://via.placeholder.com/400x200?text=PBDEs+Structure",
            "impacts": """
                - **Thyroid hormone disruption**: Structural similarity to T3 and T4
                - **Neurodevelopmental effects**: Impact on learning and memory
                - **Potential carcinogenicity**: Some evidence from animal studies
                - **Persistent bioaccumulative**: Long half-life in human tissues
                
                **Bioaccumulation**: PBDEs are lipophilic and accumulate in fatty tissues. They can undergo debromination in the body:
                C₁₂H₅Br₅O → C₁₂H₆Br₄O + Br⁻
            """
        },
        "Styrene": {
            "formula": "C₈H₈",
            "structure": "https://via.placeholder.com/400x200?text=Styrene+Structure",
            "impacts": """
                - **Neurotoxicity**: Can affect central and peripheral nervous systems
                - **Carcinogen**: Classified as a probable human carcinogen
                - **Respiratory irritant**: Affects lung function
                - **Liver enzyme changes**: Alters metabolic enzyme function
                
                **Metabolism**: Styrene undergoes oxidation by cytochrome P450:
                C₈H₈ + O₂ + NADPH + H⁺ → C₈H₈O + NADP⁺ + H₂O
                
                The resulting styrene oxide is more reactive and can bind to DNA and proteins.
            """
        }
    }
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"### {chemical}")
        st.markdown(f"**Chemical Formula**: {chemical_info[chemical]['formula']}")
        st.image(chemical_info[chemical]['structure'], caption=f"Chemical structure of {chemical}")
    
    with col2:
        st.markdown("### Health Impacts")
        st.markdown(chemical_info[chemical]['impacts'], unsafe_allow_html=True)

elif page == "Common Plastic Items Analysis":
    st.markdown("<div class='main-header'>Analysis of Common Plastic Items</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='section'>
    Here we analyze three commonly available plastic items, examining their chemical structure, potential concerns, disposal processes, environmental impacts, and biodegradability.
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for each plastic item
    tab1, tab2, tab3 = st.tabs(["PET Bottles", "Polystyrene Foam Containers", "Polyethylene Bags"])
    
    with tab1:
        st.markdown("<div class='sub-header'>Polyethylene Terephthalate (PET) Bottles</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            ### Chemical Structure and Formation
            
            **Chemical Formula**: (C₁₀H₈O₄)n
            
            **Chemical Structure**: Linear polymer with repeating units of terephthalic acid and ethylene glycol
            
            **Formation Reaction**:
            <div class='formula'>
            n(HOOC-C₆H₄-COOH) + n(HO-CH₂-CH₂-OH) → [(OOC-C₆H₄-COO-CH₂-CH₂)]n + 2nH₂O
            </div>
            
            This is a condensation polymerization""")