from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
app = Flask(__name__)
with open('Crime_Type.pkl', 'rb') as f:
    model1 = pickle.load(f)
with open('Crime_severity2.pkl', 'rb') as f:
    model2 = pickle.load(f)
with open('Area1.pkl', 'rb') as f:
    model3 = pickle.load(f)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        areas={7: 'Wilshire',
 1: 'Central',
 3: 'Southwest',
 9: 'Van Nuys',
 6: 'Hollywood',
 18: 'Southeast',
 13: 'Newton',
 19: 'Mission',
 2: 'Rampart',
 10: 'West Valley',
 8: 'West LA',
 20: 'Olympic',
 4: 'Hollenbeck',
 21: 'Topanga',
 11: 'Northeast',
 12: '77th Street',
 14: 'Pacific',
 15: 'N Hollywood',
 5: 'Harbor',
 16: 'Foothill',17: 'Devonshire'}
        crime={510: 'VEHICLE - STOLEN',
 330: 'BURGLARY FROM VEHICLE',
 480: 'BIKE - STOLEN',
 343: 'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)',
 354: 'THEFT OF IDENTITY',
 624: 'BATTERY - SIMPLE ASSAULT',
 821: 'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH',
 812: 'CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)',
 810: 'SEX,UNLAWFUL(INC MUTUAL CONSENT, PENETRATION W/ FRGN OBJ',
 230: 'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT',
 956: 'LETTERS, LEWD  -  TELEPHONE CALLS, LEWD',
 341: 'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD',
 930: 'CRIMINAL THREATS - NO WEAPON DISPLAYED',
 668: 'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)',
 420: 'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)',
 813: 'CHILD ANNOYING (17YRS & UNDER)',
 310: 'BURGLARY',
 903: 'CONTEMPT OF COURT',
 440: 'THEFT PLAIN - PETTY ($950 & UNDER)',
 626: 'INTIMATE PARTNER - SIMPLE ASSAULT',
 762: 'LEWD CONDUCT',
 441: 'THEFT PLAIN - ATTEMPT',
 331: 'THEFT FROM MOTOR VEHICLE - GRAND ($950.01 AND OVER)',
 946: 'OTHER MISCELLANEOUS CRIME',
 210: 'ROBBERY',
 662: 'BUNCO, GRAND THEFT',
 860: 'BATTERY WITH SEXUAL CONTACT',
 236: 'INTIMATE PARTNER - AGGRAVATED ASSAULT',
 820: 'ORAL COPULATION',
 661: 'UNAUTHORIZED COMPUTER ACCESS',
 901: 'VIOLATION OF RESTRAINING ORDER',
 442: 'SHOPLIFTING - PETTY THEFT ($950 & UNDER)',
 740: 'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)',
 761: 'BRANDISH WEAPON',
 649: 'DOCUMENT FORGERY / STOLEN FELONY',
 845: 'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE',
 121: 'RAPE, FORCIBLE',
 745: 'VANDALISM - MISDEAMEANOR ($399 OR UNDER)',
 627: 'CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT',
 653: 'CREDIT CARDS, FRAUD USE ($950.01 & OVER)',
 928: 'THREATENING PHONE CALLS/LETTERS',
 815: 'SEXUAL PENETRATION W/FOREIGN OBJECT',
 940: 'EXTORTION',
 625: 'OTHER ASSAULT',
 352: 'PICKPOCKET',
 648: 'ARSON',
 886: 'DISTURBING THE PEACE',
 666: 'BUNCO, ATTEMPT',
 921: 'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE',
 932: 'PEEPING TOM',
 900: 'VIOLATION OF COURT ORDER',
 439: 'FALSE POLICE REPORT',
 954: 'CONTRIBUTING',
 434: 'FALSE IMPRISONMENT',
 235: 'CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT',
 220: 'ATTEMPTED ROBBERY',
 654: 'CREDIT CARDS, FRAUD USE ($950 & UNDER',
 922: 'CHILD STEALING',
 760: 'LEWD/LASCIVIOUS ACTS WITH CHILD',
 670: 'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
 850: 'INDECENT EXPOSURE',
 237: 'CHILD NEGLECT (SEE 300 W.I.C.)',
 763: 'STALKING',
 345: 'DISHONEST EMPLOYEE - GRAND THEFT',
 888: 'TRESPASSING',
 320: 'BURGLARY, ATTEMPTED',
 122: 'RAPE, ATTEMPTED',
 753: 'DISCHARGE FIREARMS/SHOTS FIRED',
 805: 'PIMPING',
 822: 'HUMAN TRAFFICKING - COMMERCIAL SEX ACTS',
 520: 'VEHICLE - ATTEMPT STOLEN',
 806: 'PANDERING',
 906: 'FIREARMS RESTRAINING ORDER (FIREARMS RO)',
 437: 'RESISTING ARREST',
 410: 'BURGLARY FROM VEHICLE, ATTEMPTED',
 350: 'THEFT, PERSON',
 623: 'BATTERY POLICE (SIMPLE)',
 522: 'VEHICLE, STOLEN - OTHER (MOTORIZED SCOOTERS, BIKES, ETC)',
 450: 'THEFT FROM PERSON - ATTEMPT',
 890: 'FAILURE TO YIELD',
 755: 'BOMB SCARE',
 231: 'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER',
 664: 'BUNCO, PETTY THEFT',
 251: 'SHOTS FIRED AT INHABITED DWELLING',
 951: 'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $950 & UNDER',
 920: 'KIDNAPPING - GRAND ATTEMPT',
 250: 'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
 470: 'TILL TAP - GRAND THEFT ($950.01 & OVER)',
 902: 'VIOLATION OF TEMPORARY RESTRAINING ORDER',
 647: 'THROWING OBJECT AT MOVING VEHICLE',
 651: 'DOCUMENT WORTHLESS ($200.01 & OVER)',
 910: 'KIDNAPPING',
 110: 'CRIMINAL HOMICIDE',
 351: 'PURSE SNATCHING',
 421: 'THEFT FROM MOTOR VEHICLE - ATTEMPT',
 444: 'DISHONEST EMPLOYEE - PETTY THEFT',
 814: 'CHILD PORNOGRAPHY',
 756: 'WEAPONS POSSESSION/BOMBING',
 433: 'DRIVING WITHOUT OWNER CONSENT (DWOC)',
 931: 'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)',
 435: 'LYNCHING',
 438: 'RECKLESS DRIVING',
 443: 'SHOPLIFTING - ATTEMPT',
 660: 'COUNTERFEIT',
 950: 'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $950.01',
 622: 'BATTERY ON A FIREFIGHTER',
 943: 'CRUELTY TO ANIMALS',
 487: 'BOAT - STOLEN',
 949: 'ILLEGAL DUMPING',
 933: 'PROWLER',
 865: 'DRUGS, TO A MINOR',
 474: 'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
 652: 'DOCUMENT WORTHLESS ($200 & UNDER)',
 113: 'MANSLAUGHTER, NEGLIGENT',
 446: 'PETTY THEFT - AUTO REPAIR',
 475: 'THEFT, COIN MACHINE - ATTEMPT',
 471: 'TILL TAP - PETTY ($950 & UNDER)',
 451: 'PURSE SNATCHING - ATTEMPT',
 436: 'LYNCHING - ATTEMPTED',
 485: 'BIKE - ATTEMPTED STOLEN',
 349: 'GRAND THEFT / AUTO REPAIR',
 944: 'CONSPIRACY',
 942: 'BRIBERY',
 347: 'GRAND THEFT / INSURANCE FRAUD',
 353: 'DRUNK ROLL',
 870: 'CHILD ABANDONMENT',
 473: 'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)',
 880: 'DISRUPT SCHOOL',
 452: 'PICKPOCKET, ATTEMPT',
 924: 'TELEPHONE PROPERTY - DAMAGE',
 840: 'BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT WITH ANIM',
 948: 'BIGAMY',
 884: 'FAILURE TO DISPERSE',
 904: 'FIREARMS EMERGENCY PROTECTIVE ORDER (FIREARMS EPO)',
 830: 'INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)',
 432: 'BLOCKING DOOR INDUCTION CENTER',
 882: 'INCITING A RIOT',
 445: 'DISHONEST EMPLOYEE ATTEMPTED THEFT',
 926: 'TRAIN WRECKING'}
        
        area= float(request.form.get('AREA'))
        rpt_dist=float(request.form.get('Rpt_Dist_No'))
        lat=float(request.form.get('LAT'))
        lon=float(request.form.get('LON'))
        day_rptd=float(request.form.get('day_rptd'))
        month_rptd=float(request.form.get('month_rptd'))
        year_rptd=float(request.form.get('year_rptd'))
        day_occ=float(request.form.get('day_occ'))
        month_occ=float(request.form.get('month_occ'))
        year_occ=float(request.form.get('year_occ'))
        hour=float(request.form.get('hour'))
        min=float(request.form.get('minute'))
        occ_hour=float(request.form.get('occ_hour'))
        occ_min=float(request.form.get('occ_minute'))
        weapon=float(request.form.get('weapon'))
        sex=float(request.form.get('vict_sex'))
        age= float(request.form.get('vict_age'))
        descent=float(request.form.get('vict_descent'))
        area1=[lat,lon]
        features=[area,rpt_dist,lat,lon,day_rptd,month_rptd,year_rptd,day_occ,month_occ,year_occ,hour,min,occ_hour,occ_min]
        x=np.array([features])
        area2=np.array([area1])
        predictions = model1.predict(x)
        predictions = predictions.tolist()
        predictions1=crime[predictions[0]]
        print(predictions1)
        area3=model3.predict(area2)
        print("area:",areas[area3[0]])
        sever=[area,rpt_dist,predictions[0],weapon,sex,age,descent,lat,lon]
        sever=np.array([sever])
        severity=model2.predict(sever)
        if(severity==2):
            severity="Critical"
        else:
            severity="not critical"

        return render_template('results.html', predictions=predictions1, area=areas[area3[0]], severity=severity)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
