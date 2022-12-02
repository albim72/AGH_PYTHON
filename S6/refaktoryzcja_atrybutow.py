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

if deduct(bucket,99):
    print('potrzebne 99 jednostek danych')
else:
    print('nie ma 99 jednostek')
print(bucket)

if deduct(bucket,3):
    print('potrzebne 3 jednostki danych')
else:
    print('nie ma 3 jednostek danych')
print(bucket)
print("***************************************")
print("nowe spojrzenie na wiadro....")


class NewBucket:
    def __init__(self,period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return (f'NewBucket(max_quota={self.max_quota}, quota_consumed: {self.quota_consumed})')

    @property
    def quota(self):
        return self.max_quota-self.quota_consumed

    @quota.setter
    def quota(self,amount):
        delta = self.max_quota - amount
        if amount == 0:
            #liczba jednostek danych jest wyzerowana
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            #liczba jednostek danych przygotowana dla nowego przedziału czasu
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            #liczba jednostek danych wykorzystana w przedziale czasu

            assert self.max_quota >= self.quota_consumed
            self.quota_consumed+=delta

bucket = NewBucket(60)
print(f"początkowo {bucket}")
fill(bucket,100)
print(f'wypełniono: {bucket}')

if deduct(bucket,99):
    print('potrzebne 99 jednostek danych')
else:
    print('nie ma 99 jednostek')
print(f'teraz: {bucket}')

if deduct(bucket,3):
    print('potrzeba 3 jednostki danych')
else:
    print('nie ma 3 jednostek')

print(f'pozostało: {bucket}')
