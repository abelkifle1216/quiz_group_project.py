
 A,4km/s 
 B,7km/s 
 C,16km/s 
 D,11.2km/s"""
Q2="""Which wave is used in TV remote control?
 A,Infrared 
 B,Radio wave 
 C, Gamma rays 
 D,X-rays"""
Q3="""work done is zero when:
 A,Time is zero 
 B,Mass is zero 
 C,Forceis applies 
 D,Displacement is zero"""
Q4="""The focal length of a concave lens is always:
 A,Negative 
 B,Infinite 
 C,Positive 
 D,Zero"""
Q5="""Which of the following has the highest speed in vaccum?
 A,Light 
 B,Sound cccc
 C,Radio wave 
 D,X-rays"""
Q6=""" The LCM of 18 and 24 is
 A,48 
 B,72 
 C,54 
 D,46"""
Q7=""" The interior angle of aregular pentagon is :
 A,180 
 B,90 
 C,108 
 D,135"""
Q8="""solve:x**2 - 9 = 0
 A,6 
 B,4 or-4 
 C,3 or-3 
 D,9"""
Q9=""" Atrain travels 120km in 2hours.Its average speed is: 
 A,40km/h 
 B,60km/h 
 C,20km/h 
 D,90km/h"""
Q10=""" If 2**x = 32,then x=?
 A,5 
 B,6 
 C,3 
 D,4"""
Q11=""" Which element has the electronic configuration 2,8,1?
 A,Magnesium 
 B,Lithium 
 C,Sodium 
 D,Calcium""" 
Q12=""" which element dose not form hydrogen bonds?
 A,F 
 B,Na 
 C,O 
 D,N"""
Q13=""" The PH of human blood is around:
 A,4.5 
 B,7.5 
 C,7.4 
 D,5.8"""
Q14=""" Which acid is called "oil of vitri1ol"?
 A,HNo3
 B,H2So4 
 C,H3PO4 
 D,HCl"""
Q15="""Which allotrope of carbon is hardest?
 A,Diamond 
 B,Graphite 
 C,Charcoal
 D,none""" 
Q16=""" Which blood cells fight infections?
 A,RBcs 
 B,WBcs 
 C,Platelets 
 D,Plasma""" 
Q17=""" The structural and functional unit of the nervous system is:
 A,Brain 
 B,Spinal cord 
 C,Axon 
 D,Neuron""" 
Q18=""" Which process produces gametes?
 A,Meiosis 
 B,Mitosis 
 C,Fusion 
 D,Fertilization"""
Q19="""Which vitamin deficiency causes night blindness?
 A,A 
 B,C 
 C,B 
 D,E"""
Q20=""" which part of the brain controls balance?
 A,Cerebrum 
 B,Medulla 
 C,Cerebellum 
 D,Hypothalamus"""
Q21=""" choose the synonym of happy:
 A,Sad 
 B,Gentle 
 C,Glad 
 D,Angry"""
Q22=""" choose the antonym of polite:
 A,Kind 
 B,week 
 C,Quite 
 D,Rude""" 
Q23="""she|-------to the market yesterday.
 A,Go 
 B,Went 
 C,Going 
 D,Goes"""
Q24="""If a student scored 72 marks out of 120. what is the percentage.
 A,35% 
 B,50% 
 C,62% 
 D,60%"""
Q25="""The ratio of girls to boys in a class is 3:5.If there are 24 girles,how many boys are there 
 A,40 
 B,45 
 C,35 
 D,30"""
questions = {
   Q1:'D',Q2:'A',Q3:'D',Q4:'A',Q5:'A',Q6:'B',Q7:'C',Q8:'C',Q9:'B',
   Q10:'A',Q11:'C',Q12:'B',Q13:'C',Q14:'B',Q15:'A',Q16:'B',Q17:'D',
   Q18:'A',Q19:'A',Q20:'C',Q21:'C',Q22:'D',Q23:'B',Q24:'D',Q25:'A' 
   }
print("Welcome to General Quiz")
name = input("Enter your full name")
print(f"Dear {name}, Welcome to Exam Hall")
print("please ready carefully the following instruction")
print("Instr.1:Don't forgot to write your full name")
print("Instr.2:cheating will nullify your total result")

mark = 0
List = ['A','B','C','D']
for item in questions:
   print(item)
   answer = input("choose the correct answer A/B/C/D:").lower()

   if answer == questions[item]:
         print(f"{answer} is correct answer,you got 2 points.")
         mark = mark+2
   else:
         print(f"{answer} is incorrect,{questions[item]} is the correct answer")
         mark = mark

   if mark >= 23:
      print(f"{mark}/25,Excellent")
   elif mark >= 20:
      print(f"{mark}/25,v.good")
   elif mark >= 18:
      print(f"{mark}/25,Good")
   elif mark >= 15:
      print(f"{mark}/25,satisfactory")
   else:
      print(f"{mark}/25,Faild")
# Instructions: Choose the best answer for each question

Q1=""" Which of the following is the basic structural and functional unit of life?
  a. Organ
  b. Tissue
  c. Cell
  d. Organ System"""

Q2=""" What process do plants use to convert light energy into chemical energy?
  a. Respiration
  b. Photosynthesis
  c. Transpiration
  d. Fermentation"""

Q3=""" Which biomolecule primarily stores genetic information in living organisms?
  a. Proteins
  b. Lipids
  c. Carbohydrates
  d. Nucleic Acids"""

Q4=""" What is the name for the process of cell division that creates gametes (sex cells)?
  a. Mitosis
  b. Meiosis
  c. Binary Fission
  d. Budding"""

Q5=""" What is the term for a group of organisms that can interbreed and produce fertile offspring?
  a. Population
  b. Community
  c. Ecosystem
  d. Species"""

Q6=""" What is the smallest particle of an element that retains the properties of that element?
  a. Molecule
  b. Compound
  c. Atom
  d. Ion"""

Q7=""" What type of chemical bond involves the sharing of electrons between atoms?
  a. Ionic Bond
  b. Covalent Bond
  c. Metallic Bond
  d. Hydrogen Bond"""

Q8=""" What is the chemical formula for water?
  a. CO2
  b. NaCl
  c. H2O
  d. O2"""

Q9=""" What is the process called when a substance changes directly from a solid to a gas?
  a. Melting
  b. Condensation
  c. Sublimation
  d. Evaporation"""

Q10=""" What is the measure of the acidity or alkalinity of a solution called?
  a. Volume
  b. Density
  c. pH
  d. Temperature"""

# Physics (Questions 11-15)

Q11=""" What is the SI unit of force?
  a. Watt
  b. Joule
  c. Newton
  d. Pascal"""

Q12=""" What is the phenomenon called when a wave bends as it passes from one medium to another?
  a. Reflection
  b. Refraction
  c. Diffraction
  d. Interference"""

Q13=""" What type of energy is associated with the motion of objects?
  a. Potential Energy
  b. Kinetic Energy
  c. Chemical Energy
  d. Nuclear Energy"""

Q14=""" What is the name for the flow of electric charge?
  a. Voltage
  b. Resistance
  c. Current
  d. Power"""

Q15=""" What is the speed of light in a vacuum?
  a. 3.0 x 10^8 m/s
  b. 1.0 x 10^8 m/s
  c. 3.0 x 10^5 m/s
  d. 3.0 x 10^10 m/s"""

# Math (Questions 16-20)

Q16=""" What is the value of pi (π) to two decimal places?
  a. 3.16
  b. 3.14
  c. 3.20
  d. 3.00"""

Q17=""" What is the area of a circle with a radius of 5 units? (Use π = 3.14)
  a. 25 units squared
  b. 15.7 units squared
  c. 78.5 units squared

  d. 31.4 units squared"""

Q18=""" What is the square root of 144?
  a. 10
  b. 12
  c. 14
  d. 16"""

Q19=""" Solve for x: 2x + 5 = 11
  a. 2
  b. 3
  c. 4
  d. 5"""

Q20=""" What is 6! (6 factorial) equal to?
  a. 15
  b. 25
  c. 720
  d. 625"""

# English (Questions 21-25)

Q21=""" Which of the following is a synonym for "happy"?
  a. Sad
  b. Angry
  c. Joyful
  d. Tired"""

Q22=""" Which of the following is a noun?
  a. Run
  b. Tree
  c. Quickly
  d. Beautiful"""

Q23=""" Which sentence is grammatically correct?
  a. I is going to the store.
  b. I are going to the store.
  c. I am going to the store.
  d. Me going to the store."""

Q24=""" What is the plural form of "child"?
  a. Childs
  b. Childes
  c. Children
  d. Child"""

Q25=""" Which literary device involves using an object or idea to represent something else?
  a. Metaphor
  b. Simile
  c. Symbolism
  d. Personification"""

questions = {Q1:'c', Q2:'b', Q3:'d', Q4:'b',
             Q5:'d', Q6:'c', Q7:'b', Q8:'c', Q9:'c', Q10:'c',
             Q11:'c', Q12:'b', Q13:'b', Q14:'c', Q15:'a',
             Q16:'b', Q17:'c', Q18:'b', Q19:'b', Q20:'c',
             Q21:'c', Q22:'b', Q23:'c', Q24:'c', Q25:'c'
            }

name = input("enter your full name: ")  # Added a closing parenthesis
print(f"dear {name}")  # Added f-string
print("please read the following instructions:")  # Corrected spelling
print("instraction1: do not forget to write your full name")  # Corrected spelling
print("instraction 2: cheating with nullify your total result ")  # Corrected spelling

mark = 0
# Corrected logic with questions and added input function
for question in questions:
    print(question)
    answer = input("Enter your answer (a, b, c, or d): ").lower()  # take the input

    if answer == questions[question]:  # comparing
        mark = mark + 1  # addition
        print("Correct!")
    else:
        print("Incorrect!")

# Calculate the percentage
percentage = (mark / len(questions)) * 100

# Determine the grade category
if percentage >= 18:
    grade = "Excellent"
elif percentage >= 15:
    grade = "Very Good"
elif percentage >= 12:
    grade = "Good"
elif percentage >= 10:
    grade = "Satisfactory"
else:
    grade = "Failed"

# printing the final mark and grade
print(f"{name}, your final mark is {mark} out of {len(questions)}.")
print(f"Percentage: {percentage:.2f}%")  

# General Quiz Program
questions = """Q1. Which organelle produces ATP during respiration?
 A. Nucleus
 B. Mitochondrion
 C. Golgi apparatus
 D. Lysosome

