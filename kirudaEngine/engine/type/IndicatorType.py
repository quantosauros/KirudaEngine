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
        
    dataTableMap = {
        MovingAverage.SimpleMovingAverage5Day : "SMA005",
        MovingAverage.SimpleMovingAverage20Day : "SMA020",
        MovingAverage.SimpleMovingAverage60Day : "SMA060",
        MovingAverage.SimpleMovingAverage120Day : "SMA120",
        MovingAverage.WeightedMovingAverage5Day : "WMA005",
        MovingAverage.WeightedMovingAverage20Day : "WMA020",
        MovingAverage.WeightedMovingAverage60Day : "WMA060",
        MovingAverage.WeightedMovingAverage120Day : "WMA120",
        MovingAverage.ExponentialWeightedMovingAverage5Day : "EWMA005",
        MovingAverage.ExponentialWeightedMovingAverage20Day : "EWMA020",
        MovingAverage.ExponentialWeightedMovingAverage60Day : "EWMA060",
        MovingAverage.ExponentialWeightedMovingAverage120Day : "EWMA120",
    }
    
    
    
    