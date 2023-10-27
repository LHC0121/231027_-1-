def bending_moment_calculator(force, distance):
    bending_moment = force * distance
    return bending_moment

force = float(input("선반에 작용하는 힘의 크기(N):"))
distance = float(input("선반의 굽힘 중심까지의 거리(cm):"))

bending_moment = bending_moment_calculator(force, distance)
print(f"굽힘모멘트 힘: {bending_moment} Nm")

if bending_moment >= 500 :
    print("선반은 위험합니다")
else :
    print("선반은 안전합니다")