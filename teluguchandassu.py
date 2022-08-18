
import regex as re
v=input("ఒక పదాన్ని నమోదు చేయండి :")
w=v
print(v)



U=["ా","ీ","ూ","ౄ","ౣ","ే","ై","ో","ౌ","ః"]
L=["ఆ","ఈ","ఊ","ౠ","ౡ","ఏ","ఐ","ఓ","ఔ","అః"]
N={"UII":"భ గణము",
   "IUI":"జ గణము",
   "IIU":"స గణము",
   "III":"న గణము",
   "IUU":"య గణము",
   "UIU":"ర గణము",
   "UUI":"త గణము",
   "UUU":"మ గణము",
   "UI":"గల గణము",
   "IIIU":"నగ గణము",
   "IIUI":"సల గణము",
   "IIII":"నల గణము",
   "UIII":"భల గణము",
   "UIIU":"భగరు గణము",
   "UUII":"తల గణము",
   "UUIU":"తగ గణము",
   "UUUI":"మలఘ గణము",
   "IIIII":"నలల గణము",
   "IIIUU":"నగగ గణము",
   "IIIIU":"నవ గణము",
   "IIUUI":"సహ గణము",
   "IIUIU":"సవ గణము",
   "IIUUU":"సగగ గణము",
   "IIIUI":"నహ గణము",
   "UIUU":"రగురు గణము",
   "IIII":"నల గణము",}


l=['క్','ఖ్','గ్','ఘ్','ఙ్','చ్','ఛ్','జ్','ఝ్','ఞ్','ట్','ఠ్','డ్','ఢ్','ణ్','త్','థ్','ద్','ధ్',
   'న్','ప్','ఫ్','బ్','భ్','మ్','య్','ర్','ల్','వ్','శ్','ష్','స్','హ్','ళ్','క్ష్','ఱ్']
f=[]
out=""
v=list(v.split())


for text in v:
  k=(re.findall(r'\X', text, re.U))
print(k)


ele=k.pop()
res = [i for i in k if i not in l]
res.append(ele)
print(res)

for i in res:
  k=str(i)
  for i in k:
    f.append(i)
  print(f)
  if any(x in U for x in f):
    out+="U"
  elif any(x in L for x in f):
    out+="U"
  else:
    out+="I"
  f.clear()

print("",out)
print(w+" అనే పదం "+ N[out] +"కు చెందినది")