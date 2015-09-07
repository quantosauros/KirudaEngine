'''
Created on 2015. 9. 4.

@author: Jay
'''

class IndicatorType():
    
    class MovingAverage(enumerate):
        SimpleMovingAverage5Day = "SimpleMovingAverage5Day"
        SimpleMovingAverage20Day = "SimpleMovingAverage20Day"
        SimpleMovingAverage60Day = "SimpleMovingAverage60Day"
        SimpleMovingAverage120Day = "SimpleMovingAverage120Day"
        WeightedMovingAverage5Day = "WeightedMovingAverage5Day"
        WeightedMovingAverage20Day = "WeightedMovingAverage20Day"
        WeightedMovingAverage60Day = "WeightedMovingAverage60Day"
        WeightedMovingAverage120Day = "WeightedMovingAverage120Day"
        ExponentialWeightedMovingAverage5Day = "ExponentialWeightedMovingAverage5Day"
        ExponentialWeightedMovingAverage20Day = "ExponentialWeightedMovingAverage20Day"
        ExponentialWeightedMovingAverage60Day = "ExponentialWeightedMovingAverage60Day"
        ExponentialWeightedMovingAverage120Day = "ExponentialWeightedMovingAverage120Day"
    
    class Indicators(enumerate):
        AccumulationDistricutionIndex= "AccumulationDistricutionIndex"
        
    dataTableMap = {
        MovingAverage.SimpleMovingAverage5Day : "MASi005",
        MovingAverage.SimpleMovingAverage20Day : "MASi020",
        MovingAverage.SimpleMovingAverage60Day : "MASi060",
        MovingAverage.SimpleMovingAverage120Day : "MASi120",
        MovingAverage.WeightedMovingAverage5Day : "MAW005",
        MovingAverage.WeightedMovingAverage20Day : "MAW020",
        MovingAverage.WeightedMovingAverage60Day : "MAW060",
        MovingAverage.WeightedMovingAverage120Day : "MAW120",
        MovingAverage.ExponentialWeightedMovingAverage5Day : "MAEW005",
        MovingAverage.ExponentialWeightedMovingAverage20Day : "MAEW020",
        MovingAverage.ExponentialWeightedMovingAverage60Day : "MAEW060",
        MovingAverage.ExponentialWeightedMovingAverage120Day : "MAEW120",
        Indicators.AccumulationDistricutionIndex : "AD000",
    }
    
    
    
    