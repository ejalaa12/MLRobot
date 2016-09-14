from ai_regulator import AI_regulator

reg = AI_regulator(sensors=1, actuators=1, hidden=3)
# print reg.generation
# for i in reg.generation.pop:
#     print i.params

print "COMAMD"
print reg.generate_cmd([1])
reg.setScore(10)
print reg.generate_cmd([1])
