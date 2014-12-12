#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdb
import uniout
from pprint import pprint
import random
vvtk_name_list =[
    ["稽核室","A00699","黃莉婷",],
    ["董事長室","A00001","陳文昌",],
    ["董事長室","A00003","藍志忠",],
    ["董事長室","A00055","廖思鈞",],
    ["董事長室","A00213","劉禹均",],
    ["董事長室","A00492","高語辰",],
    ["董事長室","A00953","朱天羽",],
    ["董事長室","A01018","賈翔誼",],
    ["執行副總經理","A00028","馬仕毅",],
    ["管理處","A00412","左偉莉",],
    ["財務部","A00013","周美茵",],
    ["財務部","A00392","蔡秉芸",],
    ["財務部","A00485","洪秀棻",],
    ["會計部","A00084","邱秀滿",],
    ["會計部","A00170","林葳涵",],
    ["會計部","A00446","李世傑",],
    ["會計部","A00619","方少琬",],
    ["會計部","A00746","吳凌雲",],
    ["會計部","A01050","沈宏霖",],
    ["會計部","A01186","李振菁",],
    ["資訊部","A00692","黃政清",],
    ["資訊部","A00767","陳栯羚",],
    ["資訊部","A00810","陳君彥",],
    ["資訊部","A00875","陳世崟",],
    ["網路系統管理組","A00635","張晴凱",],
    ["網路系統管理組","A00756","劉啟新",],
    ["資訊系統管理組","A00544","李威慶",],
    ["資訊系統管理組","A01206","黃建榮",],
    ["總務部","A00122","劉國忠",],
    ["總務部","A00325","陳怡蓉",],
    ["總務部","A01016","陳芷蕎",],
    ["總務部","A01045","鄭弘昌",],
    ["總務部","A90025","林素櫻",],
    ["人力資源部","A00163","周玓宇",],
    ["人力資源部","A00631","林家榮",],
    ["人力資源部","A00818","林亞璇",],
    ["人力資源部","A00955","林小琪",],
    ["人力資源部","A01113","陳雯娟",],
    ["國際事業處","A00047","顧中威",],
    ["策略採購部","A01089","陳育琮",],
    ["策略採購部","A01119","范志賓",],
    ["策略採購部","A01127","陳姿蘭",],
    ["策略採購部","A01128","張雅瑜",],
    ["策略採購部","A01129","邱俊超",],
    ["策略採購部","A01159","黃千玲",],
    ["非洲中東組","A00553","楊進汶",],
    ["非洲中東組","A00572","郭家彰",],
    ["非洲中東組","A01084","吳永偉",],
    ["亞洲一組","A00958","鄭承孟",],
    ["亞洲一組","A01051","盧顯",],
    ["亞洲二組","A00681","尉遲炘",],
    ["亞洲二組","A00723","景怡齡",],
    ["亞洲二組","A01092","金娳婷",],
    ["亞洲二組","A01193","吳韋志",],
    ["拉美組","A00491","江志穎",],
    ["拉美組","A00559","陳威安",],
    ["拉美組","A00919","林明洲",],
    ["拉美組","A01137","莎拉",],
    ["行銷企劃部","A00230","程香綺",],
    ["行銷企劃部","A00920","王懷璐",],
    ["通路行銷組","A00598","詹尹甄",],
    ["通路行銷組","A00612","張家瑋",],
    ["通路行銷組","A00852","朱怡君",],
    ["通路行銷組","A00904","林璧圓",],
    ["通路行銷組","A01065","許孟傑",],
    ["媒體設計組","A00242","李泰鑫",],
    ["媒體設計組","A00253","邱世偉",],
    ["媒體設計組","A00580","黃健嘉",],
    ["媒體設計組","A00607","盧譽才",],
    ["媒體設計組","A01100","丘湘琳",],
    ["媒體設計組","A01204","李青蔚",],
    ["產品管理部","A00698","李慧玉",],
    ["產品管理部","A00714","周若茵",],
    ["產品管理部","A00728","徐步鯤",],
    ["產品管理部","A01109","陳明宗",],
    ["產品規劃組","A00227","曾淑鈴",],
    ["產品規劃組","A00407","張凱鈞",],
    ["產品規劃組","A00999","顧殷如",],
    ["產品規劃組","A01019","劉嘉偉",],
    ["專案管理組","A00622","邱顯婷",],
    ["專案管理組","A00629","任霞",],
    ["專案管理組","A00782","陳芳儀",],
    ["專案管理組","A00800","徐婉婷",],
    ["專案管理組","A01025","陳錦堂",],
    ["專案管理組","A01121","簡欣雯",],
    ["方案規劃組","A00790","張洋榕",],
    ["方案規劃組","A00945","巫芳萍",],
    ["方案規劃組","A00998","宋佩穗",],
    ["方案規劃組","A01123","孫柏青",],
    ["國際專案部","A00246","廖邦廷",],
    ["國際專案部","A00256","林政緯",],
    ["國際專案部","A00390","劉信宏",],
    ["國際專案部","A00703","許騰元",],
    ["國際專案部","A00791","陳志達",],
    ["國際專案部","A00965","蔡沛任",],
    ["國際專案部","A01082","周韋宏",],
    ["國際專案部","A01083","鄧維侖",],
    ["國際專案部","A01160","方娜拉",],
    ["歐洲業務部","A00415","柯素梅",],
    ["歐洲業務部","A00834","柯玫君",],
    ["歐洲一組","A00537","林鈺庭",],
    ["歐洲一組","A01110","雷路加",],
    ["歐洲一組","A01176","石逸凡",],
    ["歐洲二組","A00804","鄧琮寶",],
    ["歐洲二組","A01102","迪雅哥",],
    ["歐洲二組","A01165","傅惠德",],
    ["歐洲事業處","A00143","吳文貴",],
    ["歐洲專案部","A00101","侯志星",],
    ["歐洲專案部","A00947","郭政錦",],
    ["歐洲專案部","A00986","吳元鈞",],
    ["歐洲專案部","A01059","楊沛雯",],
    ["行銷企劃處","A01085","蘇建群",],
    ["國際業務一部","A00312","王芊云",],
    ["國際業務一部","A00420","陳之皇",],
    ["國際業務一部","A01175","劉威辰",],
    ["國際業務二部","A00274","連怡瑩",],
    ["國際業務二部","A00386","羅亦鎧",],
    ["國際業務二部","A00413","黃俐敏",],
    ["國際業務二部","A01136","鄭翊如",],
    ["代工事業處","A00019","廖禎祺",],
    ["代工事業處","A00171","楊秀慧",],
    ["代工事業處","A00909","劉佳玲",],
    ["專案技術部","A00207","張為棟",],
    ["專案技術部","A00575","吳采澄",],
    ["專案技術部","A00968","張庭嬡",],
    ["代工業務一部","A00133","陳殷康",],
    ["代工業務一部","A00273","張建文",],
    ["代工業務一部","A00429","陸怡璇",],
    ["代工業務一部","A00480","林若文",],
    ["代工業務一部","A00753","莊宗蓉",],
    ["代工業務一部","A00899","江欣庭",],
    ["代工業務一部","A01035","王芷宜",],
    ["代工業務一部","A01135","藍立穎",],
    ["代工業務二部","A00266","胡詔祥",],
    ["代工業務二部","A00321","張美娟",],
    ["代工業務二部","A00402","馮麗萍",],
    ["代工業務二部","A00448","劉怡伶",],
    ["代工業務二部","A00533","葉珈瑄",],
    ["代工業務二部","A00884","廖瑞雯",],
    ["代工業務二部","A00944","謝欣如",],
    ["研發一處","A00049","鄭聖夫",],
    ["研發一處","A00147","廖彥鈞",],
    ["研發一處","A01199","程意慈",],
    ["系統整合部","A00189","梁琬珮",],
    ["系統整合部","A00255","張永伸",],
    ["系統整合一組","A00531","林子翔",],
    ["系統整合一組","A00620","郭依青",],
    ["系統整合一組","A00680","鄭俊誠",],
    ["系統整合一組","A00850","謝國爗",],
    ["系統整合一組","A00901","許博豪",],
    ["系統整合一組","A01168","許文耀",],
    ["系統整合二組","A00202","陳聖元",],
    ["系統整合二組","A00395","蔡界平",],
    ["系統整合二組","A00556","曾志豪",],
    ["系統整合二組","A00558","王雅萱",],
    ["系統整合二組","A00787","陳尹凡",],
    ["系統整合二組","A00827","林祐綱",],
    ["系統整合二組","A01201","林冠宇",],
    ["系統整合三組","A00197","郭曜銘",],
    ["系統整合三組","A00248","張千威",],
    ["系統整合三組","A00517","葉再傳",],
    ["系統整合三組","A00826","吳思穎",],
    ["系統整合三組","A00957","洪健二",],
    ["系統整合三組","A01062","葉耕成",],
    ["系統整合三組","A01198","唐怡君",],
    ["系統整合四組","A00349","陳琮凱",],
    ["系統整合四組","A00460","羅明遠",],
    ["系統整合四組","A00701","阮昱勳",],
    ["系統整合四組","A00849","周元超",],
    ["系統整合四組","A00876","羅輯",],
    ["系統整合四組","A01190","方建平",],
    ["軟體開發部","A00264","郭騰凱",],
    ["軟體開發部","A01091","張哲維",],
    ["應用軟體組","A00316","鄭欽議",],
    ["應用軟體組","A00915","巫冠忠",],
    ["應用軟體組","A01054","朱明初",],
    ["應用軟體組","A01086","褚立陽",],
    ["軟體品質保證組","A00339","蔡銘鴻",],
    ["軟體品質保證組","A00830","林雍舜",],
    ["軟體品質保證組","A01024","孫玉萍",],
    ["軟體平台組","A00379","管健男",],
    ["軟體平台組","A00414","陳思翰",],
    ["軟體平台組","A00668","李昆擇",],
    ["軟體平台組","A00709","徐斌峰",],
    ["軟體平台組","A00867","林佩嫺",],
    ["使用者經驗組","A00561","劉倩雯",],
    ["使用者經驗組","A00717","林彥甫",],
    ["使用者經驗組","A00869","施以萱",],
    ["使用者經驗組","A00946","陳麒元",],
    ["使用者經驗組","A01099","鄭世暉",],
    ["使用者經驗組","A01166","莊鎧賸",],
    ["行動應用組","A00310","許倫維",],
    ["行動應用組","A00545","卓晉緯",],
    ["行動應用組","A01183","陸凱暉",],
    ["硬體開發部","A00175","蔡詒安",],
    ["硬體開發部","A00421","姬文洲",],
    ["安規暨線路佈局組","A00087","張瓊文",],
    ["安規暨線路佈局組","A00240","鄭育仁",],
    ["安規暨線路佈局組","A00270","高櫻珍",],
    ["安規暨線路佈局組","A00427","高嘉珮",],
    ["安規暨線路佈局組","A00560","周仁傑",],
    ["硬體一組","A00262","張定家",],
    ["硬體一組","A00433","蔡子揚",],
    ["硬體一組","A00441","陳興志",],
    ["硬體一組","A00468","林佳慶",],
    ["硬體一組","A00696","姚嘉祺",],
    ["硬體一組","A01182","洪煜喬",],
    ["硬體二組","A00535","黃彥傑",],
    ["硬體二組","A00568","陳俊仰",],
    ["硬體二組","A00695","張育齊",],
    ["硬體二組","A01011","吳俊義",],
    ["硬體二組","A01161","周維駿",],
    ["機構開發部","A00381","許志回",],
    ["機構開發部","A00399","黃玉嬌",],
    ["機構一組","A00400","陳泗興",],
    ["機構一組","A00570","林志鴻",],
    ["機構一組","A00617","詹智傑",],
    ["機構一組","A00689","黃尚宇",],
    ["機構一組","A00739","陳志豪",],
    ["機構一組","A00951","陳青青",],
    ["機構一組","A01030","黃尚豪",],
    ["機構二組","A00102","黃聖鑌",],
    ["機構二組","A00467","黃仲雍",],
    ["機構二組","A00528","蔡瓊緯",],
    ["機構二組","A00718","王俊英",],
    ["機構二組","A00773","游章充",],
    ["機構二組","A01114","張紡慈",],
    ["專案開發部","A00144","陳志彬",],
    ["專案開發部","A90069","簡韶逸",],
    ["通訊協定組","A00258","郭任傑",],
    ["通訊協定組","A00311","郭嘉明",],
    ["通訊協定組","A00729","吳柏庚",],
    ["通訊協定組","A00877","楊凱閔",],
    ["通訊協定組","A00949","駱文城",],
    ["通訊協定組","A01115","陳祖頤",],
    ["通訊協定組","A01169","黃敬文",],
    ["通訊協定組","A01170","吳華軒",],
    ["通訊協定組","A01205","彭脩舜",],
    ["系統應用二組","A00315","鐘逸民",],
    ["系統應用二組","A00751","林建成",],
    ["系統應用二組","A00970","陳彥璋",],
    ["系統應用二組","A01013","徐健峰",],
    ["系統應用二組","A01155","郭俊麒",],
    ["系統應用二組","A01208","游舜勛",],
    ["系統應用一組","A00388","陳志強",],
    ["系統應用一組","A00715","蔡宜蓁",],
    ["系統應用一組","A01023","楊善雯",],
    ["系統應用一組","A01053","曾郁凱",],
    ["系統應用三組","A00245","黃致瑋",],
    ["系統應用三組","A01060","陳永航",],
    ["系統應用三組","A01078","曾敬忠",],
    ["系統應用三組","A01203","彭正龍",],
    ["網路儲存系統部","A00275","陳延洛",],
    ["系統架構組","A00200","蘇傳堯",],
    ["系統架構組","A00401","楊道呈",],
    ["軟體專案組","A00279","林信又",],
    ["軟體專案組","A00393","游卓凡",],
    ["軟體專案組","A00435","謝東瀚",],
    ["軟體專案組","A00470","蘇聖詠",],
    ["軟體專案組","A00534","曾進賢",],
    ["軟體專案組","A00667","曹盛淵",],
    ["軟體專案組","A00851","呂惠琪",],
    ["軟體專案組","A01063","蕭仲甫",],
    ["嵌入式應用一組","A00539","李鴻均",],
    ["嵌入式應用一組","A00540","潘睿慈",],
    ["嵌入式應用一組","A00868","毛普臻",],
    ["嵌入式應用一組","A00870","李宗澤",],
    ["嵌入式應用一組","A00971","杜建皓",],
    ["嵌入式應用一組","A01074","鄭家宇",],
    ["嵌入式應用二組","A00391","張鴻致",],
    ["嵌入式應用二組","A00466","李昂熹",],
    ["嵌入式應用二組","A00563","陳鼎文",],
    ["嵌入式應用二組","A00688","張又仁",],
    ["嵌入式應用二組","A00694","張智翔",],
    ["嵌入式應用二組","A01126","王信傑",],
    ["嵌入式應用二組","A01209","許峻銘",],
    ["技術長室","A00024","吳仁智",],
    ["技術長室","A00059","翁舒哲",],
    ["技術長室","A00081","李鎔任",],
    ["技術長室","A00749","黃柏翰",],
    ["技術長室","A00918","高鵬豐",],
    ["技術長室","A01056","張先齊",],
    ["技術長室","A01112","陳俊致",],
    ["智慧影像系統部","A01036","劉誠傑",],
    ["智慧影像系統部","A01037","張朝明",],
    ["智慧影像系統部","A01038","張思默",],
    ["智慧影像系統部","A01104","黃世明",],
    ["智慧影像系統部","A01163","冼召中",],
    ["智慧影像系統部","A90116","鹿崇雯",],
    ["影像光學部","A00406","李傑仁",],
    ["影像光學部","A01052","王啟誠",],
    ["影像品質組","A00394","劉惠芳",],
    ["影像品質組","A00514","周振民",],
    ["影像品質組","A00814","陳志沂",],
    ["影像品質組","A01048","吳炯陞",],
    ["影像品質組","A01076","李文彬",],
    ["影像品質組","A01167","吳珮甄",],
    ["影像品質組","A01171","洪士軒",],
    ["影像系統組","A00425","陳威旭",],
    ["影像系統組","A01017","林準",],
    ["影像系統組","A01064","楊淯任",],
    ["影像演算法一組","A00828","楊明烽",],
    ["影像演算法一組","A01033","李玉傳",],
    ["影像演算法一組","A01047","陳智偉",],
    ["影像演算法一組","A01173","蔡嘉倫",],
    ["影像演算法二組","A00819","陳世軒",],
    ["影像演算法二組","A00856","李知駿",],
    ["影像演算法二組","A01027","劉昭慧",],
    ["機電機構組","A00632","陸龍綿",],
    ["機電機構組","A00855","許祥麟",],
    ["機電機構組","A00940","呂學俊",],
    ["機電機構組","A00966","張元瀚",],
    ["機電電子組","A00450","陳奕全",],
    ["機電電子組","A00816","李文淵",],
    ["機電電子組","A00887","邱奕誌",],
    ["機電電子組","A01055","葉一信",],
    ["機電電子組","A01184","黃崇誠",],
    ["機電電子組","A01196","王敏智",],
    ["研發二處","A00067","陳柏鈞",],
    ["研發二處","A00154","范姜士武",],
    ["研發二處","A00319","周建嘉",],
    ["研發二處","A00659","蕭博文",],
    ["研發二處","A00666","蔡宗澔",],
    ["研發二處","A01105","陳奇平",],
    ["研發二處","A01153","林孍瑄",],
    ["研發二處","A90132","蔡耀德",],
    ["研發三處","A00218","史立山",],
    ["研發三處","A01174","梁鵬旭",],
    ["研發三處","A01185","王志中",],
    ["研發三處","A90098","張智鴻",],
    ["營運處","A01152","陳龍慶",],
    ["資材部","A00512","何錦綾",],
    ["資材部","A00618","于淑君",],
    ["資材部","A01192","林文熙",],
    ["採購組","A00650","賴庭蓁",],
    ["採購組","A00847","蔡采婕",],
    ["採購組","A00985","楊舒媛",],
    ["採購組","A01031","張修齊",],
    ["採購組","A01061","江明芳",],
    ["採購組","A01108","張華軒",],
    ["倉管組","A00029","鄧京倫",],
    ["倉管組","A00123","唐淑娥",],
    ["倉管組","A00184","李世綺",],
    ["倉管組","A00458","吳鴻毅",],
    ["倉管組","A00461","林義政",],
    ["倉管組","A00483","陳瑜融",],
    ["倉管組","A00490","許建豪",],
    ["倉管組","A00764","許峯益",],
    ["倉管組","A00793","穆君寶",],
    ["倉管組","A00808","宋永功",],
    ["倉管組","A00835","陳俊宏",],
    ["倉管組","A01058","陳鴻興",],
    ["生管組","A00411","吳夙弘",],
    ["生管組","A00418","蘇毓涵",],
    ["生管組","A00623","高志仁",],
    ["生管組","A00645","何馥均",],
    ["生管組","A00956","吳東原",],
    ["生管組","A01015","洪苑倫",],
    ["生管組","A01079","葉宣佐",],
    ["生管組","A01172","周聖傑",],
    ["船務組","A00398","黃庚熙",],
    ["船務組","A00599","陳惠玲",],
    ["船務組","A00866","范怡萍",],
    ["物控組","A00477","許鳳慧",],
    ["物控組","A00479","吳佳齡",],
    ["物控組","A00662","陳湧竣",],
    ["物控組","A01014","鍾智羽",],
    ["物控組","A01093","吳偉娜",],
    ["物控組","A01111","許瀅瀅",],
    ["製造工程部","A00073","蕭秀惠",],
    ["製造工程部","A00305","鍾文彬",],
    ["製造工程部","A00344","陳煒慈",],
    ["製造工程部","A00742","王詩晴",],
    ["製造工程部","A90021","胡秀冉",],
    ["工程組","A00195","吳士國",],
    ["工程組","A00362","吳明憲",],
    ["工程組","A00363","徐榮璋",],
    ["工程組","A00740","吳啟旭",],
    ["工程組","A00779","湯邦彥",],
    ["工程組","A00803","曾永男",],
    ["工程組","A00961","翁玉樹",],
    ["工程組","A00967","林鼎崙",],
    ["工程組","A01098","許益源",],
    ["工程組","A01103","吳俊毅",],
    ["工程組","A01107","吳孟霖",],
    ["製造組","A00105","林慧琴",],
    ["製造組","A00118","邱淑華",],
    ["製造組","A00119","陳玉升",],
    ["製造組","A00149","顏秀美",],
    ["製造組","A00205","周惠敏",],
    ["製造組","A00226","牟湘蓁",],
    ["製造組","A00259","羅美櫻",],
    ["製造組","A00306","陳淑娟",],
    ["製造組","A00355","陳招治",],
    ["製造組","A00416","林妤鍹",],
    ["製造組","A00432","程玉瑾",],
    ["製造組","A00451","吳長書",],
    ["製造組","A00487","駱秀容",],
    ["製造組","A00500","胡憶文",],
    ["製造組","A00501","蕭玲真",],
    ["製造組","A00518","張依美",],
    ["製造組","A00523","黃禹彬",],
    ["製造組","A00542","鄭志威",],
    ["製造組","A00550","朱美珍",],
    ["製造組","A00583","蕭智華",],
    ["製造組","A00592","吳靜慧",],
    ["製造組","A00603","張莉珠",],
    ["製造組","A00604","陳蕊芳",],
    ["製造組","A00609","杜美蘭",],
    ["製造組","A00610","廖月蓮",],
    ["製造組","A00624","莊雅嵐",],
    ["製造組","A00648","曹美秀",],
    ["製造組","A00651","王佩慈",],
    ["製造組","A00674","劉偉群",],
    ["製造組","A00676","廖韋宏",],
    ["製造組","A00682","呂素玲",],
    ["製造組","A00683","蕭金蓮",],
    ["製造組","A00706","羅苡瑄",],
    ["製造組","A00716","陳麗因",],
    ["製造組","A00719","王公正",],
    ["製造組","A00720","魏建銘",],
    ["製造組","A00721","黃鈺珊",],
    ["製造組","A00722","楊安琪",],
    ["製造組","A00730","林淑翠",],
    ["製造組","A00732","林鳳珠",],
    ["製造組","A00734","張晏榕",],
    ["製造組","A00738","王琴慧",],
    ["製造組","A00757","葛秀珍",],
    ["製造組","A00759","陳郁靜",],
    ["製造組","A00761","高鄭世玉",],
    ["製造組","A00781","阮玉清",],
    ["製造組","A00794","胡麗芳",],
    ["製造組","A00798","莊詠順",],
    ["製造組","A00799","張文珊",],
    ["製造組","A00805","黃國興",],
    ["製造組","A00821","謝佳燕",],
    ["製造組","A00823","黃卉榛",],
    ["製造組","A00824","程昌莉",],
    ["製造組","A00837","吳青樺",],
    ["製造組","A00838","歐素玲",],
    ["製造組","A00841","蕭彥庭",],
    ["製造組","A00842","鄭惠文",],
    ["製造組","A00858","謝麗滿",],
    ["製造組","A00860","金艷艷",],
    ["製造組","A00862","許惠美",],
    ["製造組","A00863","顧楀齊",],
    ["製造組","A00880","龔啟芳",],
    ["製造組","A00881","林燕萩",],
    ["製造組","A00882","高鈺荃",],
    ["製造組","A00889","林佩真",],
    ["製造組","A00890","林慧慧",],
    ["製造組","A00893","盧常富",],
    ["製造組","A00896","林秋萍",],
    ["製造組","A00910","洪菁霞",],
    ["製造組","A00911","林雅婷",],
    ["製造組","A00913","林云燕",],
    ["製造組","A00921","鄭美蓮",],
    ["製造組","A00924","賴郁琳",],
    ["製造組","A00925","駱名亮",],
    ["製造組","A00937","唐麗琴",],
    ["製造組","A00950","張昌文",],
    ["製造組","A00959","林小英",],
    ["製造組","A00960","林士華",],
    ["製造組","A00962","江秀霞",],
    ["製造組","A00972","郭俊陽",],
    ["製造組","A00973","翁菓蓮",],
    ["製造組","A00975","李春紅",],
    ["製造組","A00977","陳佩君",],
    ["製造組","A00978","楊美慧",],
    ["製造組","A00980","劉柳華",],
    ["製造組","A00981","陳香盈",],
    ["製造組","A00982","廖姿婷",],
    ["製造組","A00989","林恕娟",],
    ["製造組","A00990","何述素",],
    ["製造組","A00991","彭昱璇",],
    ["製造組","A00992","柯儒軒",],
    ["製造組","A00993","呂佳玲",],
    ["製造組","A01003","饒仁豪",],
    ["製造組","A01004","林品均",],
    ["製造組","A01006","潘誼潔",],
    ["製造組","A01007","王顥螢",],
    ["製造組","A01008","牟珈萱",],
    ["製造組","A01009","楊江林",],
    ["製造組","A01020","劉美杏",],
    ["製造組","A01021","陳嘉君",],
    ["製造組","A01039","吳雅慧",],
    ["製造組","A01040","鄭淳文",],
    ["製造組","A01041","佘利君",],
    ["製造組","A01042","葉碧玉",],
    ["製造組","A01043","陳歆筠",],
    ["製造組","A01066","劉家綺",],
    ["製造組","A01067","李曉玲",],
    ["製造組","A01069","游雅婷",],
    ["製造組","A01095","王志中",],
    ["製造組","A01096","王亭雅",],
    ["製造組","A01124","張春燕",],
    ["製造組","A01125","徐文靜",],
    ["製造組","A01130","阮小柒",],
    ["製造組","A01131","林美菁",],
    ["製造組","A01133","黃淑卿",],
    ["製造組","A01134","林凱耀",],
    ["製造組","A01140","顏詩紜",],
    ["製造組","A01143","林彥亨",],
    ["製造組","A01144","曾慶蘭",],
    ["製造組","A01147","邱方又",],
    ["製造組","A01148","林景婷",],
    ["製造組","A01150","張展耀",],
    ["製造組","A01151","郭金煌",],
    ["製造組","A01177","鍾思義",],
    ["製造組","A01178","龍俊憲",],
    ["製造組","A01180","黃久庭",],
    ["製造組","A01187","陳姿均",],
    ["製造組","A01188","高慶璋",],
    ["製造組","A01189","林子傑",],
    ["製造組","A01194","趙少巍",],
    ["製造組","A01195","吳柏璋",],
    ["製程組","A00164","胡增盛",],
    ["製程組","A00365","李修承",],
    ["製程組","A00424","李家瑋",],
    ["製程組","A00748","蕭百成",],
    ["製程組","A00894","郭怡菁",],
    ["製程組","A00931","洪新旻",],
    ["製程組","A00964","陳金龍",],
    ["製程組","A00969","郭光仁",],
    ["製程組","A01117","林庭芳",],
    ["維修組","A00225","蘇嘉濱",],
    ["維修組","A00228","陳克林",],
    ["維修組","A00301","黃彥斌",],
    ["維修組","A00532","鄭友祥",],
    ["維修組","A00888","黃政傑",],
    ["維修組","A00916","莊貽善",],
    ["維修組","A00941","林宗敬",],
    ["品質管理處","A00006","車俊英",],
    ["品保部","A00114","王美芳",],
    ["品保部","A00176","江佩儒",],
    ["文管組","A00079","陳麗芬",],
    ["文管組","A00124","江青慧",],
    ["文管組","A00348","駱文玲",],
    ["文管組","A01046","陳怡靜",],
    ["品質工程組","A00157","廖英傑",],
    ["品質工程組","A00304","蔡雅如",],
    ["品質工程組","A00678","陳姵圻",],
    ["品質工程組","A00679","許智傑",],
    ["品質工程組","A00711","劉嘉玲",],
    ["品質檢驗組","A00098","林欣嫻",],
    ["品質檢驗組","A00127","曾紫淇",],
    ["品質檢驗組","A00188","陳彥君",],
    ["品質檢驗組","A00199","林碧蓮",],
    ["品質檢驗組","A00231","蔡蕎鎂",],
    ["品質檢驗組","A00437","蔡名哲",],
    ["品質檢驗組","A00452","陳冠仲",],
    ["品質檢驗組","A00664","莊秀惠",],
    ["品質檢驗組","A00693","廖芸儀",],
    ["品質檢驗組","A00744","江旭瀅",],
    ["品質檢驗組","A00783","闞維莉",],
    ["品質檢驗組","A00789","曾嘉茹",],
    ["品質檢驗組","A00871","范書碩",],
    ["品質檢驗組","A00886","陳湘羚",],
    ["品質檢驗組","A00995","蕭慈縈",],
    ["品質檢驗組","A01207","邱子芸",],
    ["品質控管組","A00589","吳俊樂",],
    ["品質控管組","A00626","陳勃宇",],
    ["品質控管組","A00670","王嘉瑜",],
    ["品質控管組","A00750","胡永勝",],
    ["品質控管組","A01156","羅偉綸",],
    ["設計驗證部","A00042","黃乃文",],
    ["設計驗證部","A00058","林威成",],
    ["設計驗證部","A00265","許博欽",],
    ["設計驗證部","A00271","蔡瀞儀",],
    ["設計驗證部","A00272","黃志軒",],
    ["驗證四組","A00353","葉緯宸",],
    ["驗證四組","A00597","吳治學",],
    ["驗證四組","A00952","吳怡如",],
    ["驗證四組","A01200","劉孟樺",],
    ["驗證六組","A00136","顏孝虔",],
    ["驗證六組","A00820","陳業淵",],
    ["驗證六組","A00938","楊孟垣",],
    ["驗證六組","A00987","廖柔婷",],
    ["驗證開發組","A00439","賴東賢",],
    ["驗證開發組","A00465","顏志祐",],
    ["驗證開發組","A00726","許維城",],
    ["驗證開發組","A00775","郭詮",],
    ["驗證開發組","A01032","黃國凱",],
    ["驗證開發組","A01191","林軒平",],
    ["驗證開發組","A01197","胡開智",],
    ["驗證一組","A00443","黃建富",],
    ["驗證一組","A00552","林玲金",],
    ["驗證一組","A00697","潘建沅",],
    ["驗證一組","A00708","張子謙",],
    ["驗證一組","A00813","趙冠淵",],
    ["驗證一組","A00914","林思萱",],
    ["驗證一組","A01010","王彥苓",],
    ["驗證一組","A01101","謝淳韜",],
    ["驗證一組","A01106","周志勳",],
    ["驗證二組","A00097","劉家綸",],
    ["驗證二組","A00464","劉麗雅",],
    ["驗證二組","A00774","許嘉文",],
    ["驗證二組","A00817","廖芷婕",],
    ["驗證二組","A01028","羅珮珊",],
    ["驗證二組","A01141","胡毓婷",],
    ["驗證三組","A00588","王銘望",],
    ["驗證三組","A00806","蘇濬嫙",],
    ["驗證三組","A00905","鄭博元",],
    ["驗證三組","A01001","江明潔",],
    ["驗證三組","A01080","程盈璇",],
    ["驗證三組","A01087","曾恕淇",],
    ["驗證五組","A00129","鄭佩庭",],
    ["驗證五組","A00337","趙駿",],
    ["驗證五組","A00354","黃嘉慶",],
    ["驗證五組","A01120","林彥廷",],
    ["技術支援部","A00463","黃志揚",],
    ["維修系統組","A00917","李苡蕎",],
    ["維修系統組","A00954","孫韻芝",],
    ["維修系統組","A01002","李敏鈺",],
    ["維修系統組","A01164","林臆儒",],
    ["應用技術組","A00249","鄭智豪",],
    ["應用技術組","A00671","李峻名",],
    ["應用技術組","A00745","郭柏寬",],
    ["應用技術組","A00948","黃亞奇",],
    ["應用技術組","A00983","林貞誼",],
    ["應用技術組","A01142","邱士恆",],
    ["稽核室","A00699","黃莉婷",],
    ["董事長室","A00001","陳文昌",],
    ["董事長室","A00003","藍志忠",],
    ["董事長室","A00055","廖思鈞",],
    ["董事長室","A00213","劉禹均",],
    ["董事長室","A00492","高語辰",],
    ["董事長室","A00953","朱天羽",],
    ["董事長室","A01018","賈翔誼",],
    ["執行副總經理","A00028","馬仕毅",],
    ["管理處","A00412","左偉莉",],
    ["財務部","A00013","周美茵",],
    ["財務部","A00392","蔡秉芸",],
    ["財務部","A00485","洪秀棻",],
    ["會計部","A00084","邱秀滿",],
    ["會計部","A00170","林葳涵",],
    ["會計部","A00446","李世傑",],
    ["會計部","A00619","方少琬",],
    ["會計部","A00746","吳凌雲",],
    ["會計部","A01050","沈宏霖",],
    ["會計部","A01186","李振菁",],
    ["資訊部","A00692","黃政清",],
    ["資訊部","A00767","陳栯羚",],
    ["資訊部","A00810","陳君彥",],
    ["資訊部","A00875","陳世崟",],
    ["網路系統管理組","A00635","張晴凱",],
    ["網路系統管理組","A00756","劉啟新",],
    ["資訊系統管理組","A00544","李威慶",],
    ["資訊系統管理組","A01206","黃建榮",],
    ["總務部","A00122","劉國忠",],
    ["總務部","A00325","陳怡蓉",],
    ["總務部","A01016","陳芷蕎",],
    ["總務部","A01045","鄭弘昌",],
    ["總務部","A90025","林素櫻",],
    ["人力資源部","A00163","周玓宇",],
    ["人力資源部","A00631","林家榮",],
    ["人力資源部","A00818","林亞璇",],
    ["人力資源部","A00955","林小琪",],
    ["人力資源部","A01113","陳雯娟",],
    ["國際事業處","A00047","顧中威",],
    ["策略採購部","A01089","陳育琮",],
    ["策略採購部","A01119","范志賓",],
    ["策略採購部","A01127","陳姿蘭",],
    ["策略採購部","A01128","張雅瑜",],
    ["策略採購部","A01129","邱俊超",],
    ["策略採購部","A01159","黃千玲",],
    ["非洲中東組","A00553","楊進汶",],
    ["非洲中東組","A00572","郭家彰",],
    ["非洲中東組","A01084","吳永偉",],
    ["亞洲一組","A00958","鄭承孟",],
    ["亞洲一組","A01051","盧顯",],
    ["亞洲二組","A00681","尉遲炘",],
    ["亞洲二組","A00723","景怡齡",],
    ["亞洲二組","A01092","金娳婷",],
    ["亞洲二組","A01193","吳韋志",],
    ["拉美組","A00491","江志穎",],
    ["拉美組","A00559","陳威安",],
    ["拉美組","A00919","林明洲",],
    ["拉美組","A01137","莎拉",],
    ["行銷企劃部","A00230","程香綺",],
    ["行銷企劃部","A00920","王懷璐",],
    ["通路行銷組","A00598","詹尹甄",],
    ["通路行銷組","A00612","張家瑋",],
    ["通路行銷組","A00852","朱怡君",],
    ["通路行銷組","A00904","林璧圓",],
    ["通路行銷組","A01065","許孟傑",],
    ["媒體設計組","A00242","李泰鑫",],
    ["媒體設計組","A00253","邱世偉",],
    ["媒體設計組","A00580","黃健嘉",],
    ["媒體設計組","A00607","盧譽才",],
    ["媒體設計組","A01100","丘湘琳",],
    ["媒體設計組","A01204","李青蔚",],
    ["產品管理部","A00698","李慧玉",],
    ["產品管理部","A00714","周若茵",],
    ["產品管理部","A00728","徐步鯤",],
    ["產品管理部","A01109","陳明宗",],
    ["產品規劃組","A00227","曾淑鈴",],
    ["產品規劃組","A00407","張凱鈞",],
    ["產品規劃組","A00999","顧殷如",],
    ["產品規劃組","A01019","劉嘉偉",],
    ["專案管理組","A00622","邱顯婷",],
    ["專案管理組","A00629","任霞",],
    ["專案管理組","A00782","陳芳儀",],
    ["專案管理組","A00800","徐婉婷",],
    ["專案管理組","A01025","陳錦堂",],
    ["專案管理組","A01121","簡欣雯",],
    ["方案規劃組","A00790","張洋榕",],
    ["方案規劃組","A00945","巫芳萍",],
    ["方案規劃組","A00998","宋佩穗",],
    ["方案規劃組","A01123","孫柏青",],
    ["國際專案部","A00246","廖邦廷",],
    ["國際專案部","A00256","林政緯",],
    ["國際專案部","A00390","劉信宏",],
    ["國際專案部","A00703","許騰元",],
    ["國際專案部","A00791","陳志達",],
    ["國際專案部","A00965","蔡沛任",],
    ["國際專案部","A01082","周韋宏",],
    ["國際專案部","A01083","鄧維侖",],
    ["國際專案部","A01160","方娜拉",],
    ["歐洲業務部","A00415","柯素梅",],
    ["歐洲業務部","A00834","柯玫君",],
    ["歐洲一組","A00537","林鈺庭",],
    ["歐洲一組","A01110","雷路加",],
    ["歐洲一組","A01176","石逸凡",],
    ["歐洲二組","A00804","鄧琮寶",],
    ["歐洲二組","A01102","迪雅哥",],
    ["歐洲二組","A01165","傅惠德",],
    ["歐洲事業處","A00143","吳文貴",],
    ["歐洲專案部","A00101","侯志星",],
    ["歐洲專案部","A00947","郭政錦",],
    ["歐洲專案部","A00986","吳元鈞",],
    ["歐洲專案部","A01059","楊沛雯",],
    ["行銷企劃處","A01085","蘇建群",],
    ["國際業務一部","A00312","王芊云",],
    ["國際業務一部","A00420","陳之皇",],
    ["國際業務一部","A01175","劉威辰",],
    ["國際業務二部","A00274","連怡瑩",],
    ["國際業務二部","A00386","羅亦鎧",],
    ["國際業務二部","A00413","黃俐敏",],
    ["國際業務二部","A01136","鄭翊如",],
    ["代工事業處","A00019","廖禎祺",],
    ["代工事業處","A00171","楊秀慧",],
    ["代工事業處","A00909","劉佳玲",],
    ["專案技術部","A00207","張為棟",],
    ["專案技術部","A00575","吳采澄",],
    ["專案技術部","A00968","張庭嬡",],
    ["代工業務一部","A00133","陳殷康",],
    ["代工業務一部","A00273","張建文",],
    ["代工業務一部","A00429","陸怡璇",],
    ["代工業務一部","A00480","林若文",],
    ["代工業務一部","A00753","莊宗蓉",],
    ["代工業務一部","A00899","江欣庭",],
    ["代工業務一部","A01035","王芷宜",],
    ["代工業務一部","A01135","藍立穎",],
    ["代工業務二部","A00266","胡詔祥",],
    ["代工業務二部","A00321","張美娟",],
    ["代工業務二部","A00402","馮麗萍",],
    ["代工業務二部","A00448","劉怡伶",],
    ["代工業務二部","A00533","葉珈瑄",],
    ["代工業務二部","A00884","廖瑞雯",],
    ["代工業務二部","A00944","謝欣如",],
    ["研發一處","A00049","鄭聖夫",],
    ["研發一處","A00147","廖彥鈞",],
    ["研發一處","A01199","程意慈",],
    ["系統整合部","A00189","梁琬珮",],
    ["系統整合部","A00255","張永伸",],
    ["系統整合一組","A00531","林子翔",],
    ["系統整合一組","A00620","郭依青",],
    ["系統整合一組","A00680","鄭俊誠",],
    ["系統整合一組","A00850","謝國爗",],
    ["系統整合一組","A00901","許博豪",],
    ["系統整合一組","A01168","許文耀",],
    ["系統整合二組","A00202","陳聖元",],
    ["系統整合二組","A00395","蔡界平",],
    ["系統整合二組","A00556","曾志豪",],
    ["系統整合二組","A00558","王雅萱",],
    ["系統整合二組","A00787","陳尹凡",],
    ["系統整合二組","A00827","林祐綱",],
    ["系統整合二組","A01201","林冠宇",],
    ["系統整合三組","A00197","郭曜銘",],
    ["系統整合三組","A00248","張千威",],
    ["系統整合三組","A00517","葉再傳",],
    ["系統整合三組","A00826","吳思穎",],
    ["系統整合三組","A00957","洪健二",],
    ["系統整合三組","A01062","葉耕成",],
    ["系統整合三組","A01198","唐怡君",],
    ["系統整合四組","A00349","陳琮凱",],
    ["系統整合四組","A00460","羅明遠",],
    ["系統整合四組","A00701","阮昱勳",],
    ["系統整合四組","A00849","周元超",],
    ["系統整合四組","A00876","羅輯",],
    ["系統整合四組","A01190","方建平",],
    ["軟體開發部","A00264","郭騰凱",],
    ["軟體開發部","A01091","張哲維",],
    ["應用軟體組","A00316","鄭欽議",],
    ["應用軟體組","A00915","巫冠忠",],
    ["應用軟體組","A01054","朱明初",],
    ["應用軟體組","A01086","褚立陽",],
    ["軟體品質保證組","A00339","蔡銘鴻",],
    ["軟體品質保證組","A00830","林雍舜",],
    ["軟體品質保證組","A01024","孫玉萍",],
    ["軟體平台組","A00379","管健男",],
    ["軟體平台組","A00414","陳思翰",],
    ["軟體平台組","A00668","李昆擇",],
    ["軟體平台組","A00709","徐斌峰",],
    ["軟體平台組","A00867","林佩嫺",],
    ["使用者經驗組","A00561","劉倩雯",],
    ["使用者經驗組","A00717","林彥甫",],
    ["使用者經驗組","A00869","施以萱",],
    ["使用者經驗組","A00946","陳麒元",],
    ["使用者經驗組","A01099","鄭世暉",],
    ["使用者經驗組","A01166","莊鎧賸",],
    ["行動應用組","A00310","許倫維",],
    ["行動應用組","A00545","卓晉緯",],
    ["行動應用組","A01183","陸凱暉",],
    ["硬體開發部","A00175","蔡詒安",],
    ["硬體開發部","A00421","姬文洲",],
    ["安規暨線路佈局組","A00087","張瓊文",],
    ["安規暨線路佈局組","A00240","鄭育仁",],
    ["安規暨線路佈局組","A00270","高櫻珍",],
    ["安規暨線路佈局組","A00427","高嘉珮",],
    ["安規暨線路佈局組","A00560","周仁傑",],
    ["硬體一組","A00262","張定家",],
    ["硬體一組","A00433","蔡子揚",],
    ["硬體一組","A00441","陳興志",],
    ["硬體一組","A00468","林佳慶",],
    ["硬體一組","A00696","姚嘉祺",],
    ["硬體一組","A01182","洪煜喬",],
    ["硬體二組","A00535","黃彥傑",],
    ["硬體二組","A00568","陳俊仰",],
    ["硬體二組","A00695","張育齊",],
    ["硬體二組","A01011","吳俊義",],
    ["硬體二組","A01161","周維駿",],
    ["機構開發部","A00381","許志回",],
    ["機構開發部","A00399","黃玉嬌",],
    ["機構一組","A00400","陳泗興",],
    ["機構一組","A00570","林志鴻",],
    ["機構一組","A00617","詹智傑",],
    ["機構一組","A00689","黃尚宇",],
    ["機構一組","A00739","陳志豪",],
    ["機構一組","A00951","陳青青",],
    ["機構一組","A01030","黃尚豪",],
    ["機構二組","A00102","黃聖鑌",],
    ["機構二組","A00467","黃仲雍",],
    ["機構二組","A00528","蔡瓊緯",],
    ["機構二組","A00718","王俊英",],
    ["機構二組","A00773","游章充",],
    ["機構二組","A01114","張紡慈",],
    ["專案開發部","A00144","陳志彬",],
    ["專案開發部","A90069","簡韶逸",],
    ["通訊協定組","A00258","郭任傑",],
    ["通訊協定組","A00311","郭嘉明",],
    ["通訊協定組","A00729","吳柏庚",],
    ["通訊協定組","A00877","楊凱閔",],
    ["通訊協定組","A00949","駱文城",],
    ["通訊協定組","A01115","陳祖頤",],
    ["通訊協定組","A01169","黃敬文",],
    ["通訊協定組","A01170","吳華軒",],
    ["通訊協定組","A01205","彭脩舜",],
    ["系統應用二組","A00315","鐘逸民",],
    ["系統應用二組","A00751","林建成",],
    ["系統應用二組","A00970","陳彥璋",],
    ["系統應用二組","A01013","徐健峰",],
    ["系統應用二組","A01155","郭俊麒",],
    ["系統應用二組","A01208","游舜勛",],
    ["系統應用一組","A00388","陳志強",],
    ["系統應用一組","A00715","蔡宜蓁",],
    ["系統應用一組","A01023","楊善雯",],
    ["系統應用一組","A01053","曾郁凱",],
    ["系統應用三組","A00245","黃致瑋",],
    ["系統應用三組","A01060","陳永航",],
    ["系統應用三組","A01078","曾敬忠",],
    ["系統應用三組","A01203","彭正龍",],
    ["網路儲存系統部","A00275","陳延洛",],
    ["系統架構組","A00200","蘇傳堯",],
    ["系統架構組","A00401","楊道呈",],
    ["軟體專案組","A00279","林信又",],
    ["軟體專案組","A00393","游卓凡",],
    ["軟體專案組","A00435","謝東瀚",],
    ["軟體專案組","A00470","蘇聖詠",],
    ["軟體專案組","A00534","曾進賢",],
    ["軟體專案組","A00667","曹盛淵",],
    ["軟體專案組","A00851","呂惠琪",],
    ["軟體專案組","A01063","蕭仲甫",],
    ["嵌入式應用一組","A00539","李鴻均",],
    ["嵌入式應用一組","A00540","潘睿慈",],
    ["嵌入式應用一組","A00868","毛普臻",],
    ["嵌入式應用一組","A00870","李宗澤",],
    ["嵌入式應用一組","A00971","杜建皓",],
    ["嵌入式應用一組","A01074","鄭家宇",],
    ["嵌入式應用二組","A00391","張鴻致",],
    ["嵌入式應用二組","A00466","李昂熹",],
    ["嵌入式應用二組","A00563","陳鼎文",],
    ["嵌入式應用二組","A00688","張又仁",],
    ["嵌入式應用二組","A00694","張智翔",],
    ["嵌入式應用二組","A01126","王信傑",],
    ["嵌入式應用二組","A01209","許峻銘",],
    ["技術長室","A00024","吳仁智",],
    ["技術長室","A00059","翁舒哲",],
    ["技術長室","A00081","李鎔任",],
    ["技術長室","A00749","黃柏翰",],
    ["技術長室","A00918","高鵬豐",],
    ["技術長室","A01056","張先齊",],
    ["技術長室","A01112","陳俊致",],
    ["智慧影像系統部","A01036","劉誠傑",],
    ["智慧影像系統部","A01037","張朝明",],
    ["智慧影像系統部","A01038","張思默",],
    ["智慧影像系統部","A01104","黃世明",],
    ["智慧影像系統部","A01163","冼召中",],
    ["智慧影像系統部","A90116","鹿崇雯",],
    ["影像光學部","A00406","李傑仁",],
    ["影像光學部","A01052","王啟誠",],
    ["影像品質組","A00394","劉惠芳",],
    ["影像品質組","A00514","周振民",],
    ["影像品質組","A00814","陳志沂",],
    ["影像品質組","A01048","吳炯陞",],
    ["影像品質組","A01076","李文彬",],
    ["影像品質組","A01167","吳珮甄",],
    ["影像品質組","A01171","洪士軒",],
    ["影像系統組","A00425","陳威旭",],
    ["影像系統組","A01017","林準",],
    ["影像系統組","A01064","楊淯任",],
    ["影像演算法一組","A00828","楊明烽",],
    ["影像演算法一組","A01033","李玉傳",],
    ["影像演算法一組","A01047","陳智偉",],
    ["影像演算法一組","A01173","蔡嘉倫",],
    ["影像演算法二組","A00819","陳世軒",],
    ["影像演算法二組","A00856","李知駿",],
    ["影像演算法二組","A01027","劉昭慧",],
    ["機電機構組","A00632","陸龍綿",],
    ["機電機構組","A00855","許祥麟",],
    ["機電機構組","A00940","呂學俊",],
    ["機電機構組","A00966","張元瀚",],
    ["機電電子組","A00450","陳奕全",],
    ["機電電子組","A00816","李文淵",],
    ["機電電子組","A00887","邱奕誌",],
    ["機電電子組","A01055","葉一信",],
    ["機電電子組","A01184","黃崇誠",],
    ["機電電子組","A01196","王敏智",],
    ["研發二處","A00067","陳柏鈞",],
    ["研發二處","A00154","范姜士武",],
    ["研發二處","A00319","周建嘉",],
    ["研發二處","A00659","蕭博文",],
    ["研發二處","A00666","蔡宗澔",],
    ["研發二處","A01105","陳奇平",],
    ["研發二處","A01153","林孍瑄",],
    ["研發二處","A90132","蔡耀德",],
    ["研發三處","A00218","史立山",],
    ["研發三處","A01174","梁鵬旭",],
    ["研發三處","A01185","王志中",],
    ["研發三處","A90098","張智鴻",],
    ["營運處","A01152","陳龍慶",],
    ["資材部","A00512","何錦綾",],
    ["資材部","A00618","于淑君",],
    ["資材部","A01192","林文熙",],
    ["採購組","A00650","賴庭蓁",],
    ["採購組","A00847","蔡采婕",],
    ["採購組","A00985","楊舒媛",],
    ["採購組","A01031","張修齊",],
    ["採購組","A01061","江明芳",],
    ["採購組","A01108","張華軒",],
    ["倉管組","A00029","鄧京倫",],
    ["倉管組","A00123","唐淑娥",],
    ["倉管組","A00184","李世綺",],
    ["倉管組","A00458","吳鴻毅",],
    ["倉管組","A00461","林義政",],
    ["倉管組","A00483","陳瑜融",],
    ["倉管組","A00490","許建豪",],
    ["倉管組","A00764","許峯益",],
    ["倉管組","A00793","穆君寶",],
    ["倉管組","A00808","宋永功",],
    ["倉管組","A00835","陳俊宏",],
    ["倉管組","A01058","陳鴻興",],
    ["生管組","A00411","吳夙弘",],
    ["生管組","A00418","蘇毓涵",],
    ["生管組","A00623","高志仁",],
    ["生管組","A00645","何馥均",],
    ["生管組","A00956","吳東原",],
    ["生管組","A01015","洪苑倫",],
    ["生管組","A01079","葉宣佐",],
    ["生管組","A01172","周聖傑",],
    ["船務組","A00398","黃庚熙",],
    ["船務組","A00599","陳惠玲",],
    ["船務組","A00866","范怡萍",],
    ["物控組","A00477","許鳳慧",],
    ["物控組","A00479","吳佳齡",],
    ["物控組","A00662","陳湧竣",],
    ["物控組","A01014","鍾智羽",],
    ["物控組","A01093","吳偉娜",],
    ["物控組","A01111","許瀅瀅",],
    ["製造工程部","A00073","蕭秀惠",],
    ["製造工程部","A00305","鍾文彬",],
    ["製造工程部","A00344","陳煒慈",],
    ["製造工程部","A00742","王詩晴",],
    ["製造工程部","A90021","胡秀冉",],
    ["工程組","A00195","吳士國",],
    ["工程組","A00362","吳明憲",],
    ["工程組","A00363","徐榮璋",],
    ["工程組","A00740","吳啟旭",],
    ["工程組","A00779","湯邦彥",],
    ["工程組","A00803","曾永男",],
    ["工程組","A00961","翁玉樹",],
    ["工程組","A00967","林鼎崙",],
    ["工程組","A01098","許益源",],
    ["工程組","A01103","吳俊毅",],
    ["工程組","A01107","吳孟霖",],
    ["製造組","A00105","林慧琴",],
    ["製造組","A00118","邱淑華",],
    ["製造組","A00119","陳玉升",],
    ["製造組","A00149","顏秀美",],
    ["製造組","A00205","周惠敏",],
    ["製造組","A00226","牟湘蓁",],
    ["製造組","A00259","羅美櫻",],
    ["製造組","A00306","陳淑娟",],
    ["製造組","A00355","陳招治",],
    ["製造組","A00416","林妤鍹",],
    ["製造組","A00432","程玉瑾",],
    ["製造組","A00451","吳長書",],
    ["製造組","A00487","駱秀容",],
    ["製造組","A00500","胡憶文",],
    ["製造組","A00501","蕭玲真",],
    ["製造組","A00518","張依美",],
    ["製造組","A00523","黃禹彬",],
    ["製造組","A00542","鄭志威",],
    ["製造組","A00550","朱美珍",],
    ["製造組","A00583","蕭智華",],
    ["製造組","A00592","吳靜慧",],
    ["製造組","A00603","張莉珠",],
    ["製造組","A00604","陳蕊芳",],
    ["製造組","A00609","杜美蘭",],
    ["製造組","A00610","廖月蓮",],
    ["製造組","A00624","莊雅嵐",],
    ["製造組","A00648","曹美秀",],
    ["製造組","A00651","王佩慈",],
    ["製造組","A00674","劉偉群",],
    ["製造組","A00676","廖韋宏",],
    ["製造組","A00682","呂素玲",],
    ["製造組","A00683","蕭金蓮",],
    ["製造組","A00706","羅苡瑄",],
    ["製造組","A00716","陳麗因",],
    ["製造組","A00719","王公正",],
    ["製造組","A00720","魏建銘",],
    ["製造組","A00721","黃鈺珊",],
    ["製造組","A00722","楊安琪",],
    ["製造組","A00730","林淑翠",],
    ["製造組","A00732","林鳳珠",],
    ["製造組","A00734","張晏榕",],
    ["製造組","A00738","王琴慧",],
    ["製造組","A00757","葛秀珍",],
    ["製造組","A00759","陳郁靜",],
    ["製造組","A00761","高鄭世玉",],
    ["製造組","A00781","阮玉清",],
    ["製造組","A00794","胡麗芳",],
    ["製造組","A00798","莊詠順",],
    ["製造組","A00799","張文珊",],
    ["製造組","A00805","黃國興",],
    ["製造組","A00821","謝佳燕",],
    ["製造組","A00823","黃卉榛",],
    ["製造組","A00824","程昌莉",],
    ["製造組","A00837","吳青樺",],
    ["製造組","A00838","歐素玲",],
    ["製造組","A00841","蕭彥庭",],
    ["製造組","A00842","鄭惠文",],
    ["製造組","A00858","謝麗滿",],
    ["製造組","A00860","金艷艷",],
    ["製造組","A00862","許惠美",],
    ["製造組","A00863","顧楀齊",],
    ["製造組","A00880","龔啟芳",],
    ["製造組","A00881","林燕萩",],
    ["製造組","A00882","高鈺荃",],
    ["製造組","A00889","林佩真",],
    ["製造組","A00890","林慧慧",],
    ["製造組","A00893","盧常富",],
    ["製造組","A00896","林秋萍",],
    ["製造組","A00910","洪菁霞",],
    ["製造組","A00911","林雅婷",],
    ["製造組","A00913","林云燕",],
    ["製造組","A00921","鄭美蓮",],
    ["製造組","A00924","賴郁琳",],
    ["製造組","A00925","駱名亮",],
    ["製造組","A00937","唐麗琴",],
    ["製造組","A00950","張昌文",],
    ["製造組","A00959","林小英",],
    ["製造組","A00960","林士華",],
    ["製造組","A00962","江秀霞",],
    ["製造組","A00972","郭俊陽",],
    ["製造組","A00973","翁菓蓮",],
    ["製造組","A00975","李春紅",],
    ["製造組","A00977","陳佩君",],
    ["製造組","A00978","楊美慧",],
    ["製造組","A00980","劉柳華",],
    ["製造組","A00981","陳香盈",],
    ["製造組","A00982","廖姿婷",],
    ["製造組","A00989","林恕娟",],
    ["製造組","A00990","何述素",],
    ["製造組","A00991","彭昱璇",],
    ["製造組","A00992","柯儒軒",],
    ["製造組","A00993","呂佳玲",],
    ["製造組","A01003","饒仁豪",],
    ["製造組","A01004","林品均",],
    ["製造組","A01006","潘誼潔",],
    ["製造組","A01007","王顥螢",],
    ["製造組","A01008","牟珈萱",],
    ["製造組","A01009","楊江林",],
    ["製造組","A01020","劉美杏",],
    ["製造組","A01021","陳嘉君",],
    ["製造組","A01039","吳雅慧",],
    ["製造組","A01040","鄭淳文",],
    ["製造組","A01041","佘利君",],
    ["製造組","A01042","葉碧玉",],
    ["製造組","A01043","陳歆筠",],
    ["製造組","A01066","劉家綺",],
    ["製造組","A01067","李曉玲",],
    ["製造組","A01069","游雅婷",],
    ["製造組","A01095","王志中",],
    ["製造組","A01096","王亭雅",],
    ["製造組","A01124","張春燕",],
    ["製造組","A01125","徐文靜",],
    ["製造組","A01130","阮小柒",],
    ["製造組","A01131","林美菁",],
    ["製造組","A01133","黃淑卿",],
    ["製造組","A01134","林凱耀",],
    ["製造組","A01140","顏詩紜",],
    ["製造組","A01143","林彥亨",],
    ["製造組","A01144","曾慶蘭",],
    ["製造組","A01147","邱方又",],
    ["製造組","A01148","林景婷",],
    ["製造組","A01150","張展耀",],
    ["製造組","A01151","郭金煌",],
    ["製造組","A01177","鍾思義",],
    ["製造組","A01178","龍俊憲",],
    ["製造組","A01180","黃久庭",],
    ["製造組","A01187","陳姿均",],
    ["製造組","A01188","高慶璋",],
    ["製造組","A01189","林子傑",],
    ["製造組","A01194","趙少巍",],
    ["製造組","A01195","吳柏璋",],
    ["製程組","A00164","胡增盛",],
    ["製程組","A00365","李修承",],
    ["製程組","A00424","李家瑋",],
    ["製程組","A00748","蕭百成",],
    ["製程組","A00894","郭怡菁",],
    ["製程組","A00931","洪新旻",],
    ["製程組","A00964","陳金龍",],
    ["製程組","A00969","郭光仁",],
    ["製程組","A01117","林庭芳",],
    ["維修組","A00225","蘇嘉濱",],
    ["維修組","A00228","陳克林",],
    ["維修組","A00301","黃彥斌",],
    ["維修組","A00532","鄭友祥",],
    ["維修組","A00888","黃政傑",],
    ["維修組","A00916","莊貽善",],
    ["維修組","A00941","林宗敬",],
    ["品質管理處","A00006","車俊英",],
    ["品保部","A00114","王美芳",],
    ["品保部","A00176","江佩儒",],
    ["文管組","A00079","陳麗芬",],
    ["文管組","A00124","江青慧",],
    ["文管組","A00348","駱文玲",],
    ["文管組","A01046","陳怡靜",],
    ["品質工程組","A00157","廖英傑",],
    ["品質工程組","A00304","蔡雅如",],
    ["品質工程組","A00678","陳姵圻",],
    ["品質工程組","A00679","許智傑",],
    ["品質工程組","A00711","劉嘉玲",],
    ["品質檢驗組","A00098","林欣嫻",],
    ["品質檢驗組","A00127","曾紫淇",],
    ["品質檢驗組","A00188","陳彥君",],
    ["品質檢驗組","A00199","林碧蓮",],
    ["品質檢驗組","A00231","蔡蕎鎂",],
    ["品質檢驗組","A00437","蔡名哲",],
    ["品質檢驗組","A00452","陳冠仲",],
    ["品質檢驗組","A00664","莊秀惠",],
    ["品質檢驗組","A00693","廖芸儀",],
    ["品質檢驗組","A00744","江旭瀅",],
    ["品質檢驗組","A00783","闞維莉",],
    ["品質檢驗組","A00789","曾嘉茹",],
    ["品質檢驗組","A00871","范書碩",],
    ["品質檢驗組","A00886","陳湘羚",],
    ["品質檢驗組","A00995","蕭慈縈",],
    ["品質檢驗組","A01207","邱子芸",],
    ["品質控管組","A00589","吳俊樂",],
    ["品質控管組","A00626","陳勃宇",],
    ["品質控管組","A00670","王嘉瑜",],
    ["品質控管組","A00750","胡永勝",],
    ["品質控管組","A01156","羅偉綸",],
    ["設計驗證部","A00042","黃乃文",],
    ["設計驗證部","A00058","林威成",],
    ["設計驗證部","A00265","許博欽",],
    ["設計驗證部","A00271","蔡瀞儀",],
    ["設計驗證部","A00272","黃志軒",],
    ["驗證四組","A00353","葉緯宸",],
    ["驗證四組","A00597","吳治學",],
    ["驗證四組","A00952","吳怡如",],
    ["驗證四組","A01200","劉孟樺",],
    ["驗證六組","A00136","顏孝虔",],
    ["驗證六組","A00820","陳業淵",],
    ["驗證六組","A00938","楊孟垣",],
    ["驗證六組","A00987","廖柔婷",],
    ["驗證開發組","A00439","賴東賢",],
    ["驗證開發組","A00465","顏志祐",],
    ["驗證開發組","A00726","許維城",],
    ["驗證開發組","A00775","郭詮",],
    ["驗證開發組","A01032","黃國凱",],
    ["驗證開發組","A01191","林軒平",],
    ["驗證開發組","A01197","胡開智",],
    ["驗證一組","A00443","黃建富",],
    ["驗證一組","A00552","林玲金",],
    ["驗證一組","A00697","潘建沅",],
    ["驗證一組","A00708","張子謙",],
    ["驗證一組","A00813","趙冠淵",],
    ["驗證一組","A00914","林思萱",],
    ["驗證一組","A01010","王彥苓",],
    ["驗證一組","A01101","謝淳韜",],
    ["驗證一組","A01106","周志勳",],
    ["驗證二組","A00097","劉家綸",],
    ["驗證二組","A00464","劉麗雅",],
    ["驗證二組","A00774","許嘉文",],
    ["驗證二組","A00817","廖芷婕",],
    ["驗證二組","A01028","羅珮珊",],
    ["驗證二組","A01141","胡毓婷",],
    ["驗證三組","A00588","王銘望",],
    ["驗證三組","A00806","蘇濬嫙",],
    ["驗證三組","A00905","鄭博元",],
    ["驗證三組","A01001","江明潔",],
    ["驗證三組","A01080","程盈璇",],
    ["驗證三組","A01087","曾恕淇",],
    ["驗證五組","A00129","鄭佩庭",],
    ["驗證五組","A00337","趙駿",],
    ["驗證五組","A00354","黃嘉慶",],
    ["驗證五組","A01120","林彥廷",],
    ["技術支援部","A00463","黃志揚",],
    ["維修系統組","A00917","李苡蕎",],
    ["維修系統組","A00954","孫韻芝",],
    ["維修系統組","A01002","李敏鈺",],
    ["維修系統組","A01164","林臆儒",],
    ["應用技術組","A00249","鄭智豪",],
    ["應用技術組","A00671","李峻名",],
    ["應用技術組","A00745","郭柏寬",],
    ["應用技術組","A00948","黃亞奇",],
    ["應用技術組","A00983","林貞誼",],
    ["應用技術組","A01142","邱士恆",]
]

name_in_groups = {}

for name in vvtk_name_list:
    if name[0] not in name_in_groups:
        name_in_groups[name[0]] = [name[1:]]
    else:
        name_in_groups[name[0]].append(name[1:])

print name_in_groups
pprint(name_in_groups)
pdb.set_trace()