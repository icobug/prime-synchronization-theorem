"""
CHEMICAL EXPERIMENT GUIDE for Goldbach Bridge Theorem
Complete BZ Reaction Implementation
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime

def create_chemical_experiment_pdf():
    """Create PDF guide specifically for chemical experiment."""
    
    pdf_filename = f"Goldbach_Chemical_Experiment_{datetime.now().strftime('%Y%m%d')}.pdf"
    
    with PdfPages(pdf_filename) as pdf:
        # ============================================
        # COVER PAGE
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        cover_text = """CHEMICAL EXPERIMENT
GOLDBACH BRIDGE THEOREM VERIFICATION

Belousov-Zhabotinsky (BZ) Reaction Implementation
Prime Number Synchronization in Chemical Oscillators
        
Complete Step-by-Step Guide"""
        
        ax.text(0.5, 0.7, cover_text, ha='center', va='center', 
                fontsize=14, fontweight='bold')
        ax.text(0.5, 0.4, f"Generated: {datetime.now().strftime('%Y-%m-%d')}", 
                ha='center', va='center', fontsize=10)
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # TABLE OF CONTENTS
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        toc_text = """TABLE OF CONTENTS

1. EXPERIMENT OVERVIEW
   1.1 Scientific Goal
   1.2 Chemical Principle
   1.3 Expected Results

2. MATERIALS & PREPARATION
   2.1 Chemical Shopping List
   2.2 Solution Preparation
   2.3 Oscillator Setup

3. EXPERIMENTAL PROCEDURE
   3.1 Day 1: Preparation
   3.2 Day 2: Setup & Observation
   3.3 Goldbach Connections
   3.4 κ Control Methods

4. MEASUREMENT & ANALYSIS
   4.1 Video Recording Setup
   4.2 Color Analysis Methods
   4.3 Synchronization Detection
   4.4 Finding κ_c

5. SAFETY & TROUBLESHOOTING
   5.1 Safety Protocol
   5.2 Common Problems
   5.3 Waste Disposal

6. DATA PUBLICATION
   6.1 Documenting Results
   6.2 Scientific Paper Outline
   6.3 Presentation Tips"""
        
        ax.text(0.05, 0.95, toc_text, ha='left', va='top', 
                fontsize=10, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # SECTION 1: EXPERIMENT OVERVIEW
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        overview_text = """1. EXPERIMENT OVERVIEW

1.1 SCIENTIFIC GOAL:
To experimentally verify the Goldbach Bridge Theorem using
chemical oscillators (Belousov-Zhabotinsky reactions).

Key Verification Points:
• Demonstrate prime number synchronization
• Measure critical coupling strength κ_c
• Validate scaling law κ_c·Γ(N) = 2.539·N^0.9327

1.2 CHEMICAL PRINCIPLE:
Belousov-Zhabotinsky (BZ) reaction is an oscillating
chemical reaction that shows periodic color changes
between red and blue due to redox reactions.

Chemical Oscillators for N=30:
• 10 BZ reactors (one for each prime ≤ 30)
• Different oscillation periods: T(p) = 10s × ln(p)/ln(2)
• Goldbach connections through shared chemical mediators

1.3 EXPECTED VISUAL RESULTS:
Low κ (Weak coupling):
• Each dish oscillates independently
• Random color patterns

Critical κ (κ_c ≈ 2-5):
• Goldbach pairs synchronize: 7-23, 11-19, 13-17
• Paired dishes change color simultaneously

High κ (Strong coupling):
• All 10 dishes synchronize
• Unified color changes"""
        
        ax.text(0.05, 0.95, overview_text, ha='left', va='top', 
                fontsize=9.5, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # SECTION 2: MATERIALS & PREPARATION
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        materials_text = """2. MATERIALS & PREPARATION

