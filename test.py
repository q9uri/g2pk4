from g2pk4 import G2p    

g2p = G2p()

text = "こんにちは。나의 친구가 mp3 file 3개를 다운받고 있다"

text = "이봐, 센파이. 한국으로 여행하자? 현지의 맛있는 요리를 먹으면 좋겠다."

a = g2p(text, to_hcj=True)

print(a)