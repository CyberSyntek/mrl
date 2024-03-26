######SUBTLE MOVMENTS######
# - You may need to adjust "i01_head_eyeRightLR" as mine is about -10 degree less than "i01_head_eyeLeftLR" currently. 
# - My "i01_head_eyelidRightUpper" & "i01_head_eyelidRightLower" have a bit of offset from the left side at mid range positions currently, you may need to slightly adjust or match to left. 
# - Check how "i01_head_rollNeck" is behaving with your calibration, may need adjusting according to your min/max settings. 

###SUBLE EYE MOVMENTS###
def SubtleLookC():
    print("SubtleLookC")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(80)   

def SubtleLookU():
    print("SubtleLookU")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(115)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(115)
    i01_head_eyeRightLR.moveTo(80)

def SubtleLookD():
    print("SubtleLookD")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(65)
    i01_head_eyeLeftLR.moveTo(90)
    i01_head_eyeRightUD.moveTo(65)
    i01_head_eyeRightLR.moveTo(80)

def SubtleLookL():
    print("SubtleLookL")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(120)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(110)

def SubtleLookR():
    print("SubtleLookR")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(90)
    i01_head_eyeLeftLR.moveTo(60)
    i01_head_eyeRightUD.moveTo(90)
    i01_head_eyeRightLR.moveTo(50)

def SubtleLookUL():
    print("SubtleLookUL")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(115)
    i01_head_eyeLeftLR.moveTo(120)
    i01_head_eyeRightUD.moveTo(115)
    i01_head_eyeRightLR.moveTo(110)

def SubtleLookUR():
    print("SubtleLookUR")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(115)
    i01_head_eyeLeftLR.moveTo(60)
    i01_head_eyeRightUD.moveTo(115)
    i01_head_eyeRightLR.moveTo(50)

def SubtleLookDL():
    print("SubtleLookDL")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(65)
    i01_head_eyeLeftLR.moveTo(120)
    i01_head_eyeRightUD.moveTo(65)
    i01_head_eyeRightLR.moveTo(110)

def SubtleLookDR():
    print("SubtleLookDR")
    i01_head_eyeLeftUD.setMaxSpeed()
    i01_head_eyeLeftLR.setMaxSpeed()
    i01_head_eyeRightUD.setMaxSpeed()
    i01_head_eyeRightLR.setMaxSpeed()
    i01_head_eyeLeftUD.moveTo(65)
    i01_head_eyeLeftLR.moveTo(60)
    i01_head_eyeRightUD.moveTo(65)
    i01_head_eyeRightLR.moveTo(50)

###SUBLE EYELID MOVMENTS###
def SubtleEyelidsOpen():
    print("SubtleEyelidsOpen")
    i01_head_eyelidLeftUpper.setMaxSpeed()
    i01_head_eyelidLeftLower.setMaxSpeed()
    i01_head_eyelidRightUpper.setMaxSpeed()
    i01_head_eyelidRightLower.setMaxSpeed()
    i01_head_eyelidLeftUpper.moveTo(180)
    i01_head_eyelidLeftLower.moveTo(180)
    i01_head_eyelidRightUpper.moveTo(180)
    i01_head_eyelidRightLower.moveTo(180)

def SubtleEyelidsMid():
    print("SubtleEyelidsMid")
    i01_head_eyelidLeftUpper.setMaxSpeed()
    i01_head_eyelidLeftLower.setMaxSpeed()
    i01_head_eyelidRightUpper.setMaxSpeed()
    i01_head_eyelidRightLower.setMaxSpeed()
    i01_head_eyelidLeftUpper.moveTo(50)
    i01_head_eyelidLeftLower.moveTo(50)
    i01_head_eyelidRightUpper.moveTo(70)   
    i01_head_eyelidRightLower.moveTo(40)   

def SubtleEyelidsLowerClosing():
    print("SubtleEyelidsLowerClosing")
    i01_head_eyelidLeftUpper.setMaxSpeed()
    i01_head_eyelidLeftLower.setMaxSpeed()
    i01_head_eyelidRightUpper.setMaxSpeed()
    i01_head_eyelidRightLower.setMaxSpeed()
    i01_head_eyelidLeftUpper.moveTo(80)
    i01_head_eyelidLeftLower.moveTo(30)
    i01_head_eyelidRightUpper.moveTo(100)
    i01_head_eyelidRightLower.moveTo(20)

