#from  SimulaQron.cqc.pythonLib.cqc  import *
from cqc.pythonLib import CQCConnection, qubit
from cqc.cqcHeader import CQC_TP_HELLO

def main():
	# Establish  connection  to  SimulaQron
	# Initialize  the  connection
	with  CQCConnection("Alice") as  Alice:
		# Create  new  qubit
		q=qubit(Alice)
		
		# Determine  which  BB84  state to use
		h_A =1;x=0
		
		# if x=1, flip |0> to |1>
		if x == 1: q.X()
		
		# if h_A==1,  convert  to  Hadamard  basis
		if h_A ==1: q.H()
		
		# Send  qubit to Bob
		Alice.sendQubit(q,"Bob")
		
		# Close  connection  to  SimulaQron
		Alice.close ()
		
##############################################################
main()
