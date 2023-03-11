import unittest
from transformer import string_transformer

class TestTransformer(unittest.TestCase):

    def test_tonumber_method(self):
        orig_string = r"Guāng wúshíwúkè bùzài wǒmen shēnbiān, zhè shǐdé yángguāng duì jiànkāng pífū de shānghài chéngwéi quán nián guānzhù de wèntí. Àn shíjiān shùnxù fāshēng de pífū lǎohuà shì wú kě bìmiǎn de (yǔ shíjiān kàngzhēng shì hěn kùnnán de), dàn guāng lǎohuà kuài jiāsù zhè yī guòchéng. Hǎo xiāoxī shì tā shì wánquán kěyǐ yùfáng de. Wǒmen qiúzhù yú Palm bóshì lái jiěshì yǔ guāng lǎohuà xiāngguān de yuányīn hé zhèngzhuàng, yǐjí kěyǐ ràng nín shāowéi yuǎnlí kàng shuāilǎo tōngdào de zhìliáo fāngfǎ."
        correct_transformation = r"Guang1 wu2shi2wu2ke4 bu4zai4 wo3men shen1bian1, zhe4 shi3de2 yang2guang1 dui4 jian4kang1 pi2fu1 de shang1hai4 cheng2wei2 quan2 nian2 guan1zhu4 de wen4ti2. Àn shi2jian1 shun4xu4 fa1sheng1 de pi2fu1 lao3hua4 shi4 wu2 ke3 bi4mian3 de (yu3 shi2jian1 kang4zheng1 shi4 hen3 kun4nan2 de), dan4 guang1 lao3hua4 kuai4 jia1su4 zhe4 yi1 guo4cheng2. Hao3 xiao1xi1 shi4 ta1 shi4 wan2quan2 ke3yi3 yu4fang2 de. Wo3men qiu2zhu4 yu2 Palm bo2shi4 lai2 jie3shi4 yu3 guang1 lao3hua4 xiang1guan1 de yuan2yin1 he2 zheng4zhuang4, yi3ji2 ke3yi3 rang4 nin2 shao1wei2 yuan3li2 kang4 shuai1lao3 tong1dao4 de zhi4liao2 fang1fa3."
        transformer_object = string_transformer()
        transformed_string = transformer_object.to_numbers(orig_string)
        try:
            self.assertEqual(correct_transformation, transformed_string)
            print("Text no.1 passed.")
        except:
            print("TEST NO. 1 FAILED")
            print(f"Original version: {correct_transformation}\n")
            print(f"Received version: {transformed_string}")
        
        orig_string = r"Xǔduō zài zhōngguó yìnshuā de shūjí shǐyòng hùnhé zìtǐ, yuán yīn hé shēngdiào biāojì yǐ yǔ zhōuwéi wénběn bùtóng de zìtǐ chéngxiàn, wǎngwǎng shǐ cǐ lèi pīnyīn wénběn zài yìnshuā shàng xiǎndé bènzhuō."
        correct_transformation = r"Xu3duo1 zai4 zhong1guo2 yin4shua1 de shu1ji2 shi3yong4 hun4he2 zi4ti3, yuan2 yin1 he2 sheng1diao4 biao1ji4 yi3 yu3 zhou1wei2 wen2ben3 bu4tong2 de zi4ti3 cheng2xian4, wang3wang3 shi3 ci3 lei4 pin1yin1 wen2ben3 zai4 yin4shua1 shang4 xian3de2 ben4zhuo1."
        transformer_object = string_transformer()
        transformed_string = transformer_object.to_numbers(orig_string)
        try:
            self.assertEqual(correct_transformation, transformed_string)
            print("Text no.2 passed.")
        except:
            print("TEST NO. 2 FAILED")
            print(f"Original version: {correct_transformation}\n")
            print(f"Received version: {transformed_string}")
        
        orig_string = r"Shǐyòng bǎidù qián bì dú. Bāngzhù zhōngxīn. Qǐyè tuīguǎng. Jīng gōng wǎng ān bèi 11000002000001 hào. Jīng ICP zhèng 030173 hào. Xìnxī wǎngluò chuánbò shìtīng jiémù xǔkě zhèng 0110516. Hùliánwǎng zōngjiào xìnxī fúwù xǔkě zhèng biānhào: Jīng (2022)0000043. Yàopǐn yīliáo qìxiè wǎngluò xìnxī fúwù bèi'àn (jīng) wǎng yàoxiè xìnxī bèi zì (2021) dì 00159 hào."
        correct_transformation = r"Shi3yong4 bai3du4 qian2 bi4 du2. Bang1zhu4 zhong1xin1. Qi3ye4 tui1guang3. Jing1 gong1 wang3 an1 bei4 11000002000001 hao4. Jing1 ICP zheng4 030173 hao4. Xin4xi1 wang3luo4 chuan2bo4 shi4ting1 jie2mu4 xu3ke3 zheng4 0110516. Hu4lian2wang3 zong1jiao4 xin4xi1 fu2wu4 xu3ke3 zheng4 bian1hao4: Jing1 (2022)0000043. Yao4pin3 yi1liao2 qi4xie4 wang3luo4 xin4xi1 fu2wu4 bei4'an4 (jing1) wang3 yao4xie4 xin4xi1 bei4 zi4 (2021) di4 00159 hao4"
        transformer_object = string_transformer()
        transformed_string = transformer_object.to_numbers(orig_string)
        try:
            self.assertEqual(correct_transformation, transformed_string)
            print("Text no. 4 passed.")
        except:
            print("TEST NO. 4 FAILED")
            print(f"Original version: {correct_transformation}\n")
            print(f"Received version: {transformed_string}")
    
    def test_totones_method(self):
        orig_string = r"Xu3duo1 zai4 zhong1guo2 yin4shua1 de shu1ji2 shi3yong4 hun4he2 zi4ti3, yuan2 yin1 he2 sheng1diao4 biao1ji4 yi3 yu3 zhou1wei2 wen2ben3 bu4tong2 de zi4ti3 cheng2xian4, wang3wang3 shi3 ci3 lei4 pin1yin1 wen2ben3 zai4 yin4shua1 shang4 xian3de2 ben4zhuo1."
        correct_transformation = r"Xǔduō zài zhōngguó yìnshuā de shūjí shǐyòng hùnhé zìtǐ, yuán yīn hé shēngdiào biāojì yǐ yǔ zhōuwéi wénběn bùtóng de zìtǐ chéngxiàn, wǎngwǎng shǐ cǐ lèi pīnyīn wénběn zài yìnshuā shàng xiǎndé bènzhuō."
        transformer_object = string_transformer()
        transformed_string = transformer_object.to_marks(orig_string)
        try:
            self.assertEqual(correct_transformation, transformed_string)
            print("Text no. 5 passed.")
        except:
            print("TEST NO. 5 FAILED")
            print(f"Original version: {correct_transformation}\n")
            print(f"Received version: {transformed_string}")

        orig_string = r"Shi3yong4 bai3du4 qian2 bi4 du2. Bang1zhu4 zhong1xin1. Qi3ye4 tui1guang3. Jing1 gong1 wang3 an1 bei4 11000002000001 hao4. Jing1 ICP zheng4 030173 hao4. Xin4xi1 wang3luo4 chuan2bo4 shi4ting1 jie2mu4 xu3ke3 zheng4 0110516. Hu4lian2wang3 zong1jiao4 xin4xi1 fu2wu4 xu3ke3 zheng4 bian1hao4: Jing1 (2022)0000043. Yao4pin3 yi1liao2 qi4xie4 wang3luo4 xin4xi1 fu2wu4 bei4'an4 (jing1) wang3 yao4xie4 xin4xi1 bei4 zi4 (2021) di4 00159 hao4"
        correct_transformation = r"Shǐyòng bǎidù qián bì dú. Bāngzhù zhōngxīn. Qǐyè tuīguǎng. Jīng gōng wǎng ān bèi 11000002000001 hào. Jīng ICP zhèng 030173 hào. Xìnxī wǎngluò chuánbò shìtīng jiémù xǔkě zhèng 0110516. Hùliánwǎng zōngjiào xìnxī fúwù xǔkě zhèng biānhào: Jīng (2022)0000043. Yàopǐn yīliáo qìxiè wǎngluò xìnxī fúwù bèi'àn (jīng) wǎng yàoxiè xìnxī bèi zì (2021) dì 00159 hào"
        transformer_object = string_transformer()
        transformed_string = transformer_object.to_marks(orig_string)
        try:
            self.assertEqual(correct_transformation, transformed_string)
            print("Text no. 6 passed.")
        except:
            print("TEST NO. 6 FAILED")
            print(f"Original version: {correct_transformation}\n")
            print(f"Received version: {transformed_string}")




if __name__ == '__main__':
    unittest.main()