def SubtleEyelidsUpperClosing():
    print("SubtleEyelidsUpperClosing")
    i01_head_eyelidLeftUpper.setMaxSpeed()
    i01_head_eyelidLeftLower.setMaxSpeed()
    i01_head_eyelidRightUpper.setMaxSpeed()
    i01_head_eyelidRightLower.setMaxSpeed()
    i01_head_eyelidLeftUpper.moveTo(20)
    i01_head_eyelidLeftLower.moveTo(80)
    i01_head_eyelidRightUpper.moveTo(40)
    i01_head_eyelidRightLower.moveTo(80)
	
def SubtleBlink():
    print("SubtleBlink")
    i01_head_eyelidLeftUpper.setMaxSpeed()
    i01_head_eyelidLeftLower.setMaxSpeed()
    i01_head_eyelidRightUpper.setMaxSpeed()
    i01_head_eyelidRightLower.setMaxSpeed()
    i01_head_eyelidLeftUpper.moveTo(180)
    i01_head_eyelidLeftLower.moveTo(180)
    i01_head_eyelidRightUpper.moveTo(180)
    i01_head_eyelidRightLower.moveTo(180)
    sleep(0.1)
    i01_head_eyelidLeftUpper.moveTo(0)
    i01_head_eyelidLeftLower.moveTo(0)
    i01_head_eyelidRightUpper.moveTo(0)
    i01_head_eyelidRightLower.moveTo(0)
    sleep(0.1)
    i01_head_eyelidLeftUpper.moveTo(180)
    i01_head_eyelidLeftLower.moveTo(180)
    i01_head_eyelidRightUpper.moveTo(180)
    i01_head_eyelidRightLower.moveTo(180)

###SUBLE EYEBROW MOVMENTS###
def SubtleBrowsC():
    print("SubtleBrowsC")
    i01_head_eyebrowLeft.setMaxSpeed()	
    i01_head_forheadLeft.setMaxSpeed()	
    i01_head_eyebrowRight.setMaxSpeed()	
    i01_head_forheadRight.setMaxSpeed()			
    i01_head_eyebrowLeft.moveTo(90)
    i01_head_forheadLeft.moveTo(90)
    i01_head_eyebrowRight.moveTo(90)
    i01_head_forheadRight.moveTo(90)

def SubtleBrowsD():
    print("SubtleBrowsD")
    i01_head_eyebrowLeft.setMaxSpeed()	
    i01_head_forheadLeft.setMaxSpeed()	
    i01_head_eyebrowRight.setMaxSpeed()	
    i01_head_forheadRight.setMaxSpeed()			
    i01_head_eyebrowLeft.moveTo(20)
    i01_head_forheadLeft.moveTo(20)
    i01_head_eyebrowRight.moveTo(20)
    i01_head_forheadRight.moveTo(20)
	
def SubtleBrowsU():
    print("SubtleBrowsU")
    i01_head_eyebrowLeft.setMaxSpeed()	
    i01_head_forheadLeft.setMaxSpeed()	
    i01_head_eyebrowRight.setMaxSpeed()	
    i01_head_forheadRight.setMaxSpeed()			
    i01_head_eyebrowLeft.moveTo(180)
    i01_head_forheadLeft.moveTo(180)
    i01_head_eyebrowRight.moveTo(180)
    i01_head_forheadRight.moveTo(180)

def SubtleBrowsOuterUpInnerDown():
    print("SubtleBrowsOuterUpInnerDown")
    i01_head_eyebrowLeft.setMaxSpeed()	
    i01_head_forheadLeft.setMaxSpeed()	
    i01_head_eyebrowRight.setMaxSpeed()	
    i01_head_forheadRight.setMaxSpeed()			
    i01_head_eyebrowLeft.moveTo(180)
    i01_head_forheadLeft.moveTo(50)
    i01_head_eyebrowRight.moveTo(180)
    i01_head_forheadRight.moveTo(50)
	
