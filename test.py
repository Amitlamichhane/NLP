import unittest 
import todo 


class testTask(unittest.TestCase):

    def test_evaluation(self):
        golden_list = [['B-TAR', 'I-TAR', 'O', 'B-HYP'], ['B-TAR', 'O', 'O', 'B-HYP']]
        predict_list = [['B-TAR', 'O', 'O', 'O'], ['B-TAR', 'O', 'B-HYP', 'I-HYP']]
        #auto generate at the end

        self.assertEquals(todo.evaluate(golden_list,predict_list),0.286)



if __name__=="__main__":
    unittest.main()