Q2. In DNA, adenine pairs with?
 A. Guanine
 B. Thymine
 C. Cytosine
 D. Uracil

Q3. Light reactions of photosynthesis occur in?
 A. Stroma
 B. Thylakoid membranes
 C. Cytosol
 D. Matrix
 
Q4. Natural selection means?
 A. Individuals change traits by need
 B. Best camouflage always survives
 C. Heritable traits improving fitness spread
 D. Evolution has a goal

Q5. What carries oxygen in human blood?
 A. Platelets
 B. Hemoglobin in RBC
 C. Plasma proteins
 D. WBC

Q6. Derivative of x^3 is?
 A. x^2
 B. 3x^2
 C. 3x
 D. 2x

Q7. Solve: 2x + 5 = 17
 A. 4
 B. 5
 C. 6
 D. 7

Q8. Area of circle radius 3?
 A. 6π
 B. 9π
 C. 3π
 D. 18

Q9. Probability of 6 on a die?
 A. 1/3
 B. 1/6
 C. 1/5
 D. 1/12

Q10. 2^3 * 2^4 = ?
 A. 16
 B. 64
 C. 128
 D. 32

Q11. Newton's second law?
 A. E=mc^2
 B. F=ma
 C. p=mv^2
 D. V=IR

Q12. Unit of resistance?
 A. Volt
 B. Ohm
 C. Watt
 D. Ampere

Q13. Speed of light (vacuum)?
 A. 3*10^6
 B. 3*10^8
 C. 3*10^10
 D. 3*10^5

Q14. In an isolated system, mechanical energy?
 A. KE always increases
 B. PE always decreases
 C. Total stays constant
 D. Energy is created

Q15. Work done (F parallel d)?
 A. W=F/d
 B. W=Fd
 C. W=Fd^2
 D. W=F/v

Q16. pH of neutral solution (25°C)?
 A. 5
 B. 6
 C. 7
 D. 8

Q17. Avogadro's number?
 A. 6.022*10^20
 B. 6.022*10^23
 C. 3*10^8
 D. 1.38*10^-23

Q18. Bond by sharing electrons?
 A. Ionic
 B. Metallic
 C. Covalent
 D. Hydrogen

Q19. Ideal gas law?
 A. PV=nRT
 B. P=pgh
 C. Q=mcΔT
 D. E=hv

Q20. Oxidation means?
 A. Gain e-
 B. Loss e-
 C. Gain proton
 D. Loss

Q21. What is the capital of France?
 A. London
 B. Berlin
 C. Paris
 D. Madrid

Q22. Who wrote Romeo and Juliet?
 A. Charles Dickens
 B. William Shakespeare
 C. Mark Twain
 D. Jane Austen

Q23. What is the opposite of "hot"?
 A. Cold
 B. Warm
 C. Heat
 D. Cool

Q24. How many days are there in a week?
 A. Five
 B. Six
 C. Seven
 D. Eight

Q25. What is the past tense of "go"?
 A. Goed
 B. Went
 C. Gone
 D. Going
"""

answers = {
    1: "B", 2: "B", 3: "B", 4: "C", 5: "B",
    6: "B", 7: "C", 8: "B", 9: "B", 10: "C",
    11: "B", 12: "B", 13: "B", 14: "C", 15: "B",
    16: "C", 17: "B", 18: "C", 19: "A", 20: "B",
    21: "C", 22: "B", 23: "A", 24: "C", 25: "B"
}

print("Welcome to the General Quiz")
name = input("Enter your full name: ")
print(f"\nDear {name}, let's start!\n")

question = [question.strip() for question in questions.strip().split("\n\n")]

mark = 0

for item, question in enumerate(question, start=1):
    print(f"Q{item}. {question}")
    
    while True:
        answer = input("Choose the correct answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid choice! Please enter only A, B, C, or D.")

    if answer == answers[item]:
        print(f" Correct! You got 1 points.\n")
        mark += 1
    else:
        print(f"Incorrect. The correct answer was {answers[item]}.\n")

print(f"Quiz Completed!\n{name}, your total score is {mark} / {len(answers)*1}")

if mark >=20:
    print(f"{mark}/25,Excellent")
elif mark >= 15:
       print(f"{mark}/25,V.good")
elif mark >= 10:
       print(f"{mark}/25,Gooood!")
else:
     mark <= 5
     print(f"{mark}/25,Failed")
