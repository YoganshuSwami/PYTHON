def time(hours,minutes):
    total_minutes=(hours*60)+minutes
    return total_minutes
def main():
    hours=int(input("Enter hours : "))
    minutes=int(input("Enter minutes : "))
    total_minutes=time(hours,minutes)
    print("Total Time : ", total_minutes )
x=main()