def SubtleBrowsOuterDownInnerUp():
    print("SubtleBrowsOuterUpInnerDown")
    i01_head_eyebrowLeft.setMaxSpeed()	
    i01_head_forheadLeft.setMaxSpeed()	
    i01_head_eyebrowRight.setMaxSpeed()	
    i01_head_forheadRight.setMaxSpeed()			
    i01_head_eyebrowLeft.moveTo(50)
    i01_head_forheadLeft.moveTo(180)
    i01_head_eyebrowRight.moveTo(50)
    i01_head_forheadRight.moveTo(180)	

def SubtleBrowsLeftUp():
    print("SubtleBrowsLeftUp")
    i01_head_eyebrowLeft.setMaxSpeed()	
    i01_head_forheadLeft.setMaxSpeed()	
    i01_head_eyebrowRight.setMaxSpeed()	
    i01_head_forheadRight.setMaxSpeed()			
    i01_head_eyebrowLeft.moveTo(180)
    i01_head_forheadLeft.moveTo(180)
    i01_head_eyebrowRight.moveTo(90)
    i01_head_forheadRight.moveTo(90)

def SubtleBrowsRightUp():
    print("SubtleBrowsRightUp")
    i01_head_eyebrowLeft.setMaxSpeed()	
    i01_head_forheadLeft.setMaxSpeed()	
    i01_head_eyebrowRight.setMaxSpeed()	
    i01_head_forheadRight.setMaxSpeed()		
    i01_head_eyebrowLeft.moveTo(90)
    i01_head_forheadLeft.moveTo(90)
    i01_head_eyebrowRight.moveTo(180)
    i01_head_forheadRight.moveTo(180)	  

###SUBLE NECK MOVMENTS###
def SubtleNeckC():
    print("SubtleNeckC")
    i01_head_rollNeck.setSpeed(60)
    i01_head_rollNeck.moveTo(120)
    i01_head_rothead.setSpeed(40)
    i01_head_rothead.moveTo(80) 

def SubtleNeckL():
    print("SubtleNeckL")
    i01_head_neck.setSpeed(140)
    i01_head_rollNeck.setSpeed(60)
    i01_head_neck.moveTo(50)
    i01_head_rollNeck.moveTo(60)

def SubtleNeckR():
    print("SubtleNeckR")
    i01_head_neck.setSpeed(140)
    i01_head_rollNeck.setSpeed(60)
    i01_head_neck.moveTo(50)
    i01_head_rollNeck.moveTo(180)

def SubtleNeckTurnC():
    print("SubtleNeckTurnC")
    i01_head_rothead.setSpeed(40)
    i01_head_rothead.moveTo(90) 

def SubtleNeckTurnL():
    print("SubtleNeckTurnL")
    i01_head_rothead.setSpeed(40)
    i01_head_rothead.moveTo(80) 

def SubtleNeckTurnR():
    print("SubtleNeckTurnR")
    i01_head_rothead.setSpeed(40)
    i01_head_rothead.moveTo(100) 

###SUBLE TORSO MOVMENTS###
def SubtleStomC():
    print("SubtleTopStomC")
    i01_torso_topStom.setSpeed(20)
    i01_torso_topStom.moveTo(90)
    i01_torso_midStom.setSpeed(10)
    i01_torso_midStom.moveTo(90)

def SubtleTopStomC():
    print("SubtleTopStomC")
    i01_torso_topStom.setSpeed(20)
    i01_torso_topStom.moveTo(90)

def SubtleTopStomL():
    print("SubtleTopStomL")
    i01_torso_topStom.setSpeed(20)
    i01_torso_topStom.moveTo(80)

def SubtleTopStomR():
    print("SubtleTopStomR")
    i01_torso_topStom.setSpeed(20)
    i01_torso_topStom.moveTo(100)

def SubtleMidStomC():
    print("SubtleMidStomC")
    i01_torso_midStom.setSpeed(10)
    i01_torso_midStom.moveTo(90)

def SubtleMidStomL():
    print("SubtleMidStomL")
    i01_torso_midStom.setSpeed(10)
    i01_torso_midStom.moveTo(70)

def SubtleMidStomR():
    print("SubtleMidStomR")
    i01_torso_midStom.setSpeed(10)
    i01_torso_midStom.moveTo(110)
