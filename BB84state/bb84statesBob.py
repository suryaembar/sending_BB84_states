#from  SimulaQron.cqc.pythonLib.cqc  import *
from cqc.pythonLib import CQCConnection, qubit
from cqc.cqcHeader import CQC_TP_HELLO
def main():

	# Establish a connection  to  SimulaQron
	# Initialize  the  connection
	with  CQCConnection("Bob") as Bob:
		# Choose  which  basis we  measure  in
		h_B=1
		
		# Wait to  receive a qubit
		q=Bob.recvQubit ()
		
		# If we  chose  the  Hadamard  basis
		# to  measure in, apply H
		if h_B ==1: q.H()
		
		# Measure  the  qubit  in the  standard
		# basis  and  store  the  outcome  in m
		m=q.measure ()
		
		# Print  measurement  outcomeprint
		print ("Bobs  meas. outcome: {}".format(m))
		
		# Close  connection  to  SimulaQron
		Bob.close()

###################################################
main()
