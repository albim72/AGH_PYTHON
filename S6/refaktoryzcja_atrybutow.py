from datetime import datetime,timedelta

class Bucket:
    def __init__(self,period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota={self.quota})'

bucket = Bucket(60)
print(bucket)

def fill(bucket,amount):
    now = datetime.now()
    if(now-bucket.reset_time)>bucket.period_delta:
        bucket.quota=0
        bucket.reset_time = now
    bucket.quota+=amount

def deduct(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False #wiadro nie zostało napełnione
    if bucket.quota -amount<0:
        return False #wiadro zostało częściowo napełnione
    bucket.quota -= amount
    return True #Wiadro zostało napełnione

bucket = Bucket(60)
fill(bucket,100)
print(bucket)