2.1 CHEMICAL SHOPPING LIST:
┌──────────────────────────────┬─────────┬─────────┐
│ Chemical                     │ Amount  │ Cost(€) │
├──────────────────────────────┼─────────┼─────────┤
│ Sodium Bromate (NaBrO₃)      │ 50g     │ 15.00   │
│ Malonic Acid (CH₂(COOH)₂)    │ 100g    │ 10.00   │
│ Sulfuric Acid (H₂SO₄) 0.5M   │ 1L      │ 5.00    │
│ Ferroin Indicator            │ 100ml   │ 8.00    │
│ Cerium(III) Sulfate          │ 25g     │ 12.00   │
│ Bromoacetic Acid             │ 25g     │ 15.00   │
│ Potassium Bromide (KBr)      │ 50g     │ 8.00    │
│ Potassium Iodide (KI)        │ 50g     │ 8.00    │
│ Iron(II) Sulfate (FeSO₄)     │ 50g     │ 10.00   │
├──────────────────────────────┼─────────┼─────────┤
│ SUBTOTAL (Chemicals)         │         │ 91.00   │
├──────────────────────────────┼─────────┼─────────┤
│ 10 Petri Dishes (100mm)      │ 10      │ 5.00    │
│ Filter Paper Strips          │ 1 pack  │ 3.00    │
│ Graduated Cylinders          │ Set     │ 15.00   │
│ Pipettes & Droppers          │ Set     │ 10.00   │
│ Lab Coat, Gloves, Goggles    │ Set     │ 20.00   │
├──────────────────────────────┼─────────┼─────────┤
│ TOTAL ESTIMATED COST         │         │ 144.00€ │
└──────────────────────────────┴─────────┴─────────┘

2.2 SOLUTION PREPARATION:
Stock Solution A (Oxidizer):
• Dissolve 15g NaBrO₃ in 250ml distilled water
• Add 10ml concentrated H₂SO₄ to 240ml water
• Mix both solutions carefully

Stock Solution B (Reductant):
• Dissolve 8g malonic acid in 250ml distilled water

Stock Solution C (Indicator):
• Use ready-made 0.025M ferroin solution
• Or prepare: 1.5g phenanthroline + 0.7g FeSO₄ in 100ml water

2.3 PERIOD MODIFIERS:
To create different oscillation periods for primes:
Fast Oscillators (Small primes):
• Add Ce³⁺/Ce⁴⁺ catalyst (0.1M solution)

Slow Oscillators (Large primes):
• Add bromoacetic acid inhibitor (0.05M solution)

Target periods for N=30:
Prime  Period  Color Code
  2     10.0s  Bright Red
  3     15.8s  Orange
  5     23.1s  Yellow
  7     28.1s  Green
  11    36.9s  Blue
  13    41.2s  Purple
  17    48.6s  Pink
  19    51.3s  Brown
  23    56.8s  Gray
  29    64.7s  Black"""
        
        ax.text(0.05, 0.95, materials_text, ha='left', va='top', 
                fontsize=8, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # SECTION 3: EXPERIMENTAL PROCEDURE
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        procedure_text = """3. EXPERIMENTAL PROCEDURE

3.1 DAY 1: CHEMICAL PREPARATION (2-3 hours)

Step 1: Prepare All Solutions
1. Prepare Stock Solution A, B, C as described
2. Prepare mediator solutions:
   • Bromide mediator: 0.1M KBr solution
   • Iodine mediator: 0.1M KI solution
   • Iron mediator: 0.1M FeSO₄ solution
3. Prepare period modifiers:
   • Catalyst: 0.1M Ce³⁺ solution
   • Inhibitor: 0.05M bromoacetic acid

Step 2: Label Petri Dishes
Label 10 dishes with prime numbers:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29
Add color dots according to color code.

Step 3: Prepare Individual Oscillators
For each prime p:
1. Add 20ml Solution A to dish
2. Add 10ml Solution B
3. Add 2ml Solution C (ferroin)
4. Add period modifier:
   • Small primes: Add 0.5ml catalyst
   • Large primes: Add 0.5ml inhibitor

3.2 DAY 2: EXPERIMENTAL SETUP (1-2 hours)

Step 1: Arrange Dishes
Arrange in circular pattern with 30cm diameter.
Place on white background for better contrast.

Step 2: Set Up Recording
• Camera on tripod directly above
• White lighting from sides
• Record at 30 fps minimum
• Include timestamp in video

Step 3: Initial Observation
Observe without connections (κ=0):
• Each dish should oscillate independently
• Periods should differ according to primes
• Record baseline oscillations for 10 minutes

3.3 GOLDBACH CONNECTIONS

Connection Method: Filter Paper Bridges
1. Cut filter paper into 1cm × 5cm strips
2. Soak each strip in specific mediator:
   • 7-23 connection: Bromide mediator
   • 11-19 connection: Iodine mediator
   • 13-17 connection: Iron mediator
3. Place soaked strips between dishes
   One end in dish 7, other end in dish 23, etc.

3.4 κ CONTROL METHODS

Coupling Strength κ is controlled by:
1. MEDIATOR CONCENTRATION:
   • Low κ: Dilute mediator (0.01M)
   • Medium κ: Standard (0.1M)
   • High κ: Concentrated (0.5M)

2. CONNECTION AREA:
   • Thin strips: Weak coupling
   • Wide strips: Strong coupling

3. DISTANCE BETWEEN DISHES:
   • Far apart: Weak coupling
   • Close together: Strong coupling"""
        
        ax.text(0.05, 0.95, procedure_text, ha='left', va='top', 
                fontsize=8, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # SECTION 4: MEASUREMENT & ANALYSIS
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        measurement_text = """4. MEASUREMENT & ANALYSIS

4.1 VIDEO ANALYSIS SETUP

Required Software:
• Python with OpenCV: For automated analysis
• Tracker Video Analysis: Free physics software
• ImageJ: For manual frame-by-frame analysis

Analysis Procedure:
1. Extract frames from video (every 0.5 seconds)
2. Convert to HSV color space
3. Measure red/blue intensity for each dish
4. Create time series for each oscillator

4.2 SYNCHRONIZATION DETECTION

Phase Calculation:
For each oscillator i at time t:
• Phase θ_i(t) = 2π × (t - t_red) / T_i
Where t_red is time of last red peak
T_i is oscillation period

Synchronization Parameter r:
r(t) = |(1/10) Σ exp(iθ_j(t))|
• r ≈ 0.3: No synchronization
• r ≈ 0.7: Critical synchronization
• r ≈ 0.9: Full synchronization

4.3 FINDING κ_c EXPERIMENTALLY

Procedure:
1. Start with κ = 0 (no connections)
2. Gradually increase κ:
   • Step 1: Weak connections (thin strips, dilute)
   • Step 2: Medium connections
   • Step 3: Strong connections (wide strips, concentrated)
3. For each κ value:
   • Record video for 5 minutes
   • Calculate average r
   • Note visual synchronization

4.4 EXPECTED RESULTS FOR N=30:

κ Range        Expected r    Visual Observation
────────────────────────────────────────────────
κ < 1.0        r < 0.3      Chaotic, independent
κ = 2.0-3.0    r > 0.7      Goldbach pairs sync
κ > 4.0        r > 0.9      All dishes sync

Theoretical scaling verification:
κ_c(exp) × Γ(30) should be close to 77.2
Acceptable error: ±30% for first experiment

4.5 DATA RECORDING TEMPLATE:

