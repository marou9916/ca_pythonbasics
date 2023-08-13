def list_benefits():
    return ["More organized code","More readable code","Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence_benefit(benefit):
    return  "%s is a benefit of functions!" % benefit

def name_of_the_benefits():   
    list = list_benefits()
    for benefit in list:
     print (build_sentence_benefit(benefit))

name_of_the_benefits()