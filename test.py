import unittest 
import todo 


class testTask(unittest.TestCase):

    def test_evaluation(self):
        golden_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'I-HYP']]
        #auto generate at the end

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]


        #test for btar only

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]

        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]



        golden_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'O']]




        #BTAR WITH ITAR in golden and BTAR with ITAR in golden
        """
        golden_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP'],['B-TAR', 'I-TAR', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'B-HYP'], ['B-TAR', 'I-TAR', 'O', 'B-HYP'],['B-TAR', 'I-TAR', 'O', 'B-HYP']]

        result = todo.evaluate(golden_list, predict_list)
        print("answers shuld be this " + str(result))

        self.assertEqual(result, 0.3333333333333333)
        """

        #when B-Tar is equal at one and not equal in another
        #simple BTAR AND BHYP
        """golden_list = [['B-TAR', 'O', 'O', 'B-HYP'],['O', 'B-TAR', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'B-HYP'],['B-TAR', 'O', 'O', 'B-HYP']]
        result = todo.evaluate(golden_list, predict_list)

        print("answers shuld be this " + str(result))
        self.assertEquals(result,0.5)
        """


if __name__=="__main__":
    unittest.main()