┌──────┬─────────┬─────────┬──────────────┬────────────┐
│ Test │ κ value │ Mediator│ r measured   │ Sync State │
├──────┼─────────┼─────────┼──────────────┼────────────┤
│ 1    │ 0.0     │ None    │ 0.25 ± 0.05  │ No         │
│ 2    │ 1.5     │ Dilute  │ 0.45 ± 0.07  │ No         │
│ 3    │ 2.5     │ Normal  │ 0.75 ± 0.06  │ Yes (pairs)│
│ 4    │ 3.5     │ Conc.   │ 0.85 ± 0.04  │ Yes (all)  │
│ 5    │ 5.0     │ Conc.+  │ 0.92 ± 0.03  │ Yes (all)  │
└──────┴─────────┴─────────┴──────────────┴────────────┘"""
        
        ax.text(0.05, 0.95, measurement_text, ha='left', va='top', 
                fontsize=8, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # SECTION 5: SAFETY & TROUBLESHOOTING
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        safety_text = """5. SAFETY & TROUBLESHOOTING

5.1 SAFETY PROTOCOL (MANDATORY)

Personal Protective Equipment (PPE):
• Lab coat (mandatory)
• Safety goggles (mandatory)
• Nitrile gloves (mandatory)
• Closed-toe shoes

Chemical Handling:
• Work in well-ventilated area
• No eating/drinking in lab
• Wash hands after handling chemicals
• Have eyewash station accessible

Acid Safety:
• Always add acid to water, NOT water to acid
• Use dilute sulfuric acid (0.5M) when possible
• Neutralize spills with baking soda

Waste Disposal:
• Collect all chemical waste separately
• Neutralize acidic waste before disposal
• Follow local regulations

5.2 TROUBLESHOOTING GUIDE

Problem: No oscillations
Solution:
• Check sulfuric acid concentration (needs 0.5M)
• Ensure fresh chemicals (malonic acid degrades)
• Wait 5-10 minutes for oscillations to start

Problem: Oscillations too fast/slow
Solution:
• Adjust catalyst/inhibitor amounts
• Temperature affects rate (ideal: 20-25°C)
• Check concentration of all solutions

Problem: Colors not visible
Solution:
• Increase ferroin concentration
• Use white background
• Improve lighting

Problem: No synchronization
Solution:
• Increase mediator concentration
• Use wider filter paper strips
• Move dishes closer together
• Ensure proper Goldbach connections

5.3 COMMON MISTAKES TO AVOID

1. Using wrong mediator for Goldbach pairs
2. Incorrect prime-to-dish labeling
3. Insufficient video recording time
4. Not allowing system to stabilize
5. Changing multiple variables at once"""
        
        ax.text(0.05, 0.95, safety_text, ha='left', va='top', 
                fontsize=8.5, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # SECTION 6: DATA PUBLICATION
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        publication_text = """6. DATA PUBLICATION

6.1 DOCUMENTING RESULTS

Essential Materials to Collect:
1. High-quality photos:
   • Setup before experiment
   • During oscillations
   • Synchronized state
2. Video recordings:
   • Raw footage (full experiment)
   • Highlight clips (synchronization moments)
   • Time-lapse (entire experiment)
3. Data files:
   • Raw intensity measurements
   • Calculated r values
   • Phase plots
4. Lab notebook entries:
   • Date, time, conditions
   • Observations
   • Problems encountered

6.2 SCIENTIFIC PAPER OUTLINE

Title: Experimental Verification of Goldbach Bridge Theorem
       Using Chemical Oscillators

Abstract (150 words):
• State the theorem
• Describe chemical implementation
• Report κ_c found
• Confirm scaling law

Introduction:
• Goldbach Bridge Theorem
• Previous work
• Chemical oscillator background

Methods:
• Detailed experimental setup
• Chemical preparations
• Measurement techniques

Results:
• κ vs r curves
• Video analysis results
• Comparison with theory

Discussion:
• Implications for arithmetic physics
• Limitations
• Future work

Conclusion:
• Summary of findings
• Confirmation of theorem

References:
• Cite original theorem paper
• Cite BZ reaction papers

Supplementary Materials:
• Video files
• Raw data
• Detailed protocols

6.3 PRESENTATION TIPS

Conference Presentation (15 minutes):
• 2 min: Introduction & problem
• 3 min: Theoretical background
• 5 min: Experimental method
• 3 min: Results
• 2 min: Conclusion

Poster Presentation:
• Left: Theory & background
• Center: Experimental setup
• Right: Results & conclusion
• Bottom: References & acknowledgments

Social Media Sharing:
• YouTube: Full experiment video
• Twitter: Key findings with #GoldbachBridge #Chemistry
• ResearchGate: Full paper
• GitHub: Analysis code"""
        
        ax.text(0.05, 0.95, publication_text, ha='left', va='top', 
                fontsize=8.5, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # BULGARIAN VERSION: ХИМИЧЕН ЕКСПЕРИМЕНТ
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        bg_chemical_text = """ХИМИЧЕН ЕКСПЕРИМЕНТ
ЗА МОСТА НА ГОЛДБАХ
(БЪЛГАРСКА ВЕРСИЯ)

1. ЦЕЛ НА ЕКСПЕРИМЕНТА:
Експериментално доказване на теоремата за моста на Голдбах
чрез химични осцилатори (реакция на Белоусов-Жаботински).

2. НЕОБХОДИМИ МАТЕРИАЛИ:
┌─────────────────────────────┬───────────┬─────────┐
│ Химикал                     │ Количество│ Цена(лв)│
├─────────────────────────────┼───────────┼─────────┤
│ Натриев бромат (NaBrO₃)     │ 50g       │ 30.00   │
│ Малонова киселина           │ 100g      │ 20.00   │
│ Сярна киселина (0.5M)       │ 1L        │ 10.00   │
│ Фероин индикатор            │ 100ml     │ 16.00   │
│ Церий(III) сулфат           │ 25g       │ 24.00   │
│ Бромооцетна киселина        │ 25g       │ 30.00   │
│ Калиев бромид (KBr)         │ 50g       │ 16.00   │
│ Калиев йодид (KI)           │ 50g       │ 16.00   │
│ Желязо(II) сулфат (FeSO₄)   │ 50g       │ 20.00   │
├─────────────────────────────┼───────────┼─────────┤
│ ОБЩО ХИМИКАЛИ               │           │ 182.00  │
├─────────────────────────────┼───────────┼─────────┤
│ 10 чашки Петри (100mm)      │ 10        │ 10.00   │
│ Филтър хартиени ленти       │ 1 опак.   │ 6.00    │
│ Мензури и цилиндри          │ Комплект  │ 30.00   │
│ Пипетки и капкомери         │ Комплект  │ 20.00   │
│ Лабораторно облекло         │ Комплект  │ 40.00   │
├─────────────────────────────┼───────────┼─────────┤
│ ОБЩА ПРИБЛИЗИТЕЛНА ЦЕНА     │           │ 278.00лв│
└─────────────────────────────┴───────────┴─────────┘

3. ПРОСТИ ЧИСЛА ЗА N=30:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29

Goldbach двойки:
7 + 23 = 30
11 + 19 = 30
13 + 17 = 30

4. ПЕРИОДИ НА ОСЦИЛАЦИИ:
T(p) = 10s × ln(p)/ln(2)

Пример:
p=2 → T=10.0s (ярко червено)
p=3 → T=15.8s (оранжево)
p=5 → T=23.1s (жълто)
p=29 → T=64.7s (черно)

5. GOLDBACH ВРЪЗКИ ЧРЕЗ МЕДИАТОРИ:
• 7-23: Бромидни йони (Br⁻/BrO₂⁻)
• 11-19: Йод (I⁻/I₂)
• 13-17: Желязо (Fe²⁺/Fe³⁺)

