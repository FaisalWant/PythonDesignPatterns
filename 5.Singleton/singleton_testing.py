import unittest 


class Singleton(type): 
    _instance={}

    def __call__(cls, *args, **kwargs): 
        if cls not in cls._instance: 
            cls._instance[cls]= super(Singleton,cls).__call__(*args, **kwargs)

        return cls._instances[cls] 



class Database(metaclass=Singleton): 
    def __init__(self): 
        self.population={} 

        f=open('capitals.txt', 'r')
        lines= f.readlines()

        for i in range(0, len(lines), 2): 
            self.population[lines[i].strip()]= int(lines[i+1].strip())
        
        f.close() 


class SingletonRecordFinder: 
    def total_population(self, cities): 
        result=0 
        for c in cities: 
            result+= Database().population[c] 
        
        return result 







class ConfigurableRecordFinder: 
   
    def __init__(self, db): 
        self.db= db   

    def total_population(self, cities): 
        result=0 
        for c in cities: 
            result += self.db.population[c] 
        
        return result 




class DummyDatabase:    #---------------- Dummy Database

    population= {
        "alpha":1, 
        "beta":2, 
        "gamma":3
    }



class SingletonTests(unittest.TestCase): 

    def test_is_singleton(self):  # not the right approach 
        db=Database() 
        db2= Database() 
        self.assertEqual(db, db2) 
    

    def test_singleton_total_population(self):    # not the right approach 
        """"This test on a live database"""

        rf= SingletonRecordFinder()
        names= ['Seoul', 'Mexico City'] 
        tp= rf.total_population(names) 
        self.assertEqual(tp, 17500000+ 17400000) 




    ddb= DummyDatabase()                   # ------------------- Call to Dummy Database 

    def test_dependant_total_population(self):     
        crf= ConfigurableRecordFinder(self.ddb) 
        self.assertEqual(
            crf.total_population(['alpha', 'beta']),
            3
        )



    
    




    
