#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re


# In[10]:


cdc_thesaurus = {
    "abdomen": ["stomach", "belly", "tummy"],
    "ability": ["skill"],
    "abolish": ["end", "do away with", "get rid of"],
    "abrasion": ["cut", "scratch", "scrape"],
    "absenteeism": ["missing work or school"],
    "absorption": ["take in", "soak up"],
    "accelerate": ["hurry", "speed up", "make worse", "make more severe"],
    "accessible": ["available", "on hand", "understandable", "usable"],
    "accommodate": ["house", "let stay with", "give shelter", "adjust", "adapt"],
    "accompany": ["go with", "take with (medicine)"],
    "accomplish": ["do", "finish"],
    "accumulate": ["add up", "gather", "collect"],
    "accurate": ["true", "right", "correct"],
    "active immunity": ["being able to fight off a specific disease once you have had that disease"],
    "acute": ["sudden start", "short term", "quick"],
    "additional": ["extra", "added", "more"],
    "adhere": ["stick", "follow"],
    "adjacent": ["beside", "next to", "near", "touching"],
    "adverse event": ["something bad that happens", "bad reaction"],
    "advocate": ["fight for", "support", "support person"],
    "aerobic": ["needs oxygen"],
    "allergen": ["something like pollen that causes the body to react by sneezing or forming a rash"],
    "allergic": ["the body’s reaction to something, like pollen, resulting in sneezing, sniffling, a rash, etc."],
    "allergy": ["reaction to certain things such as food or cloth or pollen", "itch", "rash", "hives", "breathing problem"],
    "alleviate": ["lessen", "ease", "soften", "improve", "make better"],
    "alopecia": ["hair loss", "balding"],
    "alteration": ["change", "shift", "adjustment"],
    "ambulatory": ["can walk", "mobile", "able to move about", "walking"],
    "ameliorate": ["make better", "improve", "lessen", "ease"],
    "anaerobic": ["needs lack of oxygen"],
    "anemia": ["tired", "low iron", "a low blood count that can make you tired and short of breath"],
    "annual": ["yearly", "every year", "once every year", "once a year", "each year"],
    "antibiotic": ["drug", "medicine", "drug that fights bacteria", "infection-fighting medicine"],
    "antibody": ["your body’s way to fight off infections", "infection-fighting cells"],
    "antigen": ["germ", "bacteria", "virus", "poison", "something in your body that your body tries to fight off"],
    "anxiety": ["fear", "worry"],
    "applicant": ["your name", "name of the person", "person who is applying"],
    "appropriate": ["proper", "right", "take over", "a good fit"],
    "asymptomatic": ["someone who is sick but does not feel or look sick"],
    "asthma": ["disease of the lungs", "breathing disease", "lung disease where you have trouble breathing"],
    "autoimmune disease": ["disease that makes your body attack itself"],
    "available": ["on hand", "at hand", "ready", "near-by"],
    "benefit": ["help", "aid"],
    "bacteria": ["germs"],
    "biannual": ["every two years", "twice a year", "two times every year"],
    "bioterrorism": ["spreading virus or disease to cause fear or hurt"],
    "BMI": ["a measure of body fat based on height and weight"],
    "blister": ["small bump on your skin"],
    "blood pressure": ["how hard your blood pushes on the walls of your arteries"],
    "body mass index": ["BMI", "measurement of body fat based on height and weight"],
    "carcinogen": ["cancer-causing substance"],
    "cardiologist": ["heart doctor"],
    "cardiology": ["medical department that treats heart problems"],
    "cavities": ["tooth decay"],
    "cerebral hemorrhage": ["stroke"],
    "cerebrovascular disease": ["stroke"],
    "cervix": ["lower part of the uterus"],
    "cessation": ["stopping", "quitting", "ending"],
    "characteristic": ["mark", "trait", "feature"],
    "chronic": ["long term", "long-lasting"],
    "chronic disease": ["disease that lasts for years"],
    "chronic health condition": ["constant health problem, something that affects your health for a long period of time"],
    "chronic obstructive pulmonary disease": ["lung disease, such as asthma or emphysema"],
    "clade": ["a group of animals that can all get the same disease"],
    "clinical": ["medical", "work or studies in a medical setting that involve patients"],
    "clinical examination": ["check-up", "doctor's appointment"],
    "cognitive": ["thinking", "mental ability"],
    "coagulate": ["clot", "set", "clump together"],
    "collaborate": ["work together", "team up", "help each other"],
    "communicable": ["catching", "can be passed to other people", "can make other people sick"],
    "communicate": ["tell", "say", "call", "write", "talk to"],
    "community immunity": ["the protection people who aren’t vaccinated get when most other people in their community are vaccinated"],
    "compensate": ["pay", "reward", "make up for"],
    "comprehensive": ["complete", "covers everything important", "thorough"],
    "compulsion": ["urge", "desire", "need", "want"],
    "congenital": ["born with", "inborn"],
    "contagious": ["infectious", "something that can spread disease"],
    "contact": ["get in touch with", "call", "talk to"],
    "contingency": ["possible event", "potential occurrence"],
    "convalesce": ["recover", "get better"],
    "cough etiquette": ["how to cough or sneeze properly"],
    "cystitis": ["infection causing pain when you urinate"],
    "deceased": ["dead"],
    "decompose": ["decay", "rot", "break down"],
    "decontaminate": ["clean", "kill germs", "disinfect", "sterilize"],
    "dehydration": ["water loss", "not enough water in the body"],
    "deficiency": ["lack", "not enough"],
    "deficient": ["lacking", "not enough", "poor"],
    "degenerative": ["weaken", "worsen", "decline", "decay", "droop"],
    "delirium": ["confusion", "mental state that makes it hard to think clearly"],
    "dementia": ["memory loss that gets worse over time"],
    "dermatologist": ["skin doctor"],
    "disease": ["illness", "sickness"],
    "disinfect": ["clean", "sterilize", "sanitize"],
    "disseminate": ["spread", "distribute", "send out"],
    "distinguish": ["tell apart", "set apart"],
    "donate": ["give", "offer", "present"],
    "dose": ["amount of medicine or drug"],
    "drowsy": ["sleepy"],
    "dyspepsia": ["indigestion", "heartburn"],
    "dyspnea": ["shortness of breath", "difficulty breathing"],
    "epidemic": ["widespread disease"],
    "epidemiology": ["disease study"],
    "evidence-based": ["proven through research", "scientifically supported"],
    "exacerbate": ["worsen", "make worse"],
    "exhaustion": ["tiredness", "fatigue"],
    "expectant": ["waiting for", "anticipating"],
    "exposure": ["contact with", "being around", "coming in contact with"],
    "extraneous": ["unnecessary", "not needed"],
    "facilitate": ["make easier", "help"],
    "factor": ["cause", "reason"],
    "fatigue": ["tiredness", "weakness"],
    "feasible": ["possible", "workable"],
    "febrile": ["feverish", "caused by a fever"],
    "flexible": ["able to bend", "adaptable", "stretchable"],
    "fluid": ["liquid", "drink", "water"],
    "folic acid": ["vitamin B9", "a vitamin important for health"],
    "fractionated": ["broken into parts", "divided"],
    "fungal": ["related to fungi", "mold-related"],
    "fungicide": ["substance that kills fungi"],
    "furthermore": ["also", "in addition", "besides"],
    "gastric": ["related to the stomach"],
    "gastrointestinal": ["digestive system", "stomach and intestines"],
    "general anesthesia": ["total unconsciousness caused by drugs"],
    "general practitioner": ["family doctor", "primary care physician"],
    "genetic": ["related to your genes", "inherited from your parents"],
    "genome": ["the set of genes in your body"],
    "geriatric": ["related to older adults"],
    "gland": ["an organ that produces something (like sweat, hormones)"],
    "glucose": ["sugar", "energy"],
    "granulocyte": ["type of white blood cell"],
    "hematology": ["study of blood"],
    "hematoma": ["blood clot", "bruise"],
    "hemorrhage": ["bleeding"],
    "hemodialysis": ["blood-cleaning treatment for kidney disease"],
    "hepatitis": ["liver disease", "inflammation of the liver"],
    "hereditary": ["genetic", "passed down from family"],
    "herpes": ["viral infection", "a type of virus that can cause cold sores"],
    "hormone": ["chemical that affects your body functions"],
    "hypertension": ["high blood pressure"],
    "hypotension": ["low blood pressure"],
    "immunization": ["vaccination", "getting a vaccine"],
    "immune system": ["body’s defense system against disease"],
    "infection": ["illness caused by bacteria or virus"],
    "inhaler": ["medicine to help with breathing"],
    "inflammatory": ["causing swelling or irritation"],
    "inflammation": ["swelling, redness, pain, or heat caused by infection or injury"],
    "inhalation": ["breathing in"],
    "incubation period": ["time between infection and when symptoms appear"],
    "insomnia": ["difficulty sleeping"],
    "intensity": ["strength", "how strong something is"],
    "intermittent": ["happens in stops and starts"],
    "intravenous": ["inside a vein"],
    "jaundice": ["yellowing of the skin or eyes"],
    "kidney": ["organ that filters blood"],
    "laryngitis": ["inflammation of the voice box"],
    "lesion": ["a wound, sore, or area of damage on the body"],
    "leukocyte": ["white blood cell"],
    "liquid": ["water or other fluid"],
    "liver": ["organ that processes nutrients and toxins"],
    "lobotomy": ["surgical removal of part of the brain (outdated)"],
    "long-term": ["for a long time"],
    "lupus": ["autoimmune disease that causes joint pain and swelling"],
    "malignant": ["cancerous", "harmful"],
    "mammogram": ["test to check the health of the breast"],
    "mastectomy": ["removal of the breast"],
    "medication": ["medicine", "drug"],
    "membrane": ["thin layer of tissue covering organs"],
    "metabolism": ["body’s process of turning food into energy"],
    "migraine": ["severe headache"],
    "mild": ["not severe", "gentle"],
    "molecule": ["smallest unit of a chemical compound"],
    "monitor": ["check", "watch closely"],
    "morbidity": ["sickness", "disease condition"],
    "mortality": ["death rate"],
    "mutation": ["change", "genetic variation"],
    "neurotransmitter": ["chemical in the brain that transmits signals"],
    "non-invasive": ["not requiring surgery or cuts into the skin"],
    "nutrient": ["substance needed for growth and health"],
    "obesity": ["extremely overweight"],
    "obstetrician": ["doctor for pregnancy and childbirth"],
    "oncologist": ["cancer doctor"],
    "osteoporosis": ["bone weakness disease"],
    "overdose": ["taking too much medicine or drug"],
    "pathogen": ["disease-causing microorganism"],
    "pediatrician": ["children’s doctor"],
    "pharmacist": ["person who dispenses medicine"],
    "pneumonia": ["lung infection"],
    "prophylactic": ["preventative, usually drugs or measures to prevent illness"],
    "psychiatrist": ["mental health doctor"],
    "radiologist": ["doctor who reads x-rays"],
    "respiratory": ["related to breathing or the lungs"],
    "rheumatologist": ["doctor who treats arthritis and joint issues"],
    "surgery": ["operation to treat or remove something from the body"],
    "symptom": ["sign of illness or disease"],
    "systolic": ["upper number in blood pressure readings"],
    "tachycardia": ["fast heart rate"],
    "treatment": ["care given to cure or alleviate disease"],
    "vaccination": ["getting a vaccine to prevent illness"],
    "virus": ["microorganism that causes disease"],
    "wound": ["injury to the body"]
}


