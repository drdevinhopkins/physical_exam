from fastapi import FastAPI
app = FastAPI()


# @app.get("/cc/{cc}")
# async def read_item(cc):
#     return {"cc": cc}


# @app.get("/nlp/")
# async def read_doc(text):
#     doc = nlp(text)
#     return {"ents": [{'ent_name': ent.kb_id_.split('/')[-1].replace('_', ' ')} for ent in doc.ents]}


@app.get("/options")
async def root():
    general = {'section': 'General', 'options': ['Awake, alert and oriented', 'No acute distress', 'Somnolent',
               'Confused', 'Appears in pain', 'Weak', 'Resting comfortably']}
    cardiac = {'section': 'Cardiac', 'options': ['Normal S1, S2', 'No murmurs or gallops',
               'Peripheral pulses 2+ & equal x 4', 'Irregular pulses', 'Systolic ejection murmur']}
    respiratory = {'section': 'Respiratory', 'options': ['Good air entry bilaterally', 'No adventitious sounds',
                   'Breathing comfortably', 'Coughing', 'Laboured breathing']}
    abdomen = {'section': 'Abdomen', 'options': [
        'Soft, non-tender', 'Not distended', 'No CVA tenderness', 'No guarding or rebound']}
    heent = {'section': 'HEENT', 'options': [
        'No evidence of head trauma', 'No signs of basilar skull fracture', 'No C-spine tenderness, full ROM', 'Normal pharynx', 'No adenopathy']}
    output = {"physicalExam": [general, cardiac, respiratory, abdomen, heent]}
    return output


@ app.get("/help/")
async def help():
    with open('help.txt') as f:
        lines = f.readlines()
    return {"text": lines}
