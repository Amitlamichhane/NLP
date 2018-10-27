import unittest 
import todo 


class testTask(unittest.TestCase):

    def test_evaluation(self):

        golden_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'I-HYP']]
        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))
        self.assertEqual(result, 0.286)
        #auto generate at the end
        golden_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP'] ,['B-TAR', 'I-TAR', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP'],['B-TAR', 'I-TAR', 'O', 'B-HYP']]
        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))



        golden_list = [['B-TAR', 'I-TAR', 'I-TAR', 'B-HYP','I-HYP','I-HYP','O']]
        predict_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP','I-HYP','I-HYP','O']]

        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))


        golden_list = [['O', 'O']]
        predict_list = [['O', 'O']]

        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))

        #B-hyp with I-HYP
        #SIMPLE CASES
        #2 true positive
        #2 false negative
        #2 false positive

        golden_list = [['B-TAR', 'O', 'B-HYP', 'I-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'B-HYP', 'I-HYP']]

        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))
        self.assertEqual(result, 0.5)




        #two different way for simple B-HYP prediction mistake
        #2 true positive
        #2 false negative

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP','O']]
        predict_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'O','O']]

        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))

        self.assertEqual(result, 0.857)



        #BTAR WITH ITAR in golden and BTAR with ITAR in golden

        golden_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP'],['B-TAR', 'I-TAR', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'I-TAR', 'O', 'B-HYP'],['B-TAR', 'I-TAR', 'O', 'B-HYP']]

        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))

        self.assertEqual(result, 0.667)
        """

        #when B-Tar is equal at one and not equal in another
        #simple BTAR AND BHYP
        """
        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'],['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'B-HYP'],['B-TAR', 'I-TAR', 'O', 'B-HYP']]

        result = todo.evaluate(golden_list, predict_list)

        print("answers shuld be this " + str(result))
        self.assertEqual(result,0.75)

        #more exhaustive test needed
        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]
        result = todo.evaluate(golden_list, predict_list)

        print("answers shuld be this " + str(result))
        self.assertEqual(result, 0.571)


        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]
        result = todo.evaluate(golden_list, predict_list)

        print("answers shuld be this " + str(result))
        self.assertEqual(result, 0.571)

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]
        result = todo.evaluate(golden_list, predict_list)

        print("answers shuld be this " + str(result))
        self.assertEqual(result, 0.571)

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]
        result = todo.evaluate(golden_list, predict_list)

        print("answers shuld be this " + str(result))
        self.assertEqual(result, 0.571)


        golden_list = [['B-TAR', 'I-TAR', 'I-TAR', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'B-HYP', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]
        result = todo.evaluate(golden_list, predict_list)

        print("answers shuld be this " + str(result))
        self.assertEqual(result, 0.571)




if __name__=="__main__":
    unittest.main()