# In[15]:


def simplify_sentence(sentence):
    # 1. **Use active voice**: Simplify passive voice constructions to active voice.
    sentence = re.sub(r"\bwas\b", "is", sentence)  # Simplify passive voice using "was"
    sentence = re.sub(r"\bwere\b", "are", sentence)  # Simplify passive voice using "were"
    sentence = re.sub(r"\bwere\b.*\bby\b", "", sentence)  # Remove "by" from passive constructions
    sentence = sentence.replace("is being", "is")  # Avoid passive with "being"
    
     # 2. **Avoid unnecessary jargon and complex terms**:
    sentence = sentence.replace("utilize", "use")
    sentence = sentence.replace("subsequent", "next")
    sentence = sentence.replace("in the event of", "if")
    sentence = sentence.replace("prior to", "before")
    sentence = sentence.replace("in order to", "to")
    sentence = sentence.replace("due to the fact that", "because")
    sentence = sentence.replace("ascertain", "find out")
    sentence = sentence.replace("ameliorate", "improve")
    sentence = sentence.replace("commence", "start")
    sentence = sentence.replace("terminate", "end")
    
    
    
 # 3. **Break long sentences into shorter, simpler ones**:
    # Split the sentence if it is too long by periods or commas, keeping meaning intact.
    sentence = re.sub(r"([a-zA-Z]),", r"\1. ", sentence)  # Split sentences on commas
    sentence = re.sub(r"\s*\.\s*", ".\n", sentence)  # Ensure sentences end with a period
    
     # 4. **Minimize use of formal or complex phrases**:
    sentence = sentence.replace("affect", "influence")
    sentence = sentence.replace("in the process of", "doing")
    sentence = sentence.replace("subsequent to", "after")
    sentence = sentence.replace("with respect to", "about")
    sentence = sentence.replace("owing to", "because of")
    
     # 5. **Remove redundancy**:
    sentence = re.sub(r"\b(really|truly)\s+\w+", "", sentence)  # Remove "really" or "truly" if redundant
    sentence = re.sub(r"\bactual\b\s+\w+", "", sentence)  # Remove "actual" when not necessary
    sentence = re.sub(r"\blevel of\b", "amount of", sentence)  # Simplify "level of"
    
    # 6. **Use simpler alternatives for common medical terms**:
    sentence = sentence.replace("cardiovascular disease", "heart disease")
    sentence = sentence.replace("hypertension", "high blood pressure")
    sentence = sentence.replace("pulmonary disease", "lung disease")
    sentence = sentence.replace("gastrointestinal problems", "stomach issues")
    sentence = sentence.replace("psychosomatic disorder", "mental health disorder")
    sentence = sentence.replace("epidemiology", "disease study")
    
    # 7. **Shorten long phrases**:
    sentence = sentence.replace("in the near future", "soon")
    sentence = sentence.replace("in light of the fact that", "because")
    sentence = sentence.replace("at this point in time", "now")
    sentence = sentence.replace("due to the fact that", "because")
    
        # 8. **Simplify numbers and measurements**:
    sentence = sentence.replace("milligrams", "mg")
    sentence = sentence.replace("milliliters", "mL")
    sentence = sentence.replace("centimeters", "cm")
    sentence = sentence.replace("kilograms", "kg")
    sentence = sentence.replace("liters", "L")
    
    
    return sentence



# In[16]:


example_sentences = [
    "The patient was diagnosed with hypertension and requires antihypertensive therapy.",
    "The treatment should be initiated in order to ameliorate the patient's condition."
]




# In[17]:


simplified_sentences = [simplify_sentence(sentence) for sentence in example_sentences]

for original, simplified in zip(example_sentences, simplified_sentences):
    print(f"Original: {original}")
    print(f"Simplified: {simplified}")
    print("-" * 40)


# In[ ]:





# In[ ]:



    


# In[ ]:




