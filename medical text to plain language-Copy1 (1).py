#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json
import re


# Load the medical dictionary
with open("medical_terms.json", "r", encoding="utf-8") as file:
    medical_dict = json.load(file)

def simplify_medical_text(text):
    words = text.split()
    simplified_words = [medical_dict.get(word.lower(), word) for word in words]
    return " ".join(simplified_words)


# In[11]:


combined_dict = {
    'a and/or b': ['a or b or both'],
    'accompany': ['go with', 'take with (medicine)'],
    'accomplish': ['do', 'finish'],
    'accorded': ['given'],
    'accordingly': ['so'],
    'accrue': ['add', 'gain'],
    'accurate': ['true', 'right', 'correct'],
    'additional': ['added', 'more', 'other'],
    'address': ['discuss'],
    'addressees': ['you'],
    'addressees are requested': ['please'],
    'adjacent to': ['next to'],
    'advantageous': ['helpful'],
    'adversely impact on': ['hurt', 'set back'],
    'advise': ['tell', 'warn', 'say'],
    'afford an opportunity': ['allow', 'let'],
    'aircraft': ['plane'],
    'allocate': ['divide'],
    'anticipate': ['expect'],
    'a number of': ['some'],
    'apparent': ['clear', 'plain'],
    'appreciable': ['many'],
    'appropriate': ['proper', 'right'],
    'approximate': ['about'],
    'arrive onboard': ['arrive'],
    'as a means of': ['to'],
    'ascertain': ['find out', 'learn'],
    'as prescribed by': ['in', 'under'],
    'assist': ['aid', 'help'],
    'assistance': ['aid', 'help'],
    'attain': ['meet'],
    'attempt': ['try'],
    'at the present time': ['now', 'at present'],
    'be advised': [''],
    'benefit': ['help'],
    'by means of': ['by', 'with'],
    'capability': ['ability'],
    'caveat': ['warning'],
    'close proximity': ['near'],
    'combat environment': ['combat'],
    'combined': ['joint'],
    'commence': ['begin', 'start'],
    'comply with': ['follow'],
    'component': ['part'],
    'comprise': ['form', 'include', 'make up'],
    'concerning': ['about', 'on'],
    'consequently': ['so'],
    'consolidate': ['combine', 'join', 'merge'],
    'constitutes': ['is', 'forms', 'makes up'],
    'contains': ['has'],
    'convene': ['meet'],
    'currently': ['now'],
    'deem': ['believe', 'consider', 'think'],
    'delete': ['cut', 'drop'],
    'demonstrate': ['prove', 'show'],
    'depart': ['leave'],
    'designate': ['appoint', 'choose', 'name'],
    'desire': ['want', 'wish'],
    'determine': ['decide', 'figure', 'find'],
    'disclose': ['show'],
    'discontinue': ['drop', 'stop'],
    'disseminate': ['give', 'issue', 'pass', 'send'],
    'due to the fact that': ['since', 'due to'],
    'during the period': ['during'],
    'effect modifications': ['make changes'],
    'elect': ['choose', 'pick'],
    'eliminate': ['cut', 'drop', 'end'],
    'employ': ['use'],
    'encounter': ['meet'],
    'endeavor': ['try'],
    'ensure': ['make sure'],
    'enumerate': ['count'],
    'equipments': ['equipment'],
    'equitable': ['fair'],
    'establish': ['set up', 'prove', 'show'],
    'evidenced': ['showed'],
    'evident': ['clear'],
    'exhibit': ['show'],
    'expedite': ['speed up', 'hasten'],
    'expeditious': ['fast', 'quick'],
    'expend': ['spend'],
    'expertise': ['ability'],
    'expiration': ['end'],
    'facilitate': ['ease', 'help'],
    'failed to': ['didn’t'],
    'feasible': ['can be done', 'workable'],
    'females': ['women'],
    'finalize': ['complete', 'finish'],
    'for a period of': ['for'],
    'for example,______etc.': ['for example', 'such as'],
    'forfeit': ['give up', 'lose'],
    'forward': ['send'],
    'frequently': ['often'],
    'function': ['work', 'act', 'role'],
    'furnish': ['give', 'send'],
    'has a requirement for': ['needs'],
    'herein': ['here'],
    'heretofore': ['until now'],
    'herewith': ['below', 'here'],
    'however': ['but'],
    'identical': ['same'],
    'identify': ['find', 'name', 'show'],
    'immediately': ['at once'],
    'impacted': ['affected', 'changed'],
    'implement': ['carry out', 'start'],
    'in accordance with': ['by', 'following', 'per'],
    'in addition': ['also', 'besides', 'too'],
    'in an effort to': ['to'],
    'inasmuch as': ['since'],
    'in a timely manner': ['on time', 'promptly'],
    'inception': ['start'],
    'incumbent upon': ['must'],
    'indicate': ['show', 'write down'],
    'indication': ['sign'],
    'initial': ['first'],
    'initiate': ['start'],
    'in lieu of': ['instead'],
    'in order that': ['for', 'so'],
    'in order to': ['to'],
    'in regard to': ['about', 'concerning', 'on'],
    'in relation to': ['about', 'with', 'to'],
    'inter alia': [''],
    'interface': ['work with', 'meet'],
    'interpose no objection': ["don’t object"],
    'in the amount of': ['for'],
    'in the event of': ['if'],
    'in the near future': ['soon', 'shortly'],
    'in the process of': [''],
    'in view of': ['since'],
    'in view of the above': ['so'],
    'is applicable to': ['applies to'],
    'is authorized to': ['may'],
    'is in consonance with': ['agrees with', 'follows'],
    'is responsible for': ['handles'],
    'it appears': ['seems'],
    'it is': [''],
    'it is essential': ['must', 'need to'],
    'it is requested': ['please', 'we request', 'I request'],
    'liaison': ['discussion'],
    'limited number': ['limits'],
    'magnitude': ['size'],
    'maintain': ['keep', 'support'],
    'maximum': ['greatest', 'largest', 'most'],
    'methodology': ['method'],
    'minimize': ['reduce', 'lower'],
    'minimum': ['least', 'smallest'],
    'modify': ['change'],
    'monitor': ['check', 'watch'],
    'necessitate': ['cause', 'need'],
    'notify': ['tell', 'let know'],
    'not later than': ['by', 'before'],
    'notwithstanding': ['in spite of', 'still'],
    'numerous': ['many'],
    'objective': ['goal', 'aim'],
    'obligate': ['bind', 'compel'],
    'observe': ['see'],
    'on a regular basis': [''],
    'operate': ['run', 'use', 'work'],
    'optimum': ['best', 'most'],
    'option': ['choice', 'way'],
    'parameters': ['limits'],
    'participate': ['take part'],
    'perform': ['do'],
    'permit': ['let'],
    'pertaining to': ['about', 'on', 'of'],
    'portion': ['part'],
    'possess': ['have', 'own'],
    'practicable': ['practical'],
    'preclude': ['prevent'],
    'previous': ['earlier'],
    'previously': ['before'],
    'prioritize': ['rank'],
    'prior to': ['before'],
    'proceed': ['go ahead', 'try', 'do'],
    'proficiency': ['skill'],
    'promulgate': ['publish', 'issue'],
    'provide': ['give', 'offer', 'say'],
    'provided that': ['if'],
    'provides guidance for': ['guides'],
    'purchase': ['buy'],
    'pursuant to': ['by', 'under', 'per', 'following'],
    'reflect': ['show', 'say'],
    'regarding': ['about', 'of', 'on'],
    'relative to': ['about', 'on'],
    'relocate': ['move'],
    'remain': ['stay'],
    'remainder': ['rest'],
    'remuneration': ['pay', 'payment'],
    'render': ['make', 'give'],
    'represents': ['is'],
    'request': ['ask'],
    'require': ['must', 'need'],
    'requirement': ['need'],
    'reside': ['live'],
    'retain': ['keep'],
    'said': ['the', 'this', 'that'],
    'selection': ['choice'],
    'set forth in': ['in'],
    'similar to': ['like'],
    'solicit': ['ask for', 'request'],
    'state-of-the-art': ['latest'],
    'submit': ['send', 'give'],
    'subsequent': ['next', 'later'],
    'subsequently': ['then', 'after'],
    'substantial': ['large', 'much'],
    'successfully complete': ['complete', 'pass'],
    'sufficient': ['enough'],
    'terminate': ['end', 'stop'],
    'there are': [''],
    'therefore': ['so'],
    'therein': ['there'],
    'there is': [''],
    'thereof': ['its', 'their'],
    'the undersigned': ['I'],
    'the use of': [''],
    'timely': ['prompt'],
    'time period': [''],
    'transmit': ['send'],
    'type': [''],
    'under the provisions of': ['under'],
    'until such time as': ['until'],
    'utilize': ['use'],
    'utilization': ['use'],
    'validate': ['confirm'],
    'viable': ['practical', 'workable'],
    'vice': ['versus', 'instead of'],
    'warrant': ['permit', 'call for'],
    'whereas': ['since', 'because'],
    'with reference to': ['about'],
    'with the exception of': ['except for'],
    'witnessed': ['saw'],
    'your office': ['you'],
    '/': ['and', 'or'],
}


# In[12]:


medical_dict.update(combined_dict)

def simplify_medical_text(text):
    simplified_text = text
    # Sort dictionary by key length to handle longest phrases first
    for term in sorted(medical_dict, key=lambda x: -len(x)):
        pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
        if pattern.search(simplified_text):
            # Use the first synonym as the simplified term
            replacement = medical_dict[term][0]
            simplified_text = pattern.sub(replacement, simplified_text)
    return simplified_text


# In[13]:


medical_text = "The patient exhibits signs of hypertension and requires antihypertensive therapy."

# Simplify
simplified = simplify_medical_text(medical_text)
print("Simplified Text:", simplified)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




