# This code follows the following post.
# http://cramerexplainsmath.com/2018/01/18/solving-chemical-equations-part-5b-chemical-equation-and-matrices/
# @desc This is a driver file for chemicalEquation.
# A detailed description can be found in the post
# @author Cramer Grimes cramergrimes@gmail.com
from chemicalEquation import chemicalEquation
from rowEchelon import rowEchelon


myEquation = chemicalEquation()

myEquation.readEquation("HClO4 + P4O10 + -> H3PO4 + Cl2O7")

myEquation.generateMasterList()

A = myEquation.generateMatrix()

rowEchelon.solveRowEchelon(A)

rowEchelon.showMatrix(A)