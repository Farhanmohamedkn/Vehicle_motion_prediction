import numpy as np

def my_constant_vel_model(predData,currFrame,trackID,predHorizon,samplingTime):
    #constant velocity model
    #xCenter prediction
    xVelInit = float(predData.loc[(predData['frame']==currFrame) & 
                                  (predData['trackId'] == trackID),'xVelocity'])
    xCenterInit = float(predData.loc[(predData['frame']==currFrame) & 
                                     (predData['trackId'] == trackID),'xCenter'])
    x0 = np.ones(predHorizon)*xCenterInit
    a = np.arange(1,predHorizon+1,1)
    b = np.identity(predHorizon)*xVelInit*samplingTime    
    xCenter = list(x0 + np.matmul(a, b))
    #yCenter prediction
    yVelInit = float(predData.loc[(predData['frame']==currFrame) & 
                                  (predData['trackId'] == trackID),'yVelocity'])
    yCenterInit = float(predData.loc[(predData['frame']==currFrame) & 
                                     (predData['trackId'] == trackID),'yCenter'])
    y0 = np.ones(predHorizon)*yCenterInit
    b = np.identity(predHorizon)*yVelInit*samplingTime    
    yCenter = list(y0 + np.matmul(a, b))
    #heading prediction
    heading = list(predData.loc[(predData['frame']==currFrame) & 
                                (predData['trackId'] == trackID),'heading'])*predHorizon

    prediction = xCenter + yCenter + heading
    return prediction