6. ОЧАКВАНИ РЕЗУЛТАТИ:
• При слабо свързване: Всички чашки осцилират независимо
• При критично свързване: Goldbach двойки се синхронизират
• При силно свързване: Всички 10 чашки синхронизирани"""
        
        ax.text(0.05, 0.95, bg_chemical_text, ha='left', va='top', 
                fontsize=8, family='monospace')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # ============================================
        # CLOSING PAGE
        # ============================================
        fig = plt.figure(figsize=(11, 8.5))
        ax = fig.add_subplot(111)
        ax.axis('off')
        
        closing_text = """EXPERIMENT COMPLETE GUIDE
NARЪЧНИК ЗА ЕКСПЕРИМЕНТА

This PDF contains all information needed to conduct
the chemical experiment for Goldbach Bridge Theorem
verification. Follow the step-by-step instructions
carefully for successful results.

Този PDF файл съдържа цялата необходима информация
за провеждане на химичния експеримент за проверка
на теоремата за моста на Голдбах. Следвайте
стъпка-по-стъпка инструкциите внимателно за
успешни резултати.

KEY POINTS / КЛЮЧОВИ ТОЧКИ:
• Safety first! Always use PPE / Безопасност преди всичко!
• Document everything / Документирайте всичко
• Be patient - chemical reactions take time / Бъдете търпеливи
• Share your results / Споделете резултатите си

GOOD LUCK! / УСПЕХ!

Generated: """ + datetime.now().strftime('%Y-%m-%d %H:%M')
        
        ax.text(0.5, 0.6, closing_text, ha='center', va='center', fontsize=10)
        ax.text(0.5, 0.3, "SCIENTIFIC DISCOVERY AWAITS!\nНАУЧНО ОТКРИТИЕ ОЧАКВА!", 
                ha='center', va='center', fontsize=14, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='gold', alpha=0.5))
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    print(f"\n✅ CHEMICAL EXPERIMENT GUIDE created: {pdf_filename}")
    print(f"   Pages: 10 detailed pages")
    print(f"   Languages: English + Bulgarian section")
    print(f"   Estimated cost: ~144€ / 278лв")
    print(f"   Time required: 2-3 days")
    print(f"\n📘 Open the PDF for complete chemical experiment instructions!")

# ============================================
# RUN THE CODE
# ============================================
if __name__ == "__main__":
    print("🧪 GENERATING CHEMICAL EXPERIMENT GUIDE")
    print("="*60)
    print("Creating detailed PDF for BZ reaction experiment")
    print("Includes:")
    print("• Complete chemical shopping list")
    print("• Step-by-step preparation guide")
    print("• Safety protocols")
    print("• Data analysis methods")
    print("• Bulgarian version included")
    print("="*60)
    
    try:
        create_chemical_experiment_pdf()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Install required library: pip install matplotlib")

# ============================================
# BONUS: SIMPLE VERSION FOR SCHOOLS
# ============================================
def create_simple_chemical_guide():
    """Simple version for school experiments."""
    
    print("\n" + "="*60)
    print("🎓 SIMPLE SCHOOL VERSION (Low Cost)")
    print("="*60)
    
    simple_guide = """
    SIMPLE CHEMICAL EXPERIMENT FOR SCHOOLS
    (Reduced Cost Version)
    
    MINIMAL MATERIALS (~50€):
    • Sodium bromate: 25g (15€)
    • Malonic acid: 50g (5€)
    • Sulfuric acid (battery acid): 100ml (2€)
    • Iron(II) sulfate: 25g (5€)
    • Phenolphthalein indicator: 10ml (3€)
    • 5 Petri dishes: 5€
    • Basic lab equipment: 15€
    
    SIMPLE PROCEDURE:
    1. Prepare 5 oscillators (primes: 2,3,5,7,11)
    2. Use only iron-based connections
    3. Observe basic synchronization
    
    EXPECTED RESULTS:
    • Can still demonstrate Goldbach synchronization
    • Simpler analysis
    • Safe for classroom use
    """
    
    print(simple_guide)

# Uncomment to also get simple version
# create_simple_chemical_guide()