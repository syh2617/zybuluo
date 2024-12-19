斌头老师

前言

[TOC]

`@bintou`
`2022-09-27 19:17:46`
`字数 4178`
`阅读 2144`


CINTA课的碎碎念
==========

`CINTA` `算法`

2022年CINTA授课笔记
==============

2022年9月
-------

### GF乘法及求逆元操作

定义集合，即所有8比特长的二进制串集合。定义集合上的加法、乘法如下：   

- 加法等同于异或，即任取，。   

- 乘法只定义乘2的运算。任取，如果的最高比特为0，则(左移一个比特)。如果的最高比特为1，则，也就是说，左移一个比特之后再异或一个八比特的十六进制值。当然，。[提示，因为，由此可以得到中任意值的乘法，回顾一下Simple-Mul的过程。]

大家的任务：   

- 写一个程序GF\_mul（C或者Python）完成任意中元素的乘法。   

- 思考这样一个问题，集合的非零元素会有乘法逆元吗？即，任取，且 ，是否一定存在使得？   

- 如果我告诉你们答案，以上的问题答案是肯定的，如何求任意元素的乘法逆元？请写一个程序GF\_inverse完成这个任务。[提示，还是从egcd算法出发，关键点在于，你们要思考，什么是除法。]

[参考答案.](https://crypto.stackexchange.com/questions/12956/multiplicative-inverse-in-operatornamegf28) 暂时别泄露给20级 :-)

### LeetCode上加减乘除相关题目

* [Power of 2](https://leetcode.com/problems/power-of-two/)
* [加法题](https://leetcode.com/problems/sum-of-two-integers/)
* [除法题](https://leetcode.com/problems/divide-two-integers/)
* [完全平方数](https://leetcode.com/problems/valid-perfect-square/)
* [x的n次方](https://leetcode.com/problems/powx-n/description/)

### 关于算术基本算法的好资料

[The Aggregate Magic Algorithms](http://aggregate.org/MAGIC/)

2022年7-8月
---------

### 欧拉公式

* [斌头老师教你记住欧拉公式](https://www.zybuluo.com/bintou/note/2309274)

### 两题思考题（20220714）

* n个元素分成两个非空子集，有多少种分法？Why？
* 定义n元素的Cycle（圈）如下，比如，四个元素，A B C D 形成一个圈，B C D A也是圈，但是这两圈我们认为是同一个圈。但是，A C D B就是另一个圈了。请问，n个元素会形成多少个不同的n元素圈？

---

2021年CINTA课授课笔记
===============

### 模指数运算

模指数算法的复杂性、内涵远比我们想象的要多很多，有兴趣的同学可以浏览以下链接：   

- [Efficient modular exponentiation algorithms](https://eli.thegreenplace.net/2009/03/28/efficient-modular-exponentiation-algorithms)   

- [ModPow](https://www.codeproject.com/Tips/791253/ModPow)

### 第一次作业相关

* 除法定理的证明

### 七月的课前训练

#### Modular Subset Product Problem （选做题，比较难）

Given a list of primes, e.g., from 2 to nth prime, denoted as , and an integer  and a prime . To find a  bits vector , such that:

#### Your works

* Write a Sage (Python) program to solve the MSP problem. For example, we let the parameters ,  and .
* Anaylize the efficience of your progrm, and try to improve.
* What is the relation between Subset Sum Problem(SSP) and Subset Product Problem?
* How hard is the MSP problem? Give a postulate, and prove. (I don't think you can do it.)

以下是历史遗留内容。
----------

### 第二周.Binary egcd的正确性分析

[![](https://i.imgur.com/QKgnJpZ.png)   

]   

大家如果阅读这个bianry egcd算法有问题，应该大多都出现在repeat里面的那两个while，特别是s和t不能同时被2整除的时候。都被2整除，大家应该能懂。

要理解这里，关键点还是我常强调的，别想太多，动笔算一算！

其次，大家有没有注意到那两个变量和在整个算法过程中都不变？这里就是我CINTA书里面强调的：和只是占位符，并不直接参与计算。那这里为什么出现了和？

说到这里，我们回想一下egcd在做什么？一直在保持 这一类型等式的成立。所以，和不变。现在要除2，等式的左边要干啥？保持平衡啊！怎么才平衡，凑数！比如：   

   

但是，或不能同时被2整除时，失败！   

于是，想到(怎么想到的，算法里面不是这样做的吗？哈哈哈...)   

   

变形得到   



问题是，你怎么确保和一定被2整除？   

这里其实我也没想到更好的说明办法，那就分情况讨论嘛。   

1、a和b同为奇数时；因为r为偶数，所以，s和t必须同为偶数或者奇数。可得！   

2、a为奇数，b为偶数时；因为r为偶数，所以，这里我偷个懒，大家自己分析。

其他都比较容易。但是复杂性分析还是不容易的。有同学说，与gcd算法一样，其实不一样。为什么？注意那个repeat主循环，每次迭代r和r'只是做一次减法，注意，这里真是减法，不是gcd里面的mod运算。所以gcd分析里面每一次减半的结论其实是没有了！怎么办呢？

这是另一个版本的[Binary-GCD算法](https://perso.ens-lyon.fr/damien.stehle/BINARY.html)。

### 第三周. 关于作业的几个问题

作业错得很离谱，错得很典型。基本功缺失严重。

改作业两点意见：第一，不接受任何的MD文件和Html文件。如果你扔个pdf、c或者jpg，我还能看到，稍可忍受，MD文件、Html文件我怎么看啊？统统打回。第二就是不懂MarkDown的同学太多。打回。

大部分同学需要补一下大一的这一课：[计算思维训练简要指南](https://www.jianshu.com/p/fc258c7b341d)。

### 第三周--关于乘法逆元的三个问题

第一个问题就要问：求乘法逆元输入什么，输出什么？返回一个void型，这能对吗？

第二，gcd和egcd有什么共同点。既然计算了egcd还需要gcd吗？

第三，egcd的输出是什么？它的输出就是乘法逆元？

### 国庆假期--关于努力

关于努力，应该有不少同学会说，我会努力的！我也相信大多数同学内心确实也是努力的！相信我。只是，相信归相信，还是靠事实说话。

我在课堂派出了两道所谓的扩展练习作业。其实根本不是难题，也不是什么扩展作业，就是基本作业里面抽出来，命名为扩展作业而已。出题至今大概两周了吧？提交答案的只有区区的2人次。

大学不是中学，没有什么超纲不超纲，没有什么上纲上线。学习无上限！我不会因此就说大家不努力。但是我坚信这个事实说明了很多问题。什么问题，你们自己说吧。

以后不会有所谓的扩展练习就是了。

### 国庆假期的思考题

题目：对任意正整数，数列，设。请问最大的是什么？为什么？

提示：首先编程算，找规律。找到规律之后就硬算。利用了Bezout定理。

我刚从一本书里看到的，看了解答，不很繁琐，就是硬做，所以，感觉没什么意思。

### 原根定理

对任意素数，是循环群，且存在个生成元（原根）。

### 欧拉函数的一种性质

给定任意正整数，的所有因子分别记为，其中包括和。记函数：   

   

现在需要证明。为完成这个任务，请依次完成以下小任务：   

- 证明，对任意素数，。

* 证明，对任意素数，。
* 证明，对任意素数，，是任意正整数。
* 证明，对任意素数和，。
* 证明函数是积性函数，即对任意的正整数和，如果，则。提示：既然与互素，则它们之间就不存在大于一的公因子，那么它们的因子相乘之后作用于欧拉函数会满足什么特性？
* 最后，完成证明的任务。提示：任意整数都是素数的乘积，即。

### 作业一例

答案：因为是的子群，根据拉格朗日定理，的阶整除的阶，即，是一个整数。又因为是的真子群，所以，，所以。

### 思考题

#### 思考题一

设群的阶是，是素数。请证明，如果不是循环群，即不存在阶元素，那么必然存在阶的元素，而且也必然存在阶的元素。

#### 思考题二

定义商群，再定义映射，是定值（一个正整数）。请问这是不是良定义映射，为什么？

### 好消息

这个学期我们讲过整数乘法的算法，复杂度是，2019年已经有人提出了[复杂度为O(n log n)的算法](https://rjlipton.wordpress.com/2019/03/29/integer-multiplication-in-nlogn-time/)，这里有[文章](https://hal.archives-ouvertes.fr/hal-02070778v2)。 目前大家当然是看不懂了，我也没有看，估计也看不懂。只是报告这个消息给大家，让大家注意，这些看上去简单的算法持续有人在研究。

之前GMP使用的是基于FFT的Schönhage–Strassen algorithm，那篇博客里面也说到了。复杂度是O( n log n (log log n)) 。

### 题解

任取环中的元素，都满足，请证明环是交换环。   

证明（以下是一个错误的证明，请找出错误）：   

根据假设有。所以有：   

   

同理，   

   

整理可得：   

   

所以，是交换环。

### 考试题解

这是2019级CINTA考试中唯一一道不出现在课堂与作业的“难题”，答对率极低，其实客观说，也不难。

> 题目Z是整数环。请证明环 2Z 不与环 3Z 同构。（8分）

#### 答案

> 设是从到 的环同构，则 (请注意，是环，有两种操作 )。所以有   
> 
>    
> 
> 记为，是某整数（因为中的元素就是3的倍数。）。所以有   
> 
>    
> 
> 因此，有，不是一个整数。矛盾！



---


`@bintou`
`2015-10-17 05:48:32`
`字数 666`
`阅读 2517`


CS核心专业教材
========

`CS` `书单`

---

精选这一系列教材的理由：   

1、讲述内容具学科核心地位，即为其他课程奠定基础，内容相对自包含，具有相对长的时效性，同时也是该学科最难的理论知识。   

2、思想性与阅读性俱强。   

3、均属著名教材，容易购买或者获取。

---

1、微积分，James Stewart   

2、线性代数导论[MIT]，G. Strang，<http://web.mit.edu/18.06/www/index.shtml>   

3、概率与计算，Michael Mitzenmacher   

4、算法导论，CLRS   

5、深入理解计算机系统，CSAPP   

6、计算机程序的构造与解释，SICP   

7、A practical introduction to computer architecture，Daniel Page   

8、计算理论导引，ITOC，M. Sipser   

9、计算复杂性，Sanjeev Arora，Boaz Barak （也许不是好的选择！但是目前还没有更好的选择.）   

10、具体数学，GKP   

11、代数，Michael Artin   

12、数论概论 (FINT)，J.H. Silverman

---

13、编译原理：技术与工具 （Dragon Book）   

14、Logic in Computer Science：modelling and reasoning about systems，Michael Huth and Mark Ryan，好书！   

15、Modern Computer Algebra，Gathen, Joachim Von Zur/ Gerhard, Jurgen/ Von Zur Gathen, Joachim 出版社: Cambridge Univ Pr



---


`@bintou`
`2019-10-09 06:17:33`
`字数 2051`
`阅读 2058`


CSI讲义13-- 计算思维训练简要指南
====================

`CSI`

---

计算思维不是自然形成，而是特别训练的产物。以下简要给出一些建议，围绕这些建议可以进行相关训练。新生只需要关注第一和第二阶段，所以，第三阶段我还没写。或者说，因为我还没写，所以大家可以先关注第一、第二阶段。

第一阶段： 面向问题
----------

计算机专业新生的第一阶段任务就是要强调“面向问题”的思维。把“发现问题、分析问题、解决问题”优先放在你任何思考当中。

### 1. 面向数据的思维

考虑一个独立的“问题”，首先问两个问题：

* 输入什么？
* 输出什么？

也就是说，在提出问题的初期，把关注点放在数据（Data）上，关注于问题的I/O（输入/输出）。进一步，需要关注数据的表达：长度、类型等。

> 例子. 给定一个整数n，求n的阶乘。输入是整数n，输出也是一个整数。进一步问，这个整数有多大？这个函数大概长这个模样。

```


1. \* Input: integer n
2. * Output: integer res, where res = n*(n-1)...2*1
3. *\
4. int factorial(int n){
5. ......
6. return res;
8. }

```

请注意，你可以不知道这个问题怎么解决，但千万不可不知道你的问题是什么！不知道问题是什么，下一步所谓“解决问题”就免谈。而清楚知道自己的问题，将有助于问题的解决。

以下是常见错误，请大家体会，并尽量避免！为什么我说它错？请问，你的输出是什么？输出就是打印出结果啊！真的是这样吗？

```


1. void factorial(int n){
2. ......
3. printf("哈哈哈，你的答案是：%d.\n", res);
4. }

```

另外一个错误，这是一个求a的x次方的程序。源自真实的作业提交。

```


1. int pow(int a, int x, int n) {
2. if(n == 0||a ==0 || x <= 0) {
3. printf("输入数据错误：/n");
4. exit(1);
5. //以下省略。。。
6. }

```

请回答我，为什么我认为这是错误？

> 习题. 给出以下问题的输入输出分析，并写出函数的雏形。   
> 
> 1. 判断一个整数n是否素数；   
> 
> 2. 求两个整数的最大公因子；

在初学的早期就必须关注这些问题，准确并自觉地应用函数这个概念。千万别到了大二还不能准确写一个函数出来！！！

### 2. 结构化方法

所谓结构化的方法，即面向特定问题，把该问题“自顶向下”地分解为更小的问题，通过解决小问题来解决大问题。

> 例子. 编程验证哥德巴赫猜想，即任意大于2的偶数都是两个素数的和。   
> 
> 子问题：整数加法、判断素数、判断两个整数相等......

### 3. 与程序设计语言结合的训练

自觉在编程程序的时候体现以上两种思维。当你接到一个编程任务，首先问输入/输出，其次考虑数据类型，再思考解决这个问题需要分解为解决什么子问题。即，所谓的“结构化编程”。

现在的教学强调“面向对象编程”（OOP），请注意，OOP并不会对冲结构化，它们各司其职，而结构化方法在专业学习初期必须更加强调。

### 4. 问题解决后需要问的三个问题

“面向问题”的思维中，解决问题并非最后一步，因为，“解决完”一个问题我们还需要针对解决问题的方法问三个问题（问题系列）：

* 正确性. 该方法是否正确？为什么？如何证明？
* 效率. 该方法解决问题的效率如何评估？
* 优化. 该方法是否最优方案？如果不是，怎么样改进？如果是，如何证明？

> 例子. 插入排序的效率？快速排序的效率？如何证明？Theta(n log n)是否最优效率？
> 
> 例子. 寻找峰值. [这篇博客](https://www.jianshu.com/p/53c8dcf25b2f)具体展示了以上思想的每一个步骤，可惜阅读者甚少。

第二阶段：面向方法
---------

计算思维当然不是一成不变的，然而经过一个世纪的发展，到目前已经形成一系列得到广泛认同的方法学。这些方法学当中，某些针对程序（自动化问题求解）的“数据结构”，某些则是特定的思维模式。

### 数据结构

数据结构分为两类：初级与高级。不要被“高级”、“初级“这两个看上去有高低评价的字眼迷惑。它们不可以相互替代，各司其职，分别有其特殊的用途。

### 初级数据结构

* 数组：
* 链表：
* 栈：先进后出
* 队列：先进先出

#### 高级数据结构

* 树(二叉树、B树、红黑树)
* 堆
* 图

### 特定的方法

具体内容参考[《算法导论》](https://www.jianshu.com/p/b3e03375fb7c)，请尽快进入“算法”的学习。

#### 1. 暴力求解

计算机的优势是高速，这使得暴力求解往往成为可行的方法。我想提醒的是，无论“暴力求解”这个名字多粗暴，看上去有多“幼稚”，在面向问题的第一时刻请首先想起“暴力”，任何时候！方法就是方法，也许暴力法无法解决很多问题，但它永远是思维的第一步。许多低年级的同学没有经过暴力法的洗礼，盲目追求所谓的“高级”方法，往往得不偿失，失去了训练自己的最好时机。

另外，暴力法也往往是给其他高级方法带来启发。只有明白暴力法无效的本质，才有可能去发现更高效的方法。

> 例子. 给定一个整数n，判断其是否素数。暴力求解应该如何做？问题：为什么我们需要比暴力法更高效的方法？
> 
> 例子. [求两个整数的最大公因子](https://www.jianshu.com/p/9682136c9361)。 给出算法描述，如何证明其正确性？其效率是什么？是否最优？如何改进？

#### 2. 分治法

* 二分搜索
* 归并排序
* 快速排序

继续强推这关于[分治法的小博客](https://www.jianshu.com/p/53c8dcf25b2f)，以实例带动思维。

#### 3. 贪心法

* 哈夫曼编码

#### 4. 动态规划

* 背包问题

#### 5. 线性规划

-

第三阶段 面向代数的特定结构
--------------

### 向量空间

### 代数结构

### 代数几何



---


`@bintou`
`2019-09-24 20:08:52`
`字数 3764`
`阅读 1722`


CSI讲义1--二进制及其相关操作
=================

`CSI` `二进制`

---

> 本文为非常规的《计算机科学导论》课程讲义，适用于大一新生。初学者可能会觉得有点难。最好是不要畏难，跟上思路。相信没有那么难。--斌头老师

![CSI](http://upload-images.jianshu.io/upload_images/52389-3d7885a39ca2a4e8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1080/q/50)

计算机专业学什么？
---------

从计算机科学的本质开讲。学“计算机科学”到底是学什么？本质上，Computer Science不是学计算机，不是学计算机的使用也不是学计算机的制造。学的是“计算”-- Computation。

通常，大家进入这个专业多数是因误解而来，从今天开始，也许需要换一下思维了。这也就是我为什么一直推荐How to Think like a Computer Scientist（HTCS）而不是其他比如C++ Primer之类的书为入门书的原因。关键不在于是否学会编程，而是要如何改变思维。

那到底**什么是计算**？这个问题很复杂，然后具体落实到计算机的实现上却又非常简单。这是两个问题。第一，什么是计算？这个暂时还回答不了。第二是，怎么计算。这个可以有一个简单的初始到答案：**二进制**。

**“世界上有10种人，一种懂二进制，一种不懂！”**你们是其中的第一种。改变思维的第一步，就是认识二进制。

二进制的定义及运算规则
-----------

*注：本章内容并不涉及负数，即统统考虑无符号数。*

首先我们给出二进制数字的描述。

```
二进制：只有0和1两位数字，每一位我们称为一个bit（比特）。
计算规则：0+0 = 0，0+1 = 1，1+1 = 10，10+1 = 11

```

现在可以归纳一下规律了。   

0，1，10，11，...，1111，...， 这样的数字有没有遍历完所有的我们之前认识的十进制正整数？答案是，yes！然后，我们还知道，二进制加法无非就是“逢二进一”。

十进制数无非就是偶数和奇数两种。请问，偶数在二进制中长什么样子？答：最后一个bit为0 。

于是我们有以下规则：

```
0结尾的二进制数是偶数；1结尾的二进制数是奇数。

```

例子：

```
 2对应10，4，对应100，8对应1000，16对应10000

```

大家有没有看到10后面加个0等于是乘二？好像我们可以得出一个规律: **在一个二进制数后面补一个零等于乘二**？

一般来说，没接触过二进制的同学在回答上面这个问题的的时候基本都是说：“No！”因为这里如果考虑奇数，那么，很可能不对！但是，乘二不是在后面补零？末尾为零不就是偶数？这......有什么不对呢？

例子：

```
 十进制7 ＝＝ 二进制 111
 7*2 == 14 == 二进制 1110

```

似乎是这么个理？再演算一下其他数字......得到**乘法**规则如下：

```
二进制乘2运算等于在数字末尾补一个0.

```

思考一下，乘法是补0，除法呢？我们只考虑整除，即只取整数商。

例子：

```
十进制7的二进制为111，十进制7/2 == 十进制3 == 二进制 11
十进制11的二进制为1011，十进制11/2 == 十进制5 == 二进制101

```

**除法**规律：

```
二进制除2运算等于在砍掉数字末尾一个数位。

```

如何把任何的二进制数转换为十进制？这是下一节的内容。

**补充练习**：

```
给定一个整数v，如何判断v是否2的某次方（Power of 2）？
比如，v = 4 = 2^2，返回True；v = 9 并非2的次方，返回False。
请写一个C语言的函数来实现。

```

二进制的逻辑操作
--------

### 与或非

### 异或

### 移位

二进制加法
-----

二进制数转换为十进制数
-----------

归纳一下之前的内容。首先，计算机科学是关于“**计算**”的科学，是关于“思维”的科学。然后，介绍了二进制，当然是非正式地介绍，为的是归纳出两个规则：在后补零等于乘2（扩展思考，除2怎么做？）；尾数为0的数是偶数（尾数为1的是奇数）。现在，我们需要思考的是如何在二进制数与十进制数之间进行转换。特别是，我们不要满足于怎么做，还要思考为什么。更重要的是，我们想得到一个“过程”：一个计算机可以读懂的过程。

当我们思考一个过程的时候，首要必须确定的是：**输入什么，输出什么**。比如，我们命名将二进制转换为十进制的过程为B2D，这只是一个名字。

例子：

```
function B2D(a)
输入：一个二进制数a
输出：a所代表的十进制数

```

在完全描述出这个程序之前，我们先计算一些实例出来，比如：

例子：

> 输入0，立即输出0；输入1立即输出1！这太简单，但是请注意，这很重要！

考虑多比特输入。比如：

> 输入：1110；输出：1110代表的十进制（记为Res）。根据之前的规则，补零等于乘2，所以，**这个数必然是`111`表示的十进制数乘2**！！！所以，我们的计算结果就是2\*B2D(111)。

但是，如果是奇数呢？比如，输入1111 。Ok，没关系，我们照样可以得到结果：`2*B2D(111) + 1` ，多加个1就好了。

所以，我们可以完成我们的程序描述了：   

注意：＃代表注释！

```
function B2D(a)
#输入：一个二进制数a 
#输出：a所代表的十进制数
if a < = 1:      #程序的终止条件
    return a;    #即，当a小于等于1，原样输出.
else:             #否则
    return 2*B2D(a/2) + lsb(a)  #lsb(x)指的返回x的最后一个比特.

```

请注意一点，我们现在只有二进制数操作的两个规则：乘2等于补零；0为偶数，1为奇数。上面这个程序违反规则了没？有啊，怎么能用除法“/”？其实，这里的除法就是把a的最后一个比特删除。而lsb(a)指的是a的最后一个比特。

这个程序中最古怪之处是：`2*B2D(a/2) + lsb(a)`。因为，这里B2D这个程序自己调用了自己！！！我们把这种自己调用自己的过程称为“**递归**”。

**所有计算无非递归而已！所有的思维都是递归的！**

> 作业：用C语言实现以上程序中的“除2”运算及lsb过程。

十进制数转换为二进制数
-----------

现在反过来，如果要从十进制得到二进制应该如何？通常，我们的课程会像这样教，如下图：

![十进制转换为二进制](http://upload-images.jianshu.io/upload_images/52389-b4d8db14342f8777.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我们当然不能满足于知道这个方法，要多问一句，为什么？好，重新来，思维运动起来！现在我们要写一个名字为“D2B”的程序，输入一个十进制数，输出一个二进制数。

```
 function D2B(a)
 输入：一个十进制数a
 输出：a所代表的二进制数

```

思路如下：   

首先，我们需要得到程序的终止条件。如果 a< = 1，怎么样？输出a！然后，计算无非递归，递归起来！比如，7这个数，我们能知道它最后一个比特是什么吗？奇数，当然是1 。如果是16呢？偶数，当然是0 。就是说，对任意输入，我们至少知道了部分答案，a的最后一个比特。剩下的比特who care？交给递归啊！我们得到D2B(a')＋lsb(a)，其中a'是a删除最后一比特之后的数。呃，忘记了，a是十进制数呢？没事，除法嘛，除2。

程序：

```
function D2B(a)
# Input, a decimal number a;
# Output, the binary number of a;
if a <= 1:  ＃终止条件！
    return a;
else:
    return D2B(a/2)||lsb(a)

```

`D2B(a) = D2B(a/2) || b` ，这样的过程为什么会结束？也许很多同学立即会担心，递归怎么会结束呢？

为什么递归会终止？因为每一个递归程序都有一个终止条件。而且，每次自己调用自己的时候，参数都在减小（这很重要），这就确保了终止条件一定会到达。

递归效率低？我的回答是：思维，不在乎效率；其次，递归并不总是低效率。相信提这个问题的同学学过一些，但是，对递归的理解不能那么片面。以后继续深入。

```
作业题：用C语言编程实现以下过程。
function fac(n)
输入：整数n
输出：n的阶乘
要求：必须使用递归

```

最后一个内容，这是世界上最有意思的问题之一。话说有两只兔子......

```
作业：斐波那契数列：1 1 2 3 5 8 13 21...... 请用C语言用递归的方法写出第n项斐波那契数。
function fib(n)
输入：整数n
输出：第n项斐波那契数
要求：必须使用递归

```

二进制数的乘法
-------

计算机的核心是CPU，我们总是希望这些个核心设备做尽可能少的“操作”，但是借助它又似乎无所不能。这似乎矛盾，其实又不矛盾。上面讲到二进制的加法和乘2。然后讲到用递归的方法去思考。

接下来，先延续上面的思路，出一道题，实现二进制数的乘法：

```
function multiply(a,b)
输入: a和b，两个任意长的二进制数；
输出：a*b 。
要求：请用递归的方法，并且只能用加法和乘2操作来完成，不要写程序，用我昨天的描述方法即可。

```

建立、改变思维方式应该放第一位，请不要小看这些似乎没用的东西。

例子：

```
11*1 ＝11；11＊0 ＝＝0；
11 * 10 ＝＝110，实际就是11乘2，即11后面补个0；
如果是11 * 11？当然应该是11*10 ＋11*1，即11*(10 + 01)。
推广到任意比特的乘法：x * y ＝ 2*multipy(x, y/2) ＋ x 。这里看明白了吗？递归！

```

代码：

```
function multiply(a,b)
if b ＝＝ 0：
    return 0;
if b == 1:
    return a;
if is_even(b): # the last bit of b is 0;
    return 2*multiply(a, b/2);
else:         # b is odd    
    return 2*multiply(a, b/2) + a;

```

这个乘法算法展示，计算机只要乘2和加法就可以做任何乘法，对吗？但是，我们怎么不讲除法和减法呢？下回分解。

```
练习：
用C语言编程实现is_even()和is_odd() 函数。
is_even()，如果输入为偶数，返回True，否则返回False。
is_odd判断输入是否奇数。

作业: 用C语言编程实现两个整数的乘法。
要求，不能用递归！

```

2019-09-24整理



---


`@bintou`
`2018-10-22 19:36:08`
`字数 792`
`阅读 1834`


浮点数陷阱
=====

`C语言` `CSI` `浮点数` `陷阱`

---

### 运行以下程序，解释为什么。

```


1. #include <stdio.h>
2. int main()
3. {
4. double i, endFlag = 10.0;
6. for(i = 9.0; i != endFlag; i += 0.1) {
7. printf("i = %.11f\n", i);
8. if(i > endFlag){
9. printf("Overflow. i = %.11f\n", i);
10. break;
11. }
12. }
14. i = 9.9;
15. i += 0.1;
16. printf("i = %.11f\n", i);
17. if(endFlag != i)
18. printf("They are not equal!\n");
19. else
20. printf("They are the same!\n");
22. return 0;
23. }

```
### 类似的程序，只是改变了精度，我们看到了什么？ 再运行看看？

```


1. #include <stdio.h>
2. int main()
3. {
4. double i, endFlag = 10.0;
6. for(i = 9.0; i != endFlag; i += 0.1){
7. printf("i = %.50lf\n", i);
8. if(i > endFlag){
9. printf("Overflow. i = %.50lf\n", i);
10. break;
11. }
12. }
14. i = 9.9;
15. printf("i = %.50f\n", i);
16. i += 0.1;
17. printf("i + 0.1 = %.50f\n", i);
18. printf("endFlag = %.50f\n", endFlag);
19. if(endFlag != i)
20. printf("They are not equal!\n");
21. else
22. printf("They are the same!\n");
24. return 0;
25. }

```
### 怎么办？使用精度控制，在以上代码中增加以下代码。再看看？

```


1. #define PRECISION 0.0000000000001
2. for (i = 0; !(i < 10 + PRECISION && i > 10 - PRECISION); i += 0.1){
3. printf("%.12lf\n", i);
4. }

```

---


`@bintou`
`2017-12-01 05:04:14`
`字数 786`
`阅读 1987`


Linked list
===========

`CSI` `Source` `Code`

---

```


1. #include <stdio.h>
2. #include <stdlib.h>
3. typedef struct _slist_t{
4. int data;
5. struct _slist_t *next;
6. } slist_t;
8. // This function prints contents of linked list starting from head
9. void printList(slist_t *node)
10. {
11. while (node != NULL)
12. {
13. printf(" %d ", node->data);
14. node = node->next;
15. }
16. printf("\n");
17. }
19. int main()
20. {
22. slist_t *list = NULL, *visitor; //empty list;
23. slist_t *new_node = (slist_t*)malloc(sizeof(slist_t));
24. new_node->data = 2017;
25. new_node->next = NULL;
27. //insert in list
28. list = new_node;
29. new_node = (slist_t*)malloc(sizeof(slist_t));
30. new_node->data = 2018;
31. new_node->next = NULL;
33. //insert in head
34. new_node->next = list;
35. list = new_node;
37. //Run through the list. We write this to warn you sth...
38. visitor = list;
39. int i = 0;
40. while (visitor != NULL){
41. printf("The %d th member is %d.\n", i++, visitor->data);
42. visitor = visitor->next;
43. }
45. //Print the list using a function.
46. printList(list);
48. return 0;
49. }

```

---


`@bintou`
`2018-10-03 17:54:10`
`字数 3122`
`阅读 2566`


CSI第七章查找与排序
===========

`CSI` `源代码`

---

### Binary Search

```


1. #include <stdio.h>
3. // A recursive binary search function. It returns location of x in
4. // given array arr[l..r] is present, otherwise -1
5. int binarySearch(int arr[], int l, int r, int x)
6. {
7. if (r >= l)
8. {
9. int mid = l + (r - l)/2;
11. // If the element is present at the middle itself
12. if (arr[mid] == x)  return mid;
14. // If element is smaller than mid, then it can only be present
15. // in left subarray
16. if (arr[mid] > x) return binarySearch(arr, l, mid-1, x);
18. // Else the element can only be present in right subarray
19. return binarySearch(arr, mid+1, r, x);
20. }
22. // We reach here when element is not present in array
23. return -1;
24. }
26. int ite_binarySearch(int* array, int size, int key)
27. {
28. int left = 0, right = size, mid = -1;
29. while(left <= right)
30. {
31. mid = (left + right)/2;
32. if(array[mid] == key)
33. return mid;
34. if(array[mid] < key)
35. left = mid + 1;
36. else
37. right = mid - 1;
38. }
39. return -1;
40. }
42. int main(void)
43. {
44. int arr[] = {2, 3, 4, 10, 40};
45. int n = sizeof(arr)/ sizeof(arr[0]);
46. int x = 10;
47. int result = binarySearch(arr, 0, n-1, x);
48. (result == -1)? printf("Element is not present in array")
49. : printf("Element is present at index %d", result);
50. return 0;
51. }

```
### Insertion sort

> 算法思路：   
> 
> // 对大小为n的数组arr[]进行升序排序（从小到大）   
> 
> insertionSort(arr, n)   
> 
> for i = 1 to n-1:   
> 
> Pick element arr[i] and insert it into sorted sequence arr[0…i-1]

```


1. /* Function to sort an array using insertion sort*/
2. void insertionSort(int arr[], int n)
3. {
4. int i, key, j;
5. for (i = 1; i < n; i++)
6. {
7. key = arr[i];//当前需要插入的元素.
8. j = i-1;
10. /* Move elements of arr[0..i-1], that are
11. greater than key, to one position ahead
12. of their current position */
13. while (j >= 0 && arr[j] > key)
14. {
15. arr[j+1] = arr[j];
16. j = j-1;
17. }
18. arr[j+1] = key;
19. }
20. }

```
### Selection Sort

> 算法思路：   
> 
> 不断选择“未排序”数组中最小的元素，并把它放在数组的开头.

```


1. void selectionSort(int arr[], int n)
2. {
3. int i, j, min_idx;
5. // One by one move boundary of unsorted subarray
6. for (i = 0; i < n-1; i++)
7. {
8. // Find the minimum element in unsorted array
9. min_idx = i;
10. for (j = i+1; j < n; j++)
11. if (arr[j] < arr[min_idx])
12. min_idx = j;
14. // Swap the found minimum element with the first element
15. swap(&arr[min_idx], &arr[i]);
16. }
17. }

```
### Bubble Sort

> 算法思路：   
> 
> Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

```


1. /* A function to implement bubble sort */
2. void bubbleSort(int arr[], int n)
3. {
4. int i, j;
5. for (i = 0; i < n-1; i++)
7. // Last i elements are already in place
8. for (j = 0; j < n-i-1; j++)
9. if (arr[j] > arr[j+1])
10. swap(&arr[j], &arr[j+1]);
11. }

```
### Quick Sort

> 算法思路：   
> 
> 1、选择一个主元；   
> 
> 2、根据主元，将数组分成两部分：比主元小的部分和比主元大的部分；   
> 
> 3、递归地，分别对两个部分进行Quick Sort。

```


1. /* This function takes last element as pivot, places
2. the pivot element at its correct position in sorted
3. array, and places all smaller (smaller than pivot)
4. to left of pivot and all greater elements to right
5. of pivot */
7. int partition (int arr[], int low, int high)
8. {
9. int pivot = arr[high];    // pivot
10. int i = (low - 1);  // Index of smaller element
12. for (int j = low; j <= high - 1; j++)
13. {
14. // If current element is smaller than or
15. // equal to pivot
16. if (arr[j] <= pivot)
17. {
18. i++;    // increment index of smaller element
19. swap(&arr[i], &arr[j]);
20. }
21. }
22. swap(&arr[i + 1], &arr[high]);
23. return (i + 1);
24. }
26. //另一种Partition
27. int partition( int arr[], int low, int high) {
28. int pivot = arr[low], i = low, j = high + 1;
30. while( 1)
31. {
32. do ++i; while( arr[i] <= pivot && i <= high );
33. do --j; while( arr[j] > pivot );
34. if( i >= j ) break;
35. swap(&arr[i], &arr[j]);
36. }
37. swap(&arr[low], &arr[j]);
38. return j;
39. }
41. /* The main function that implements QuickSort
42. arr[] --> Array to be sorted,
43. low  --> Starting index,
44. high  --> Ending index */
45. void quickSort(int arr[], int low, int high)
46. {
47. if (low < high)
48. {
49. /* pi is partitioning index, arr[p] is now
50. at right place */
51. int pi = partition(arr, low, high);
53. // Separately sort elements before
54. // partition and after partition
55. quickSort(arr, low, pi - 1);
56. quickSort(arr, pi + 1, high);
57. }
58. }

```

[参考资料](http://www.geeksforgeeks.org/)



---


`@bintou`
`2017-11-16 06:43:01`
`字数 540`
`阅读 1822`


CSI第六章作业
========

`CSI` `实例` `汇编代码`

---

### 题目

> 用Pep/8汇编语言写满足这样功能的程序：键盘输入一个整数n，求1+2+...+ n的结果，并输出最终结果。

### 答案示例

```


1. ;答案不唯一，仅供参考
2. BR main; 跳过数据定义进入主程序
3. sum: .WORD   0x0000 ; 最终结果初始值为0
4. num: .BLOCK 2 ; Set up a two byte block for input value
5. ;以上为数据定义
6. main: DECI num, d ; 输入一个正整数
7. loop:  LDA num, d
8. ADDA sum, d
9. STA sum, d ; 以上三行完成sum = sum + num
10. LDA num, d
11. SUBA 1, i
12. STA num, d; 以上完成 num--
13. CPA 0, i; num与0比较
14. BREQ quit; goto quit if num equals 0
15. BR loop; repeat loop
16. quit:  DECO sum, d; output sum
17. STOP
18. .END

```
### 作业点评

> 存在以下问题：   
> 
> - 对变量的定义概念含糊。   
> 
> - 对程序运行的流程不够清晰，主要体现在死板地参考其他题的答案，又不能灵活地运用到新的程序中。   
> 
> - 缺乏学习主动性。   
> 
> - 胆子太小，轻易被稍微难（陌生）一点的知识点吓跑。

### 思考题

这里的答案给出一个用两个变量实现的例子，请问能否只用一个变量就可以完成计算？如果可以，应该如何做？如果不行，为什么？



---


`@bintou`
`2017-12-09 05:49:40`
`字数 1469`
`阅读 1862`


图的定义及BFS
========

`Source` `Code`

---

> C++代码.

```


1. // Program to print BFS traversal from a given
2. // source vertex. BFS(int s) traverses vertices
3. // reachable from s.
4. #include<iostream>
5. #include <list>
7. using namespace std;
9. // This class represents a directed graph using
10. // adjacency list representation
11. class Graph
12. {
13. int V;    // No. of vertices
15. // Pointer to an array containing adjacency
16. // lists
17. list<int> *adj;
18. public:
19. Graph(int V);  // Constructor
21. // function to add an edge to graph
22. void addEdge(int v, int w);
24. // prints BFS traversal from a given source s
25. void BFS(int s);
26. };
28. Graph::Graph(int V)
29. {
30. this->V = V;
31. adj = new list<int>[V];
32. }
34. void Graph::addEdge(int v, int w)
35. {
36. adj[v].push_back(w); // Add w to v’s list.
37. }
39. void Graph::BFS(int s)
40. {
41. // Mark all the vertices as not visited
42. bool *visited = new bool[V];
43. for(int i = 0; i < V; i++)
44. visited[i] = false;
46. // Create a queue for BFS
47. list<int> queue;
49. // Mark the current node as visited and enqueue it
50. visited[s] = true;
51. queue.push_back(s);
53. // 'i' will be used to get all adjacent
54. // vertices of a vertex
55. list<int>::iterator i;
57. while(!queue.empty())
58. {
59. // Dequeue a vertex from queue and print it
60. s = queue.front();
61. cout << s << " ";
62. queue.pop_front();
64. // Get all adjacent vertices of the dequeued
65. // vertex s. If a adjacent has not been visited,
66. // then mark it visited and enqueue it
67. for (i = adj[s].begin(); i != adj[s].end(); ++i)
68. {
69. if (!visited[*i])
70. {
71. visited[*i] = true;
72. queue.push_back(*i);
73. }
74. }
75. }
76. }
78. // Driver program to test methods of graph class
79. int main()
80. {
81. // Create a graph given in the above diagram
82. Graph g(4);
83. g.addEdge(0, 1);
84. g.addEdge(0, 2);
85. g.addEdge(1, 2);
86. g.addEdge(2, 0);
87. g.addEdge(2, 3);
88. g.addEdge(3, 3);
90. cout << "Following is Breadth First Traversal "
91. << "(starting from vertex 2) \n";
92. g.BFS(2);
93. cout << "\n";
94. return 0;
95. }

```

---


`@bintou`
`2017-12-08 07:00:58`
`字数 7097`
`阅读 1871`


Binary Search Tree
==================

`Source` `Code`

---

> 本程序用于展示BST的基本操作，特别是使用Stack的遍历方法，让初学者建立直观。适合大一新生阅读。C语言为主。附加了一个Python代码，感觉Python代码非常简洁，个人非常喜欢，就推荐推荐。

### BST操作

```


1. // C program to demonstrate delete operation in binary search tree
2. #include<stdio.h>
3. #include<stdlib.h>
4. #include<stack.h>
6. // A utility function to create a new BST node
7. struct node *newNode(int item)
8. {
9. struct node *temp =  (struct node *)malloc(sizeof(struct node));
10. temp->key = item;
11. temp->left = temp->right = NULL;
12. return temp;
13. }
15. // A utility function to do inorder traversal of BST
16. void inorder(struct node *root)
17. {
18. if (root != NULL)
19. {
20. inorder(root->left);
21. printf("%d ", root->key);
22. inorder(root->right);
23. }
24. }
26. /* A utility function to insert a new node with given key in BST */
27. struct node* insert(struct node* node, int key)
28. {
29. /* If the tree is empty, return a new node */
30. if (node == NULL) return newNode(key);
32. /* Otherwise, recur down the tree */
33. if (key < node->key)
34. node->left  = insert(node->left, key);
35. else
36. node->right = insert(node->right, key);
38. /* return the (unchanged) node pointer */
39. return node;
40. }
42. /* Given a non-empty binary search tree, return the node with minimum
43. key value found in that tree. Note that the entire tree does not
44. need to be searched. */
45. struct node *minValueNode(struct node *node)
46. {
47. struct node* current = node;
49. /* loop down to find the leftmost leaf */
50. while (current->left != NULL)
51. current = current->left;
53. return current;
54. }
56. /* Given a binary search tree and a key, this function deletes the key
57. and returns the new root */
58. struct node *deleteNode(struct node *root, int key)
59. {
60. // base case
61. if (root == NULL) return root;
63. // If the key to be deleted is smaller than the root's key,
64. // then it lies in left subtree
65. if (key < root->key)
66. root->left = deleteNode(root->left, key);
68. // If the key to be deleted is greater than the root's key,
69. // then it lies in right subtree
70. else if (key > root->key)
71. root->right = deleteNode(root->right, key);
73. // if key is same as root's key, then This is the node
74. // to be deleted
75. else
76. {
77. // node with only one child or no child
78. if (root->left == NULL)
79. {
80. struct node *temp = root->right;
81. free(root);
82. return temp;
83. }
84. else if (root->right == NULL)
85. {
86. struct node *temp = root->left;
87. free(root);
88. return temp;
89. }
91. // node with two children: Get the inorder successor (smallest
92. // in the right subtree)
93. struct node* temp = minValueNode(root->right);
95. // Copy the inorder successor's content to this node
96. root->key = temp->key;
98. // Delete the inorder successor
99. root->right = deleteNode(root->right, temp->key);
100. }
101. return root;
102. }
104. /* Iterative function for inorder tree traversal */
105. void Ite_inOrder(struct node *root)
106. {
107. /* set current to root of binary tree */
108. struct node *current = root;
109. struct Stack *stack = createStack(100);
110. bool done = 0;
112. while (!done)
113. {
114. /* Reach the left most tNode of the current tNode */
115. if(current !=  NULL)
116. {
117. /* place pointer to a tree node on the stack before traversing
118. the node's left subtree */
119. push(stack, current);
120. current = current->left;
121. }
123. /* backtrack from the empty subtree and visit the tNode
124. at the top of the stack; however, if the stack is empty,
125. you are done */
126. else
127. {
128. if (!isEmpty(stack))
129. {
130. current = pop(stack);
131. printf("%d ", current->key);
133. /* we have visited the node and its left subtree.
134. Now, it's right subtree's turn */
135. current = current->right;
136. }
137. else
138. done = 1;
139. }
140. } /* end of while */
141. }
143. // Driver Program to test above functions
144. int main()
145. {
146. /* Let us create following BST
147. 50
148. /     \
149. 30      70
150. /  \    /  \
151. 20   40  60   80 */
152. struct node *root = NULL;
153. root = insert(root, 50);
154. root = insert(root, 30);
155. root = insert(root, 20);
156. root = insert(root, 40);
157. root = insert(root, 70);
158. root = insert(root, 60);
159. root = insert(root, 80);
161. printf("Inorder traversal of the given tree \n");
162. inorder(root);
164. printf("\nDelete 20\n");
165. root = deleteNode(root, 20);
167. printf("Iteratively Inorder traversal of the modified tree \n");
168. Ite_inOrder(root);
169. printf("\n");
170. /*
171. printf("\nDelete 30\n");
172. root = deleteNode(root, 30);
173. printf("Inorder traversal of the modified tree \n");
174. inorder(root);
176. printf("\nDelete 50\n");
177. root = deleteNode(root, 50);
178. printf("Inorder traversal of the modified tree \n");
179. inorder(root);
180. */
181. return 0;
182. }

```
### Stack的定义

```


1. // C program for array implementation of stack
2. /*
3. Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
4. Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
5. Peek or Top: Returns top element of stack.
6. isEmpty: Returns true if stack is empty, else fals.
7. */
8. #define bool int
9. //A structure to represent a tree
10. struct node
11. {
12. int key;
13. struct node *left, *right;
14. };
16. // A structure to represent a stack
17. struct Stack
18. {
19. int top;
20. int capacity;
21. struct node **array;
22. };
24. // function to create a stack of given capacity. It initializes size of
25. // stack as 0
26. struct Stack *createStack(unsigned capacity);
28. // Stack is full when top is equal to the last index
29. int isFull(struct Stack *stack);
31. // Stack is empty when top is equal to -1
32. int isEmpty(struct Stack *stack);
34. // Function to add an item to stack.  It increases top by 1
35. void push(struct Stack *stack, struct node *item);
37. // Function to remove an item from stack.  It decreases top by 1
38. struct node *pop(struct Stack *stack);

```
### Stack的实现

```


1. // C program for array implementation of stack
2. /*
3. Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
4. Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
5. Peek or Top: Returns top element of stack.
6. isEmpty: Returns true if stack is empty, else fals.
7. */
8. #include <stdio.h>
9. #include <stdlib.h>
10. #include <limits.h>
11. #include <stack.h>
13. // function to create a stack of given capacity. It initializes size of
14. // stack as 0
15. struct Stack* createStack(unsigned capacity)
16. {
17. struct Stack *stack = (struct Stack*) malloc(sizeof(struct Stack));
18. stack->capacity = capacity;
19. stack->top = -1;
20. stack->array = (struct node **) malloc(stack->capacity * sizeof(struct node *));
21. return stack;
22. }
24. // Stack is full when top is equal to the last index
25. int isFull(struct Stack *stack)
26. {   return stack->top == stack->capacity - 1; }
28. // Stack is empty when top is equal to -1
29. int isEmpty(struct Stack *stack)
30. {   return stack->top == -1;  }
32. // Function to add an item to stack.  It increases top by 1
33. void push(struct Stack *stack, struct node *item)
34. {
35. if (isFull(stack))
36. return;
37. stack->array[++stack->top] = item;
38. //printf("%d pushed to stack\n", item);
39. }
41. // Function to remove an item from stack.  It decreases top by 1
42. struct node* pop(struct Stack *stack)
43. {
44. if (isEmpty(stack))
45. return NULL;
46. return stack->array[stack->top--];
47. }

```
### BST in Python

```


1. # Python program to demonstrate insert operation in binary search tree
3. # A utility class that represents an individual node in a BST
4. class Node:
5. def __init__(self,key):
6. self.left = None
7. self.right = None
8. self.val = key
10. # A utility function to insert a new node with the given key
11. def insert(root,node):
12. if root is None:
13. root = node
14. else:
15. if root.val < node.val:
16. if root.right is None:
17. root.right = node
18. else:
19. insert(root.right, node)
20. else:
21. if root.left is None:
22. root.left = node
23. else:
24. insert(root.left, node)
26. # A utility function to do inorder tree traversal
27. def inorder(root):
28. if root:
29. inorder(root.left)
30. print(root.val),
31. inorder(root.right)
33. # Iterative function for inorder tree traversal
34. def Ite_inOrder(root):
35. #set current to root of binary tree
36. current = root
37. stack = []
38. done = False
40. while not done:
41. # Reach the left most tNode of the current tNode
42. if current !=  None:
43. #place pointer to a tree node on the stack before traversing the node's left subtree
44. stack.append(current)
45. current = current.left
47. #  backtrack from the empty subtree and visit the tNode
48. #  at the top of the stack; however, if the stack is empty,
49. #  you are done
50. else:
51. if len(stack) != 0:
52. current = stack.pop()
53. print(current.val),
55. # we have visited the node and its left subtree.
56. # Now, it's right subtree's turn
57. current = current.right
58. else:
59. done = True
61. # end of while
62. #end of Ite_inOrder
64. # Driver program to test the above functions
65. # Let us create the following BST
66. #      50
67. #    /    \
68. #   30     70
69. #   / \    / \
70. #  20 40  60 80
71. r = Node(50)
72. insert(r,Node(30))
73. insert(r,Node(20))
74. insert(r,Node(40))
75. insert(r,Node(70))
76. insert(r,Node(60))
77. insert(r,Node(80))
79. # Print inoder traversal of the BST
80. inorder(r)
81. # This code is contributed by Bhavya Jain
82. print
83. Ite_inOrder(r)
84. # Ite_inOrder is contributed by Bintou

```

---


`@bintou`
`2017-12-07 05:21:10`
`字数 668`
`阅读 1951`


C语言操作文件
=======

`Source` `Code`

---

### C语言简单实例

请大家阅读.

```


1. /* 本程序展示C语言操作文件的基本方法。
2. The latest C standard C11 provides a new mode “x” which is exclusive create-and-open mode.
3. Mode “x” can be used with any “w” specifier, like “wx”, “wbx”.
4. When x is used with w, fopen() returns NULL if file already exists or could not open.
5. */
6. #include <stdio.h>
7. #include <stdlib.h>
9. int main()
10. {
11. FILE *fp = fopen("test.txt", "wx");
12. if (fp == NULL)
13. {
14. puts("Couldn't open file or file already exists");
15. //exit(0);
16. }
17. else
18. {
19. fputs("This is a test for FILEs operation.", fp);
20. puts("Write done.");
21. fclose(fp);
22. }
23. // Open file
24. fp = fopen("test.txt", "r");
25. if (fp == NULL)
26. {
27. printf("Cannot open file. \n");
28. exit(0);
29. }
31. // Read contents from file
32. char c = fgetc(fp);
33. while (c != EOF)
34. {
35. printf ("%c", c);
36. c = fgetc(fp);
37. }
38. printf("\n");
39. fclose(fp);
40. return 0;
41. }

```

---


`@bintou`
`2017-12-07 18:43:37`
`字数 4246`
`阅读 1956`


Stack in C/C++
==============

`Source` `Code`

---

> 修改了一下代码，分成三个文件：stack.h 、stack.cpp和调用stack.cpp的main.cpp文件.
> 
> 练习：使用Linked list实现一种动态Stack，即，Stack的Size可以根据应用的需求增大，而无需预先定死。

### stack.h

```


1. /* C++ head file to define a class of stack.
2. Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
3. Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
4. Peek or Top: Returns top element of stack.
5. isEmpty: Returns true if stack is empty, else fals.
6. */
7. #define MAX 1000
9. class Stack
10. {
11. int top;
12. public:
13. int a[MAX];    //Maximum size of Stack
15. Stack()  { top = -1; }
16. bool push(int x);
17. int pop();
18. int peek();
19. bool isEmpty();
20. };

```
### stack.cpp

```


1. /* C++ program to implement a basic stack. */
3. #include <stack_oo.h>
5. bool Stack::push(int x)
6. {
7. if (top >= MAX)
8. {
9. //cout << "Stack Overflow";
10. return false;
11. }
12. else
13. {
14. a[++top] = x;
15. return true;
16. }
17. }
19. int Stack::pop()
20. {
21. if (top < 0)
22. {
23. //cout << "Stack Underflow";
24. return 0;
25. }
26. else
27. {
28. int x = a[top--];
29. return x;
30. }
31. }
33. int Stack::peek()
34. {
35. if (top < 0)
36. {
37. //cout << "Stack Underflow";
38. return -1;
39. }
40. else
41. {
42. return a[top];
43. }
44. }
46. bool Stack::isEmpty()
47. {
48. return (top < 0);
49. }

```
### main.cpp

```



2. /* C++ program to test basic stack operations */
4. #include <stack_oo.h>
5. #include <iostream>
7. int main()
8. {
9. Stack s;
10. s.push(10);
11. std::cout << " Push a value to stack\n";
12. s.push(20);
13. std::cout << " Push a value to stack\n";
14. s.push(30);
15. std::cout << " Push a value to stack\n";
17. std::cout << s.pop() << " Popped from stack\n";
19. return 0;
20. }

```
### 老文件

```


1. // C program for array implementation of stack
2. /*
3. Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
4. Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
5. Peek or Top: Returns top element of stack.
6. isEmpty: Returns true if stack is empty, else fals.
7. */
8. #include <stdio.h>
9. #include <stdlib.h>
10. #include <limits.h>
12. // A structure to represent a stack
13. struct Stack
14. {
15. int top;
16. unsigned capacity;
17. int* array;
18. };
20. // function to create a stack of given capacity. It initializes size of
21. // stack as 0
22. struct Stack* createStack(unsigned capacity)
23. {
24. struct Stack* stack = (struct Stack*) malloc(sizeof(struct Stack));
25. stack->capacity = capacity;
26. stack->top = -1;
27. stack->array = (int*) malloc(stack->capacity * sizeof(int));
28. return stack;
29. }
31. // Stack is full when top is equal to the last index
32. int isFull(struct Stack* stack)
33. {   return stack->top == stack->capacity - 1; }
35. // Stack is empty when top is equal to -1
36. int isEmpty(struct Stack* stack)
37. {   return stack->top == -1;  }
39. // Function to add an item to stack.  It increases top by 1
40. void push(struct Stack* stack, int item)
41. {
42. if (isFull(stack))
43. return;
44. stack->array[++stack->top] = item;
45. printf("%d pushed to stack\n", item);
46. }
48. // Function to remove an item from stack.  It decreases top by 1
49. int pop(struct Stack* stack)
50. {
51. if (isEmpty(stack))
52. return INT_MIN;
53. return stack->array[stack->top--];
54. }
55. // Driver program to test above functions
56. int main()
57. {
58. struct Stack* stack = createStack(100);
60. push(stack, 10);
61. push(stack, 20);
62. push(stack, 30);
64. printf("%d popped from stack\n", pop(stack));
66. return 0;
67. }

```
```


1. /* C++ program to implement basic stack
2. operations */
3. /*
4. Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
5. Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
6. Peek or Top: Returns top element of stack.
7. isEmpty: Returns true if stack is empty, else fals.
8. */
9. #include<bits/stdc++.h>
10. using namespace std;
12. #define MAX 1000
14. class Stack
15. {
16. int top;
17. public:
18. int a[MAX];    //Maximum size of Stack
20. Stack()  { top = -1; }
21. bool push(int x);
22. int pop();
23. bool isEmpty();
24. };
26. bool Stack::push(int x)
27. {
28. if (top >= MAX)
29. {
30. cout << "Stack Overflow";
31. return false;
32. }
33. else
34. {
35. a[++top] = x;
36. return true;
37. }
38. }
40. int Stack::pop()
41. {
42. if (top < 0)
43. {
44. cout << "Stack Underflow";
45. return 0;
46. }
47. else
48. {
49. int x = a[top--];
50. return x;
51. }
52. }
54. bool Stack::isEmpty()
55. {
56. return (top < 0);
57. }
59. // Driver program to test above functions
60. int main()
61. {
62. struct Stack s;
63. s.push(10);
64. s.push(20);
65. s.push(30);
67. cout << s.pop() << " Popped from stack\n";
69. return 0;
70. }

```
```


1. /*
2. The functions associated with stack are:
3. empty() – Returns whether the stack is empty
4. size() – Returns the size of the stack
5. top() – Returns a reference to the top most element of the stack
6. push(g) – Adds the element ‘g’ at the top of the stack
7. pop() – Deletes the top most element of the stack
8. */
9. #include <iostream>
10. #include <stack>
12. using namespace std;
14. void showstack(stack <int> gq)
15. {
16. stack <int> g = gq;
17. while (!g.empty())
18. {
19. cout << '\t' << g.top();
20. g.pop();
21. }
22. cout << '\n';
23. }
25. int main ()
26. {
27. stack <int> gquiz;
28. gquiz.push(10);
29. gquiz.push(30);
30. gquiz.push(20);
31. gquiz.push(5);
32. gquiz.push(1);
34. cout << "The stack gquiz is : ";
35. showstack(gquiz);
37. cout << "\ngquiz.size() : " << gquiz.size();
38. cout << "\ngquiz.top() : " << gquiz.top();
41. cout << "\ngquiz.pop() : ";
42. gquiz.pop();
43. showstack(gquiz);
45. return 0;
46. }

```

---


`@bintou`
`2017-11-01 06:28:08`
`字数 4594`
`阅读 2180`


Crypto-related Codes in Sage
============================

`Code` `Crypto` `Sage`

---

RSA Code
--------

### Basis Algorithm

```


1. #https://www.math.ucdavis.edu/~anne/FQ2010/Number_Theory_RSA.html
2. def rsa_kg(bits):
3. # only prove correctness up to 1024 bits
4. proof = (bits <= 1024)
5. p = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
6. q = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
7. n = p*q
8. phi_n = (p-1)*(q-1)
9. while True:
10. e = ZZ.random_element(1,phi_n)
11. if gcd(e,phi_n) == 1: break
12. d = lift(Mod(e,phi_n)^(-1))
13. return e, d, n
15. def encrypt(m, e, n):
16. return lift(Mod(m,n)^e)
18. def decrypt(c, d, n):
19. return lift(Mod(c,n)^d)
21. def encode(s):
22. s = str(s)
23. return sum(ord(s[i])*256^i for i in range(len(s)))
25. def decode(n):
26. n = Integer(n)
27. v = []
28. while n != 0:
29. v.append(chr(n % 256))
30. n //= 256     # this replaces n by floor(n/256)
31. return ''.join(v)
33. e,d,n = rsa_kg(1024)
34. m = encode('Meet me at 4.'); m
35. c = encrypt(m,e,n); c
36. M = decrypt(c,d,n); M
37. decode(M)

```
### Common Modulus Attack

Given e, d, N and e1, compute d1 such that d1 is a valid decrypting exponent for the public key (e1 , N )

```


1. k1 = gcd(e1 , e*d − 1)
2. k2 = (e*d − 1) / k1
3. d1 = xgcd(e1, k2) [1]

```
### Small d attack

攻击成功的条件：q < p < 2q and that d < n^{1/4}/3

0、生成弱秘钥

```


1. def rsa_weak_kg(bits):
2. # only prove correctness up to 1024 bits
3. proof = (bits <= 1024)
4. p = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
5. q = next_prime(ZZ.random_element(2**(bits//2+1)), proof=proof)
6. n = p*q
7. phi_n = (p-1)*(q-1)
8. while True:
9. d = ZZ.random_element(2**(bits//4))
10. if gcd(d,phi_n) == 1 and 36*pow(d, 4) < n: break
11. e = lift(Mod(d,phi_n)^(-1))
12. return e, d, n

```

1、算e/n的连分数

```


1. fra = (e/n).continued_fraction()

```

2、依次选择fra对e/N的逼近，记为k/d，利用这个k和d进行N的分解

```


1. # Define f(x)= (x - p)(x - q) = 0
2. # x = var('x')
3. # a , b, c = 1, 1, 1
4. # qe = (a*x^2 + b*x + c == 0)
6. # Trials
7. def small_d_attack(fra):
8. for i in range(1, len(fra)):
9. k = fra.numerator(i)
10. d = fra.denominator(i)
11. if k != 0:
12. phi = (d*e - 1)/k
13. a = 1
14. b = -(n - phi + 1)
15. c = n
16. # Define f(x)= (x - p)(x - q) = 0
17. x = var('x')
18. qe = (a*x^2 + b*x + c == 0)
19. sol = solve(qe, x)
20. p = sol[0].right()
21. q = sol[1].right()
22. if p.is_integer() and q.is_integer() and q*p == n:
23. print sol[0].right(), sol[1].right()
24. print "We found the decrypting exponent.", d
25. break

```

Discrete Logarithm
------------------

### Sage下Dlog的求解命令

```


1. F.<a>=GF(2^16+1)
2. g=F.multiplicative_generator()
3. u=g**12345
4. discrete_log(u,g)
5. # discrete_log_rho(u,g) can't work for composite order group.

```
### DLOG实例生成

```


1. # p is a prime and q is (p-1)/2 and also a prime. Thus Zq* is a subgroup of Zp* with prime order.
2. def dlog_gen(n):
3. p = next_prime(n)
4. while not is_prime( floor((p-1)/2) ):
5. p = next_prime(p)
6. x = randint(1,p-1)
7. y = randint(1,p-1)
8. g = x*x % p
9. h = y*y % p
10. return [p,floor( (p-1)/2 ),g,h]

```
### Baby-Step Giant-Step DLOG

```


1. # Generate a random DLOG instance.
2. def dlog_gen(bits):
3. p = next_prime(ZZ.random_element(2**bits))
4. q = floor((p-1)/2)
5. while not is_prime(q):
6. p = next_prime(p)
7. q = floor((p-1)/2)
8. g = 1
9. while g == 1:
10. x = randint(1, p-1)
11. g = x*x % p
12. return [p,q,g]
14. # Baby Step Giant Step DLP problem a = g**x mod n
15. # Input: g,a,n where g is the generator, a = g^x mod n,
16. def dlog_bgs(a, g, n):
17. s = floor(sqrt(n))
18. A = []
19. B = []
20. for r in range(0,s):
21. value = a*(g^r) % n
22. A.append(value)
24. for t in range(1,s+1):
25. value = g^(t*s) % n
26. B.append(value)
27. #print A
28. #print B
29. x1,x2 =0,0
31. for u in A:
32. for v in B:
33. if u == v:
34. x1 = A.index(u)
35. x2 = B.index(v)
36. #print x1,x2
37. break
39. #print 'the value of x is ', ((x2+1)*s - x1) % n # Answer
40. return ((x2+1)*s - x1) % n

```
### Pollard rho discrete logarithm

```


1. # A simple Pollard rho discrete logarithm
2. # implementation and has some limitations:
3. # 1. p must be a prime that equals 2q + 1
4. # 2. q must be a prime, too
5. # 3. g generates a sub group with order q
6. # 4. a belongs to <g>, the subgroup generated by g
7. # these four limitations made this program simpler
8. # x = log_g(a) in Zp
9. # assert: classify(1) != 1
11. def classify(x):
12. # 3n + 2 -> S0
13. # 3n     -> S1
14. # 3n + 1 -> S2
15. return (x + 1) % 3
17. def succssor(x, s, t, p, q, g, a):
18. c = classify(x)
19. if c == 0:
20. return (g * x) % p, (s + 1) % q, t
21. elif c == 1:
22. return (x * x) % p, (2 * s) % q, (2 * t) % q
23. else: # c == 2
24. return (a * x) % p, s, (t + 1) % q
26. def dlog_rho(a, g, p, q):
27. xa, sa, ta = 1, 0, 0
28. xb, sb, tb = succssor(1, 0, 0, p, q, g, a)
29. while xa != xb:
30. xa, sa, ta = succssor(xa, sa, ta, p, q, g, a)
31. xb, sb, tb = succssor(xb, sb, tb, p, q, g, a)
32. xb, sb, tb = succssor(xb, sb, tb, p, q, g, a)
34. s, t = sa - sb, tb - ta
35. if s == 0:
36. return 'fail'
37. if s < 0:
38. s = s + q
39. if t < 0:
40. t = t + q
41. res = xgcd(t, q)[1]
42. if res < 0 :
43. res = res + q
44. res = (res * s) % q
45. return res
47. # How to use in Sage and compare with discrete_log and discrete_log_rho
48. bits = 30
49. p,q,g = dlog_gen(30)
50. x = 120
51. a = Mod(g,p)^x
52. time discrete_log(a, g, p)
53. time discrete_log_rho(a, g, q)
54. #dlog_bgs(g, a, p)
55. #dlog_rho(g, a, p, q)

```

WStein 2017 Elementary Number Theory
------------------------------------

### Chapter 6 ECC

```


1. #Code from WStein 2017 Elementary Number Theory
2. from sage.libs.libecm import ecmfactor
4. ecmfactor(2^128+1,1000,sigma=227140902)
6. # Pollard p-1 method
7. def pollard(N, B=10^5, stop=10):
8. m = prod([p^int(math.log(B)/math.log(p)) for p in prime_range(B+1)])
9. for a in [2..stop]:
10. x = (Mod(a,N)^m - 1).lift()
11. if x == 0: continue
12. g = gcd(x, N)
13. if g!=1 or g != N: return g
14. return 1
16. # Lenstra's EC method
17. def ecm(N, B=10^3, trials=10):
18. m = prod([p^int(math.log(B)/math.log(p)) for p in prime_range(B+1)])
19. R = Integers(N)
20. # Make Sage think that R is a field:
21. R.is_field = lambda : True
22. for _ in range(trials):
23. while True:
24. a = R.random_element()
25. if gcd(4*a.lift()^3 + 27, N) == 1: break
26. try:
27. m * EllipticCurve([a, 1])([0,1])
28. except ZeroDivisionError, msg:
29. # msg: "Inverse of <int> does not exist"
30. return gcd(Integer(str(msg).split()[2]), N)
31. return 1
33. #set_random_seed(2)
34. #ecm(5959, B=20)
35. #ecm(next_prime(10^20)*next_prime(10^7), B=10^3)

```

---


`@bintou`
`2016-07-13 18:44:58`
`字数 1841`
`阅读 3350`


Source Code of Lattice-Based Cryptography
=========================================

`Code` `Lattice-based` `Cryptography` `Projects`

---

### 1. A Toolkit which implement the LPR'13

Toolkit for Ring-LWE Based Cryptography in Arbitrary Cyclotomic Number Fields（<http://eprint.iacr.org/2016/049>）. <https://github.com/CMMayer/Toolkit-for-Ring-LWE.git>

### 2. An AKE Scheme from CP'14

A Practical Key Exchange for the Internet using Lattice(<https://eprint.iacr.org/2015/138>). <https://github.com/vscrypto/ringlwe_power>

### 3. "Newhope" Ring-LWE-based key exchange

Paper: Erdem Alkim, Léo Ducas, Thomas Pöppelmann, and Peter Schwabe: Post-quantum key exchange – a new hope(<https://cryptojedi.org/papers/newhope-20151207.pdf>).   

<https://github.com/tpoeppelmann/newhope>   

<https://cryptojedi.org/crypto/#newhope>

### 4. BLISS

BLISS: Bimodal Lattice Signature Schemes(<http://bliss.di.ens.fr/>).

### 5. Hardware Security Group in RUB

Implementation of lattice-based cryptography by Hardware Security Group in RUB( <https://www.sha.rub.de/research/projects/lattice/>).

### 6. NTRU OpenSourceProject

<https://github.com/NTRUOpenSourceProject/ntru-crypto>   

<https://www.securityinnovation.com/products/encryption-libraries/ntru-crypto/ntru-resources.html>

### 7. MALB personal source

His Blog: <https://martinralbrecht.wordpress.com/>   

<https://bitbucket.org/malb/>

### 8. Post-quantum key exchange from the ring learning with errors problem

This software implements the key exchange protocol based on the ring learning with errors (ring-LWE) problem from the following paper:

* Joppe W. Bos, Craig Costello, Michael Naehrig, Douglas Stebila. Post-quantum key exchange for the TLS protocol from the ring learning with errors problem. In Proc. IEEE Symposium on Security and Privacy (S&P) 2015, pp. 553-570. IEEE, May 2015. DOI:10.1109/SP.2015.40, Eprint <http://eprint.iacr.org/2014/599>.

This software was initially distributed by the authors from <https://github.com/dstebila/rlwekex>

### 9. Yet another new hope?

Speeding up R-LWE post-quantum key exchange. Eprint: <http://eprint.iacr.org/2016/467>   

The source distributed by the authors: <https://github.com/fschlieker/newhope>.



---


`@bintou`
`2016-03-16 17:46:31`
`字数 6875`
`阅读 2548`


高校计算机教育与IT职业市场的关系
=================

`计算机教育` `IT职业` `教育改革`

---

*註：2005年的老文章，內容過時了，發在這裏只是爲了備忘。2016年3月*

摘 要：高校计算机教育的改革不应以IT职业市场的需求为指针。首先，讨论当前美国计算机教育与市场需求之间的矛盾，指出在计算机教育体系相对完善、市场需求相对成熟的环境中，高校计算机教育与市场需求的鸿沟依然难以跨越。其次，通过讨论计算机科学的学科特性，指出计算机科学领域中有着相对固定的知识体系，高校计算机教育的发展方针应尊重学科规律，而不应轻易地被某些不稳定因素所动摇。进而讨论以市场需求为指针的学科建设的多种困难。最后，为跨越高校计算机教育与IT职业市场的鸿沟设想若干对策。

关键词：计算机教育，IT职业，教育改革

一、前言
----

现阶段我国高校计算机专业的教育与IT职业市场的需求之间存在着尖锐的矛盾。一方面，高校计算机专业规模蓬勃发展。从普通本科计算机教育的层面上看，全国高校总数为l683所，本科学校679所，其中505所开设有“计算机科学与技术”专业，是全国专业之首。另一方面，我国IT产业处于高速成长期，从人才市场反馈回的信息表明，计算机人才处于供需两旺的形势。现在IT人才每年需求100万，其中仅软件人才缺口每年就达42万。而矛盾在于每年却有相当大一部分计算机毕业生找不到工作【1】。

在计算机毕业生严峻的就业压力下，部分学生出现了学习目的不明确、学习积极性不高等问题。文献【2】的调查数据显示，有相当一部分学生认为计算机专业课程枯燥难懂，对学习计算机课程失去信心和兴趣，甚至后悔报考计算机专业。另一方面，用人单位又抱怨高校的计算机教育过于理论化，知识过于陈旧，学生的动手能力较差，并质疑高校计算机教育的培养计划。

面对如此尖锐的矛盾，反思高校计算机教育中存在的问题，有学者得出这样的结论：我国高校计算机教育中普遍存在着重视理论知识忽视职业技能、教学方法与实践相脱离、教材内容陈旧抽象、学生缺乏实际锻炼等问题，这种人才培养模式培养出的学生与企业实际用人存在巨大差异，难以胜任其IT岗位职责的技能。进而认为“我国的计算机专业教育，无论是教育理念、教学方式还是教材内容，都应该从纯粹的理论模式向应用开发模式方向发展，从纯教学型向社会应用型模式发展，这样才会大大提高我国计算机专业教育的质量，培养市场需要的应用型人才”【2】。类似的观点得到了广泛的认同【1，3】。并且，高校的管理者、教师、学生等也在自觉与不自觉地以职业市场的需求为参照来指导自己的行为。

针对以上观点，本文在同意高校计算机教育存在问题、需要改革的前提下，重点讨论这样一个问题：改革高校计算机专业的培养目标、培养计划是否应以IT职业市场的需求为指针来培养市场需要的应用型人才。全文组织如下，第二章讨论当前美国计算机教育与IT职业市场之间的供求矛盾，指出在计算机教育体系相对完善、劳动市场相对成熟的环境中，高校计算机教育与市场需求的鸿沟依然难以跨越。第三章通过讨论计算机科学的学科特性，指出计算机科学领域中有着相对固定的知识体系，高校计算机教育的发展方针应尊重学科规律，而不应轻易地被其他不稳定因素所动摇。第四章讨论以市场需求为指针的学科建设的多种困难。最后，总结全文并为跨越高校计算机教育与IT职业市场的鸿沟设想若干对策。

二、欧美高校计算机教育与市场需求的现状
-------------------

文献【4】显示，在欧美等发达国家中，现在也出现了计算机教育与市场需求的巨大矛盾。在美国高校，选修计算机专业的学生正逐年减少，从2000年至2004年，大学新生选择计算机专业的人数下降了60%。在2004年，大学新生选择计算机专业的比例下降为1.4%，于1993年至1997年的平均值1.6%,而最高峰值是1998年的3.4%。问题更为严重的是，在不同的高校中，中途退出计算机专业学习的比率高达35%-50%。另一方面，IT职业的需求却稳步上升。美国劳动统计局的预计，到2012年，除计算机操作员（下降）与程序员（持平）以外，对各类计算机专业人才的需求将增加20%-50%。

在英国也有相同的趋势。在2000年至2004年间，申请就读计算机科学专业的申请者从24,151人下降为13,715人，申请就读软件工程的申请者则从1,892人下降为917人。而且退学率也非常之高。同一时期，申请数学专业的人数从3,925上升至4,533，申请电子电气工程专业的人数从3,016上升至5,852。同样，在其他欧洲国家中也出现了计算机专业的入学率在下降，而IT职业的需求却在增长的问题。

引用以上数据不是要说明欧美各国也遭遇了我国相同的问题，而是说明在教育体系相对完善、劳动市场相对成熟的环境中计算机专业的教育与市场的需求之间依然存在难以跨越的鸿沟，制订计算机教育的发展方针是一个应当长远规划的难题。所以，面对我国计算机教育与市场需求的矛盾，在加紧计算机教育改革的同时，更应慎重审视计算机专业的学科规律和发展前景，不要轻易下结论认为我国的高校计算机教育脱离了市场的实际需求，从而盲目地制订计算机教育的发展模式、人才培养模式。比如，以我国“软件人才缺口每年就达42万”的现状，如果不脱离市场的实际需求，是否高校计算机专业就应该发展成为软件人才的培训基地？不要忽视上文中的一个细节：在不远的将来，对计算机操作员、程序人员的需求非但不会增长，反而会下降。

欧美等国的计算机教育现状恰好是我们计算机教育发展的重要参照物，在下一章我们还会就此进行讨论。

三、计算机科学的学科特性
------------

在计算机专业毕业生面临严峻的就业压力之时则反思、质疑计算机教育的模式，然而数学专业等理工科专业的学生显然也面临着同样（甚至更严重的）就业压力，却鲜有人对数学等专业的教育模式、培养计划提出质疑。这是否意味着计算机科学具有其他学科所不同的学科特性呢？本文认为，现在对计算机教育的质疑（无论是学者还是学生）往往基于这样一种潜台词“现在是IT时代，计算机专业的学生就应该具有就业的优势，因为计算机专业是一种面向应用的工程型学科”，却忽视了计算机科学如其他科学一样具有自身的学科特性。

目前，计算机科学的性质还无定论，在它是纯理论的学科还是应用型学科上还存在分歧。但是科学家似乎普遍认为计算机科学是一门严密的科学。荷兰计算机科学家Edsger Dijkstra认为“计算机科学是应用数学最难的一个分支”，而美国计算机科学家Ronald Knuth认为“计算机科学是关于算法的科学”。同为图灵奖的获得者，他们的观点在学术界具有广泛的代表性。文献【5】认为，目前的计算机科学还不如说是一门科学与工程的学科，或者是科学与工程学及更广泛的学科。计算机科学并不是典型的工程学科，确切地说它是一种新形式的工程学。同样，计算机科学也不是一门典型的理科，计算机科学本质上不同于其它科学。因此．它可以被看作是科学中一种新的形式。

本文并不准备在计算机科学的学科特性上进行争论，但是既然计算机科学已经作为一门学科得到承认，那么计算机科学领域就有着相对固定的知识体系，不会轻易为某些不稳定因素所动摇，比如，市场的需求。不妨比较美国计算机械协会ACM和国际电气电子工程师协会计算机学会IEEE／CS联合工作组分别在1991年发布的计算教程1991(CC1991)和在2001年发布的计算教程2001（CC2001）中所定义的计算机学科中的主要知识体系的差别。

离散结构   

程序设计基本原理   

算法与复杂度   

体系结构与组织   

操作系统   

网络计算   

程序语言   

人机交互   

图形与可视计算   

智能系统   

信息管理   

社会与职业专题   

软件工程   

可计算性与数值方法   

表1. CC1991知识体系

算法与数据结构   

体系结构   

人工智能与机器人学   

数据库与信息检索   

人机通信   

数值与符号计算   

操作系统   

程序语言   

软件方法学与工程   

表2.CC2001的知识体系

通过比较表1和表2不难发现，计算机学科在经过了10年的发展之后其知识体系并没有发生巨大的本质的改变，只是在理论的广度、深度进一步加强，比如增加了多媒体、网络等的知识领域，加深了算法、复杂性理论、可计算理论等理论深度。

既然计算机科学有着相对稳定的知识体系，也有着自身的学科发展规律，那么大学的计算机教育的发展方针无疑应该首先尊重学科规律，围绕核心的知识体系进行人才培养，培养经得起时间考验的合格人才。P.J. Denning在反思美国计算机教育与市场需求存在矛盾的现状时深刻地指出：很多人相信计算机科学只属于技术领域，并没有多少科学的和工程的成份。CC1991知识体系并没有得到充分的重视，高校并没有把计算机专业作为一门学科进行建设，而是将计算机科学等同于程序设计。例如，程序设计课程并不重视算法的构造，也不是作为软件系统工程的重要基础，而是在介绍不同程序语言的使用，比如Java或者C++等程序语言【6】。他认为，忽视计算机科学的学科特性正是导致学生缺乏学习积极性而市场又缺乏人才的重要原因之一。

我国高校计算机教育发展较晚，学科的基本建设方针很大程度上是借鉴了美国高校的先进经验和课程体系，大方向并没有错。现在鉴于就业的压力、市场的需求，将原来的教育理念、教学方式全盘否定，提出所谓的开发型、应用型模式，是否足够慎重呢？美国高校计算机教育的教训在于警告我们高校计算机教育的建设必须尊重计算机学科的发展规律，要立足于长远的规划，而市场需求、就业压力等都是动态的、不稳定的因素，怎么能以之为指针来左右学科的建设呢？

四、高校计算机教育面向市场的困难
----------------

高校不（应）是职业培训基地，但是由于在我国改革开放的特定大环境中，各高校面临着扩招、就业率等重重压力，尊重学科规律的教育发展方针似乎只是理论正确的思路，常被斥为“纸上谈兵”。有高校领导明确指出，学生就业率关乎于学校的存亡。在这样的压力下，高校计算机教育的发展要适应市场的需求几乎是无法避免的事实。然而，在现在的教育体制下，让教育去适应市场也许就是“削足适履”，操作上困难重重。有学者提出这样的思路，计算机教育要保持动态性，所谓动态性就是根据市场的需求随时改进教学计划。实际上，这似乎也只是理论正确的思路。

首先，课程建设缺乏依据。就现有的高校体制而言，我们没有拥有任何的手段或机制来保证所要开设的课程确实能满足职业市场的迫切需求。换而言之，在大谈市场需求的时候我们发现，高校里并没有深入调研市场的机制，在缺乏数据支持、理论依据的情况下，所谓根据市场需求进行的课程建设就有可能只是道听途说，或者一叶障目，或者只能是有识之士的英明领导。而依据计算机学科的知识体系进行课程建设就能体现出强有力的理论根据。

其次，课程的质量难以得到保证。市场的需求以实用为主，不追究学术性，以此为指针的课程建设质量当然难以保证。上世纪90年代的计算机本科生入学之后的基础课程是打字练习、五笔字型输入，这在现在看来也许是可笑的，课程的含金量不足。但是，现在要求计算机本科生不断地学习C++、Java、Delphi、C#等等开发语言，学习网页的制作，学习动画的设计，这就不可笑吗，这样的课程又能有多大的含金量？在低水平的课程体系中培养出来的学生也许能得一时之利，但是却没办法保证他在计算机领域的可持续发展性。

第三，教学计划难以制订。市场的需求在快速更新，而且要求千变万化，不成体系。新课程往往是在原有专业的课程框架之上进行添加，比如在网络工程的课程体系中增加《J2EE网络应用技术》、《电子商务导论》等课程。这样直接导致制订出的教学计划针对性不强，难以形成完整的课程体系。而且，高校中课程建设中的各种烦琐的行政步骤也直接导致课程建设不可能在短期之内完成，所谓教学计划的动态性也无法保证。   

另外，投入大量的人力物力去建设短期效应的课程会造成严重的资源浪费，课程负责人的积极性不高等等问题。总之，大学教育本来是超前于市场的学科教育，现在却要跟着市场的尾巴跑，既不符合学科发展的规律，而实际操作也困难重重，所以提出紧跟市场需求的教育方针也往往流于空谈。

五、总结
----

本文的一个重要观点是认为高校计算机教育的建设必须尊重计算机学科的发展规律，不应以IT职业市场的需求为指针。但是在当前严峻的就业压力之下，高校及其相关职能部门也应当为跨越计算机教育与IT职业市场的鸿沟而做出多种努力，为此本文提出以下对策。

首先，以计算机学科的知识体系为基础，通过建设完善主干课程的课程实验，以达到培养学生的工程应用能力的目的。比如，应大力建设完善数据结构、操作系统、编译原理等课程的课程设计实验平台，将理论学习与培养学生的开发能力结合起来。应该相信，完备的知识体系辅于完善的实验系统的计算机教育模式必定能培养出能迅速适应市场需求的开发型人才，而针对市场需求的特定技能无需在高校进行培训。

其次，应尽快建设、完善IT职业培训机构以满足市场需求。高校注重以学科为主的计算机教育，用人单位迫切需求拥有特定技能的人员，所以应当建设IT职业培训机构来跨越高校与职业市场的鸿沟。高等院校与职业培训机构独立并存，各司其职，可使高校摆脱陷入职业培训的尴尬而关注学科的建设。职业培训具有高校教育所没有的针对性、实用性、灵活性和多样性，可以缓解就业压力，并提高劳动者的职业素质。对于高校毕业生而言，通过短期的职业培训可有针对性地提高自身的技术性和技能性，从而提升自己在职业市场的竞争力。

最后，应深入进行计算机科学的学科特性与学科现状的研究，并加大对高校计算机教育性质的宣传。把计算机科学等同于程序设计、把计算机学科视为面向应用的工程型学科等不正确观点还深深地影响着决策者、管理者、教师、学生等的行为模式，造成很大的负面影响。通过深入的理论研究可以澄清某些不正确的观点，加大宣传可以消除非专业人士的各种误会，从而确保高校计算机教育改革走在正确的发展道路之上。

参考文献   

1. 王 莉. 我国高校计算机人才培养的现状研究, 武汉科技学院学报, Vol 18(12):142-143，2005年12月   

2. 赵旭，郝筱松. 浅析高校计算机教育中存在的问题，陕西教育学院学报,Vol 21(2):100-102, 2005年5月   

3. 钟乐海，谭斌. 高师院校计算机科学与技术专业课程建设及教学内容改革与实践，西华师范大学学报(哲学社会科学版)，Vol 2005(5):143-145, 2005年5月   

4. Peter J. Denning , Andrew McGettrick. Recentering Computer Science. Communication of The ACM, Vol 48(11): 15-19, Nov 2005   

5. 牟连佳，赵植武. 论计算机科学的学科性质--一对大学生计算机学科学习的要求，计算机工程与应用，Vol 2006(15): 52-55，2006年8月   

6. Peter J. Denning. The Field of Programmers Myth. Communication of The ACM, Vol 47(7): 15-20, July 2004

Computer Education and IT Profession
------------------------------------

**Abstract.** In this paper, we suggest that the development of computer education in high school should not be affected by the trends of IT profession. Firstly, we discuss the current chasm between the computer education of college and the increase of IT job in U.S., and indicate that it is difficult to cross the chasm even in a relative mature environment of education and profession. Secondly, we discuss computing as a discipline and show there is a stable body of knowledge in the field, the development of computer education in high school should follow the rules of the discipline but should not be affected by some unstable factors. Moreover, we argue that we will encounter many obstacles if we construct the computing discipline following the requirements of the IT labor market. Lastly, we propose some countermeasures to cross the chasm between computer education and the IT labor market.

Key Word. Computer Education, IT Profession，Revolution of Education



---


`@bintou`
`2018-10-07 00:40:29`
`字数 529`
`阅读 1859`


Merge Sorted Linked List
========================

`编程` `代码` `LeetCode`

---

### 题目

这个题目出自LeetCode，[合并两条链表](https://leetcode.com/problems/merge-two-sorted-lists/description/)，推荐大家做。

### 思考

值得注意的是在链接表操作中的一些问题。比如，大家能区分以下两段代码的不同吗？

```


1. /**
2. * Definition for singly-linked list.
3. * struct ListNode {
4. *     int val;
5. *     struct ListNode *next;
6. * };
7. */
9. struct ListNode *list, *tail;
11. //list; 初始化为一个任意链表；
13. /*初始化一个名为tail的节点来跟踪list, 满足条件的情况下就把list当前节点放到tail的尾巴，然后list往前走。当然，tail也应该往前走。*/
14. tail = (struct ListNode*)malloc(sizeof(struct ListNode));
15. tail->val = -1;
16. tail->next = NULL;
18. //省略很多代码，重点在下面三行！！！
20. tail->next = list;
21. list = list->next;
22. tail = tail->next;

```

如果以上三行代码写成这样：

```


1. tail->next = list;
2. tail = tail->next;
3. list = list->next;

```

会不会有什么不同？



---


`@bintou`
`2018-01-23 05:44:09`
`字数 432`
`阅读 1957`


Linux学习经验分享与交流
==============

`学习` `Linux` `折腾`

---

Ubuntu下装QQ
----------

[别人的经验](http://blog.csdn.net/dearwind153/article/details/53294506)   

新版本下的Ubuntu运行不了，14.04是可以的。

Markdown学习
----------

1. 使用的软件、工具与插件   
   * Emacs 下的markdown-mode安装
   * Emacs 下与markdown-mode协同工作的Pandoc安装与使用
2. 所出现过的问题   
   * M+x 改变markdown command曾经出错，大概原因是没有找到major mode；
   * 需要改进的是对markdown-mode的快捷键的使用
   * 尚不明白Pandoc的主要用法
3. 主要快捷键   
   * C-c C-c m 预览
   * C-c C-c p 在Browser中预览
   * C-c C-c v 刷新

---

C/C++ 、Python编程
---------------

### PyQT5

1.安装SIP在make阶段出错！解决方法是sudo apt-get install python-dev   

2.没有安装PyQT5

### QT Creator 5.2.1

1. 安装成功、可运行！
2. 尚未进一步学习

### 大整数包及高精度运算

1. NTL   
   * 安装
   * 使用
   * 代码
   * 注意事项
2. GMP   
   * 安装
   * 使用
   * 代码
   * 注意事项

ACM竞赛
-----

1. 编程
2. 算法

---


`@bintou`
`2018-01-31 02:50:27`
`字数 5795`
`阅读 2095`


简明Y-combinator指南
================

`程序设计理论` `Y组合子`

---

> 本文试图给出一个简洁的Y-combinator的小课程，它源自与[这个帖子](http://mvanier.livejournal.com/2897.html)。我进行了翻译，改写，并简化了相关内容。希望对大家有所帮助。我只是一个搬运工，功劳归原作者。读者基本无需什么基础，只要有一个可以运行Scheme的环境即可，边看边动手试一下。

### 为什么需要学习Y-combinator?

* 它是计算机程序理论中最优雅的理论之一。
* 它是区分懂程序理论与懂写程序的试金石之一。

### 以阶乘(Factorials)为例

#### 阶乘的递归定义：

```
 factorial 0 = 1
 factorial n = n * factorial (n - 1)

```
#### 阶乘的Scheme程序：

```


1. (define (factorial n)
2. (if (= n 0)
3. 1
4. (* n (factorial (- n 1)))))

```
#### 阶乘的另一种Scheme写法

```


1. (define factorial
2. (lambda (n)
3. (if (= n 0)
4. 1
5. (* n (factorial (- n 1))))))

```

使用Lambda定义的函数是一种匿名函数，即函数本身没有名字。以上两个递归程序等价。

### “消灭”递归

思考: 使用Scheme定义factorial函数是否可以不使用递归？

答案是肯定的，而这直接引出Y combinator。

### 理论基础

以下解释一些基本概念

#### 什么是Y combinator？

Y-combinator是一种高阶函数，它的输入是一种函数（非递归），它可以返回一种递归函数。

#### Lazy求值还是Strict求值？

* Lazy evaluation，对表达式求值，你只需要对可得到最终结果的部分进行求值，即不影响最终结果的部分不会被计算。
* Strict evaluation，表达式的所有部分都被求值，然后得到最终结果。

实践中，lazy evaluation更通用，但strict evaluation更容易控制且更高效。

以下内容两种方法都将涉及。

#### 只有一种Y combinator还是有多种?

实际上，有无穷种Y-combinator，以下只涉及两种：lazy型和strict型，分别记为：normal-order Y combinator 和applicative-order Y combinator（SICP中的概念）。

#### 静态类型还是动态类型?

以下定义使用动态类型，具体细节暂时可以不讨论。Scheme支持动态类型。

#### 什么是"combinator"？

Combinator（组合子）是一种没有自由变量的Lambda表达式。

##### 实例，分析以下表达式的自由变量与受限变量：

```


1. (lambda (x) x)
2. (lambda (x) y)
3. (lambda (x) (lambda (y) x))
4. (lambda (x) (lambda (y) (x y)))
5. (x (lambda (y) y))
6. ((lambda (x) x) y)

```
##### 答案：

1、x是受限变量，这是一个combinator.   

2、y是自由变量，不是combinator.   

3、x是受限变量，这是一个combinator.   

4、x和y都是受限变量，这是组合子.   

5、非lambda表达式，非组合子；x是自由变量，y是受限变量.   

6、非lambda表达式，非组合子；x是受限变量，y是自由变量.

##### 以下定义是否combinator？

```


1. (define factorial
2. (lambda (n)
3. (if (= n 0)
4. 1
5. (* n (factorial (- n 1))))))

```

否！

##### 以下定义是否组合子？

```


1. (lambda (n)
2. (if (= n 0)
3. 1
4. (* n (factorial (- n 1)))))

```

否！因为，factorial是自由变量。

### 回到问题中来

#### 抽象出递归函数调用

之前给出的factorial函数：

```


1. (define factorial
2. (lambda (n)
3. (if (= n 0)
4. 1
5. (* n (factorial (- n 1))))))

```

我们试图把函数体中的factorial去掉。

首先我们这样做：

```


1. (define sort-of-factorial
2. (lambda (n)
3. (if (= n 0)
4. 1
5. (* n (<???> (- n 1))))))

```

里面应该放什么？

函数式编程中的一个原则：当你不知道那里要放什么，你就把它抽象出来，然后把它作为一个函数的参数。因此，我们得到：

```


1. (define almost-factorial
2. (lambda (f)
3. (lambda (n)
4. (if (= n 0)
5. 1
6. (* n (f (- n 1)))))))

```

这里我们干了这样一些事情：把对factorial的递归调用重新命名为f，然后把f作为一个函数的参数，这个函数我们命名为almost-factorial。注意：almost-factorial并非factorial函数，它是一个高阶函数，输入一个参数f（f是函数），然后返回另一个函数(就是(lambda (n) ...) 那部分)。这个函数有望成为一个factorial函数，如果我们选对了f的话！

#### 预知未来

提前透露一下以下我们大概想做的事情：一旦我们定义好 Y-combinator，我们就可以使用Y和almost-factorial来定义factorial函数：

```


1. (define factorial (Y almost-factorial))

```

从而在不需要递归调用的前提下得到一个递归函数。

#### 从 almost-factorial得到factorial

假定我们有一个factorial function factorialA，无论如何得到，也无论它是否递归。考虑一下程序：

```


1. (define factorialB (almost-factorial factorialA))

```

问题：factorialB是否阶乘函数？

要回答这个问题，我们需要展开almost-factorial的定义:

```


1. (define factorialB
2. ((lambda (f)
3. (lambda (n)
4. (if (= n 0)
5. 1
6. (* n (f (- n 1))))))
7. factorialA))

```

现在，用factorialA替换f，得到:

```


1. (define factorialB
2. (lambda (n)
3. (if (= n 0)
4. 1
5. (* n (factorialA (- n 1))))))

```

这很像一个递归的阶乘函数，但它并不是：factorialA并不等同factorialB。所以，它是一个依赖于factorialA的非递归函数。它能正常工作吗？当然，稍微分析可知，factorialB能计算阶乘当且仅当factorialA是一个阶乘函数。现在的问题是，我们不知道factorialA怎么得来！

我们能否这样定义：

```


1. (define factorialA (almost-factorial factorialA))

```

思路是：如果factorialA是一个正常的阶乘函数，我们把它扔给almost-factorial函数就又得到一个正确的阶乘函数，为什么不把这个函数命名为“factorialA”？但是，这......分明就是“永动机”啊！

实际上，如果你使用DrScheme，并且使用"lazy Scheme" language level，这个定义竟然是对的！！！

定义以下函数:

```


1. (define identity (lambda (x) x))
2. (define factorial0 (almost-factorial identity))

```

identity函数很简单：输入一个参数，然后输出该参数。这是一个组合子。我们使用它作为占位符，在我们需要传输一个函数作为参数但又不知道需要传送什么函数的时候使用它。

factorial0计算输入为0时的阶乘值。验证如下：

```


1. (factorial0 0)
3. ==> ((almost-factorial identity) 0)
5. ==> (((lambda (f)
6. (lambda (n)
7. (if (= n 0)
8. 1
9. (* n (f (- n 1))))))
10. identity)
11. 0)
13. ==> ((lambda (n)
14. (if (= n 0)
15. 1
16. (* n (identity (- n 1)))))
17. 0)
19. ==> (if (= 0 0)
20. 1
21. (* 0 (identity (- 0 1))))
23. ==> (if #t
24. 1
25. (* 0 (identity (- 0 1))))
27. ==> 1

```

OK，确实是对的，但当n > 0时它无法计算。比如，n = 1时：

```


1. (factorial0 1)
3. ==> (* 1 (identity (- 1 1)))
5. ==> (* 1 (identity 0))
7. ==> (* 1 0)
9. ==> 0

```

错！考虑下一个程序:

```


1. (define factorial1
2. (almost-factorial factorial0))

```

它可以计算0和1的阶乘。自己验证。我们这样做下去：

```


1. (define factorial2 (almost-factorial factorial1))
2. (define factorial3 (almost-factorial factorial2))
3. (define factorial4 (almost-factorial factorial3))
4. (define factorial5 (almost-factorial factorial4))

```

用这种方法，尽管我们可以得到某个n的阶乘函数，但是我们还是无法得到一个任意n的函数。

#### 函数的不动点

函数f的不动点(fixpoint)就是一个值x，使得f(x) = x。不动点不但可以是值，还可以是函数，实际上可以是不同的实物。almost-factorial的不动点就是一个函数：

```


1. fixpoint-function = (almost-factorial fixpoint-function)

```

通过替换：

```


1. fixpoint-function =
2. (almost-factorial
3. (almost-factorial fixpoint-function))
5. = (almost-factorial
6. (almost-factorial
7. (almost-factorial fixpoint-function)))
9. = ...
11. = (almost-factorial
12. (almost-factorial
13. (almost-factorial
14. (almost-factorial
15. (almost-factorial ...)))))

```

不难看出，almost-factorial的不动点就是阶乘函数：

```


1. factorial = (almost-factorial factorial)
2. = (almost-factorial
3. (almost-factorial
4. (almost-factorial
5. (almost-factorial
6. (almost-factorial ...)))))

```

但是仅仅知道factorial是almost-factorial的不动点并不够。如何求得这个不动点呢？

使用Y combinator！ Y也被称为不动点组合子：给定一个函数，求该函数的不动点。

#### 消灭递归(lazy版本)

Y的工作是：

```


1. (Y f) = fixpoint-of-f

```

f的不动点是什么？由定义，我们知道：

```


1. (f fixpoint-of-f) = fixpoint-of-f

```

因此：

```


1. (Y f) = fixpoint-of-f = (f fixpoint-of-f)

```

得到：

```


1. (Y f) = (f (Y f))

```

乌拉！我们定义出来Y！写成Scheme程序就是：

```


1. (define (Y f) (f (Y f)))

```

或者用Lambda：

```


1. (define Y
2. (lambda (f)
3. (f (Y f))))

```

然而，这里有两个问题：

1、它只能在lazy语言中工作。   

2、这个Y并不是一个combinator，因为Y在定义体中是自由变量，只有定义结束它才是受限变量。

无论如何，如果你使用lazy Scheme，你确实可以得到一个factorials:

```


1. (define Y
2. (lambda (f)
3. (f (Y f))))
5. (define almost-factorial
6. (lambda (f)
7. (lambda (n)
8. (if (= n 0)
9. 1
10. (* n (f (- n 1)))))))
12. (define factorial (Y almost-factorial))

```

这是正确的！

我们完成了什么？开始我们试图不使用递归调用来定义factorial函数，现在基本完成任务。然而，目前的Y还是递归的。不可否认，我们已经前进了一大步，为了定义递归函数，仅仅在Y的定义中使用递归。

#### 消灭递归(strict 版本)

如果在标准Scheme中使用以上定义：

```


1. (Y f)
2. = (f (Y f))
3. = (f (f (Y f)))
4. = (f (f (f (Y f))))

```

(Y f)的求值将不终止，也就是说以上定义不适合 strict语言。

有一种聪明的方法可以拯救世界。考虑到(Y f)是一个带一个参数的函数，因此，这等式满足：

```


1. (Y f) = (lambda (x) ((Y f) x))

```

无论(Y f) 这个函数是什么，(lambda (x) ((Y f) x))都与之等价。

根据以上分析，Y可以被定义为：

```


1. (define Y
2. (lambda (f)
3. (f (lambda (x) ((Y f) x)))))

```

既然(lambda (x) ((Y f) x)) 与 (Y f)等价，以上定义是对的！我们可以使用这个Y来定义factorial函数。

最酷的是，这个版本的Y可以工作在strict语言中 (比如标准Scheme)！因为，如果你给Y一个f，让它找不动点，它返回：

```


1. (Y f) = (f (lambda (x) ((Y f) x)))

```

这一次，不会陷入无穷循环，因为内部的(Y f)被一个Lambda表达式保护着，它保持不动直到它需要被求值（Scheme中，lambda表达式不会被求值，直到它被应用到某个参数上）。本质上，我们是使用lambda来对(Y f)延迟求值。所以，如果f是almost-factorial，我们会得到：

```


1. (define almost-factorial
2. (lambda (f)
3. (lambda (n)
4. (if (= n 0)
5. 1
6. (* n (f (- n 1)))))))
8. (define factorial (Y almost-factorial))

```

展开对Y的调用：

```


1. (define factorial
2. ((lambda (f) (f (lambda (x) ((Y f) x))))
3. almost-factorial))
5. ==>
7. (define factorial
8. (almost-factorial (lambda (x) ((Y almost-factorial) x))))
10. ==>
12. (define factorial
13. (lambda (n)
14. (if (= n 0)
15. 1
16. (* n ((lambda (x) ((Y almost-factorial) x)) (- n 1))))))

```

请验证！

以上分析也许容易，也许不容易，无论如何，鼓励大家去尝试，必要收获。至此，我们基本完成任务，除了一点细节。作为简明版本tutorial，就此略过。详细内容请看[Mike帖子](http://mvanier.livejournal.com/2897.html)。



---


`@bintou`
`2015-07-03 16:25:42`
`字数 733`
`阅读 2514`


East Coker from “The Four Quartets“
===================================

`诗歌` `世界文学`

---

...   

You say I am repeating   

Something I have said before. I shall say it again.   

Shall I say it again? In order to arrive there,   

To arrive where you are, to get from where you are not,   

You must go by a way wherein there is no ecstasy.   

In order to arrive at what you do not know   

You must go by a way which is the way of ignorance.   

In order to possess what you do not possess   

You must go by the way of dispossession.   

In order to arrive at what you are not   

You must go through the way in which you are not.   

And what you do not know is the only thing you know   

And what you own is what you do not own   

And where you are is where you are not.

― T.S. Eliot “East Coker“

**译文：**   

你说我在重复   

我之前曾说过的。我还要再一次谈起。   

我还要再次谈起吗？为了到达那里，   

到达你所在之地，从你所不在之处，   

你必须走一条没有欢愉之路。   

为了达到你所不解之物，   

你必须走一条无知之路。   

为了获得你所未拥有的，   

你必须走一条被剥夺之路。   

为了成就你所不是之物，   

你必须走一条非我之路。   

你所不知道的是你所唯一知道的   

你所拥有的是你所不拥有的   

你所在之地是你所不在之地。

![T.S. Eliot](http://d.gr-assets.com/authors/1362610359p5/18540.jpg)   

[译文参考](http://www.jintian.net/today/html/32/t-51832.html)



---


`@bintou`
`2017-07-09 02:31:17`
`字数 1396`
`阅读 2349`


你，安德鲁·马维尔
=========

`诗歌` `世界文学`

---

[美] 麦克里希 / 丛文译

并在这里，低下头，在太阳下   

在这里，在正午大地的最高处   

感受那不断涌聚   

不断升起的黑夜：

感受它沿着弯曲的东方爬升   

感受黄昏里泥土的寒气以及   

从地球的另一端，那巨大   

而不断攀升的阴影缓缓地滋生

在伊克巴坦，那些奇异的树   

一叶一叶地，占据奇异的夜晚   

黑暗弥漫在它们膝下   

波斯群山渐渐黯淡

而此时，在克尔漫沙汗的城门   

几个晚归的旅人，穿行在   

黑黝的虚空和衰败的野草   

在一片微光中，向西而行

在黯淡的巴格达，大桥   

跨越沉默的河流，而消隐   

黑夜，穿越阿拉伯半岛   

偷偷地扩展它的疆域

在帕尔米拉古城，在街头   

废墟的石径上，车辙深陷   

黎巴嫩消隐了，而克里特   

高跨云端，在风中飘散

在西西里，天空   

依然闪烁着归航的鸥群   

但暗影下的船只，上面的船帆   

在朦胧中慢慢消隐

而西班牙沉没，在非洲   

金色沙滩的海岸下   

甚至夜晚消失，在这个陆地上   

再也不会有它苍白的光辉

海面上，也不再有那一道长长的余晖

在这里，低下头，在阳光下   

去感受如此迅急而神秘   

涌来的黑夜的暗影……

---

You, Andrew Marvell

And here face down beneath the sun   

And here upon earth’s noonward height   

To feel the always coming on   

The always rising of the night:

To feel creep up the curving east   

The earthy chill of dusk and slow   

Upon those under lands the vast   

And ever climbing shadow grow

And strange at Ecbatan the trees   

Take leaf by leaf the evening strange   

The flooding dark about their knees   

The mountains over Persia change

And now at Kermanshah the gate   

Dark empty and the withered grass   

And through the twilight now the late   

Few travelers in the westward pass

And Baghdad darken and the bridge   

Across the silent river gone   

And through Arabia the edge   

Of evening widen and steal on

And deepen on Palmyra’s street   

The wheel rut in the ruined stone   

And Lebanon fade out and Crete   

High through the clouds and overblown

And over Sicily the air   

Still flashing with the landward gulls   

And loom and slowly disappear   

The sails above the shadowy hulls

And Spain go under the shore   

Of Africa the gilded sand   

And evening vanish and no more   

The low pale light across that land

Nor now the long light on the sea:

And here face downward in the sun   

To feel how swift how secretly   

The shadow of the night comes on.....



---


`@bintou`
`2017-06-29 18:21:02`
`字数 16756`
`阅读 5290`


2016级《计算机科学导论》授课笔记
==================

`导论` `世间少有的扯蛋授课` `笔记`

---

*如果你是第一次看到这个笔记，请直接跳到本页面底部去，从后往前看。*

### 1、万物皆0/1

从这计算机科学的本质开讲。学“计算机科学”到底是学什么？其实，computer science不是学计算机，不是学计算机的使用也不是学计算机的制造。学的是“计算”－－computation。我理解，大家进入这个专业多数是因误解而来，从今天开始，也许需要换一下思维了。这也就是我为什么一直推荐How to Think like a Computer Scientist（HTCS）而不是其他比如C++ Primer之类的书为入门书的原因。关键不在于是否学会编程，而是要如何改变思维。

那到底什么是计算？这个问题很复杂，然后具体落实到计算机的实现上却又非常简单。这是两个问题。第一是，什么是计算！这个暂时还回答不了。第二是，怎么计算。这个可以有一个简单的初始到答案：二进制。

**“世界上有10种人，一种懂二进制，一种不懂！”**你们是其中的第一种。改变思维的第一步，就是认识二进制。

首先我们给出二进制数字的描述。

```
二进制：只有0和1两位数字，每一位我们称为一个bit（比特）。
计算规则：0+0 = 0，0+1 = 1，1+1 = 10，10+1 = 11

```

现在可以归纳一下规律了。   

0，1，10，11，...，1111，...， 这样的数字有没有遍历完所有的我们之前认识的十进制正整数？答案是，yes。

十进制数无非就是偶数和奇数两种。请问，偶数在二进制中长什么样子？答：最后一个bit为0 。

于是我们有以下规则：

```
0结尾的二进制数是偶数；1结尾的二进制数是奇数。

```

例子：   

2对应10，4，对应100，8对应1000，16对应10000

大家有没有看到10后面加个0等于是乘二？好像我们可以得出一个规律: **在一个二进制数后面补一个零等于乘二**？（注：在此处回答问题的同学基本上答案都是No！）因为这里如果考虑奇数，那么，很可能不对！但是，乘二不是在后面补零？末尾为零不就是偶数？这......

例子：

```
 十进制7 ＝＝ 二进制 111
 7*2 == 14 == 二进制 1110

```

似乎是这么个理？再演算一下其他数字......得到规则如下：

```
二进制乘2运算等于在数字末尾补一个0.

```

思考一下，乘法是补0，除法呢？我们只考虑整除，即只取整数商。

例子：   

十进制7的二进制为111，十进制7/2 == 十进制3 == 二进制 11   

十进制11的二进制为1011，十进制11/2 == 十进制5 == 二进制101

规律：

```
二进制除2运算等于在砍掉数字末尾一个数位。

```

如何把任何的二进制数转换为十进制？第一次授课结束。

### 2、思维皆递归

归纳一下之前的内容。首先，计算机科学是关于“计算”的科学，是关于“思维”的科学。然后，介绍了二进制，当然是非正式地介绍，为的是归纳出两个规则：在后补零等于乘2（扩展思考，除2怎么做？）；尾数为0的数是偶数（尾数为1的是奇数）。然后，我们需要思考的是如何在二进制数与十进制数之间进行转换。特别是，我们不要满足于怎么做，还要思考为什么。更重要的是，我们想得到一个“过程”，一个计算机可以读懂的过程。

当我们思考一个过程的时候，我们需要知道的是，输入什么，得到什么。比如，我们命名二进制转换为十进制的过程为B2D，这是一个名字。

例子：

```
function B2D(a)
输入：一个二进制数a
输出：a所代表的十进制数

```

在完成这个程序之前，我们拿些实例出来看看，比如：   

例子：

```
输入0，立即输出0；输入1立即输出1！这太简单，但是请注意，这很重要！

考虑多比特输入。比如输入：1110；输出：1110代表的十进制。根据之前的规则，补零等于乘2，所以，这个数必然是111的十进制乘2。所以，如果我们的计算结果就是2*B2D(111)。但是，如果是奇数呢？比如，输入1111 。Ok，没关系，我们照样可以得到结果：2*B2D(111)+1 ，多加个1就好了。

```

所以，我们可以完成我们的程序为：   

注意：＃代表注释！

```
function B2D(a)
＃输入：一个二进制数a 
＃输出：a所代表的十进制数
if a < = 1:      ＃递归的终止条件
    return a;    #即，当a小于等于1，原样输出。
else:           ＃否则
    return 2*B2D(a/2) + lsb(a)

```

请注意一点，我们现在只有二进制数操作的两个规则：乘2等于补零；0为偶数，1为奇数。上面这个程序违反规则了没？有啊，怎么能用除法“／”。其实，这里的除法就是把a的最后一个比特删除。而lsb(a)指的是a的最后一个比特。

这个程序中最古怪之处是：2\*B2D(a/2) + lsb(a)。因为，这里B2D这个程序自己调用了自己！！！我们把这种自己调用自己的过程称为“递归”。

**所有计算无非递归而已！所有的思维都是递归的！**

现在反过来，如果要从十进制得到二进制应该如何？我们重新来，思维运动起来！

现在我们要写一个D2B的程序，输入：a，十进制数；输出：a的二进制数。首先，我们需要得到程序的终止条件。如果 a< = 1，怎么样？输出a！然后，计算无非递归，递归起来！比如，7这个数，我们能知道它最后一个比特是什么吗？奇数，当然是1 。如果是16呢？偶数，当然是0 。就是说，对任意输入，我们至少知道了部分答案，a的最后一个比特。剩下的比特who care？交给递归啊！我们得到D2B(a')＋lsb(a)，其中a'是a删除最后一比特之后的数.呃，忘记了，a是十进制数呢？没事，除法嘛，除2。

程序：

```
function D2B(a)
# Input, a decimal number a;
# Output, the binary number of a;
if a <= 1:  ＃终止条件！
    return a;
else:
    return D2B(a/2)||lsb(a)

```

D2B(a) = D2B(a/2) || b ，这样的过程为什么会结束？也许很多同学立即会担心，递归怎么会结束呢？

为什么会终止？因为每一个递归程序都有一个终止条件。而且，每次自己调用自己的时候，参数都在减小（这很重要），这就确保了终止条件一定会到达。

递归效率低？我的回答是：思维，不在乎效率；其次，递归并不总是低效率。相信提这个问题的同学学过一些，但是，对递归对理解不能那么片面。以后继续深入。

接下来，做一个习题：

```
function fac(n)
输入：整数n
输出：n的阶乘
要求：必须使用递归

```

最后一个内容，这是世界上最有意思的问题之一。话说有两只兔子...斐波那契数列：1 1 2 3 5 8 13 21...... 请用C语言用递归的方法写出第n项斐波那契数。

```
function fib(n)
输入：整数n
输出：第n项斐波那契数
要求：必须使用递归

```

注：第二次授课结束。

### 3. 计算即递归

计算机的核心是CPU，我们总是希望这些个核心设备做尽可能少的“操作”，但是借助它又似乎无所不能。这似乎矛盾，其实又不矛盾。昨天讲到二进制的加法和乘2。然后讲到用递归的方法去思考。

今天，先延续昨天的思路，出一道题，如果没人做，以后看来也不需要上课了。今天做“乘法”：

```
function multiply(a,b)
输入: a和b，两个任意长的二进制数；
输出：a*b 。
要求：请用递归的方法，并且只能用加法和乘2操作来完成，不要写程序，用我昨天的描述方法即可。

```

有会的同学，写了可以发我Q邮箱。我11点左右来看看。然后再看看有没有然后。。。建立、改变思维方式应该放第一位，请不要小看这些似乎没用的东西。

例子：

```
11*1 ＝11；11＊0 ＝＝0；
11 * 10 ＝＝110，实际就是11乘2，即11后面补个0；如果是11 * 11？当然应该是11*10 ＋11*1，即11*(10 + 01)。
推广到任意比特的乘法：x ＊ y ＝ 2*multipy(x,y/2) ＋ x 。这里看明白了吗？递归！

```

代码：

```
function multiply(a,b)
if b ＝＝ 0：
    return 0;
if b == 1:
    return a;
if iseven(b): # the last bit of b is 0;
    return 2*multiply(a, b/2);
else:         # b is odd    
    return 2*multiply(a, b/2) + a;

```

这个乘法算法展示，计算机只要乘2和加法就可以做任何乘法，对吗？但是，我们怎么不讲除法和减法呢？

练习：

```
 既然整数a乘2是在a的后面补0，那么，整除的a除2运算应该是什么？

```
#### 二分查找法

略，以后增加！

#### GCD算法

接下来讲一个世界上最古老的算法（并没有之一）！给定两个整数a和b，求a和b的最大公因子，记为GCD(a, b)。

算法：

```
function GCD(a, b)
#input: a, b, two integers with a >= b >= 0
#output: the greatest common divisor of a and b
if b == 0:
    return a;
else:
    return GCD(b, a mod b)

```

例子：

```
求8、4的gcd，8 mod 4 ＝＝ 0；所以，递归gcd(4,0),然后返回4。
求7和3的gcd，第一步递归gcd(3,1);第二步递归gcd(1,0).结果为1。

```

定义：

```
如果整数a和b的最大公因子为1，则称a与b互素。如果对于整数a，所有小于a且大于0的数都与a互素，则称a为素数。

```

为什么算法是正确的？要证明，我们需要一个简单的中间结论gcd(a,b) == gcd(a-b,b) 。

证明：

```
  1、因为a和b的公因子肯定整除a－b，所以gcd(a,b) <= gcd(a-b,b);
  2、同时能整除a－b和b的家伙一定可以整除a和b！所以，gcd(a－b,b) <= gcd(a,b)。

```

这里利用了一种证明方法，要证明 a == b，我们只需要证明：a <= b 且 b < = a。一种非常常规的证明方式。推广，如果a和b为集合，证明这两个集合相等，只需要证明a是b的子集且b是a的子集。

为什么gcd(a,b) == gcd(a-b,b)就得到结论？因为：

```
 gcd(a,b) == gcd(a-b,b) ＝＝ gcd(((a-b)-b),b) == gcd((((a-b)-b)-b),b)== ... == gcd(a mod b, b)

```

不断对a进行减b，当然会得到a mod b。mod运算无非是a除b取余数。

GCD算法又称为欧几里德算法，是最古老的算法，然而也是目前使用最广泛的算法之一。GCD算法的一个简单扩展是目前互联网中使用最广泛的安全保密算法－－RSA算法－－的基础。

要理解递归也许我们需要更多的练习，或者阅读，不知道我以前的这份[递归讲义](http://blog.163.com/bintou_ics/blog/static/240582009201491242619258/)是否可以帮助大家？

最后要说，在计算机的实现中，加法和乘法是最本质的运算。而计算机的加法和乘法都是mod加和mod乘。这是下一次课程的内容。（第三次授课结束。）

### 4、算术都要mod（第四次上课的内容）

当我们学习某种理论体系的时候，我们往往从它的弱点开始。计算机的弱点是什么？

也许我们首先要知道，计算机所有的计算都是**有限计算**，这非常重要。什么是有限计算？我们现在只知道二进制是0/1比特串，可以进行加法和乘法（上次我们已经从乘二中得到了任意的乘法）。那么**有限**就体现在，计算机只能做有限比特的加法和乘法？这似乎有悖于我们对计算机对认识，计算机不是连围棋高手都打败了吗？是的，无论它表现得似乎无所不能，本质上，它只是做有限比特的加法与乘法。

好吧，那么有限到什么程度？也许有些计算机只能做8比特的运算，有些能做16比特或者32比特，而你们现在购买的64位机就是做64比特的运算而已。是不是有点为自己那几大千RMB感到遗憾？请大家要明白，你买32位机或者64位机，其实是说你的cpu在执行一次运算时候能做多少比特的运算。

几个概念：

```
8比特为一个byte（字节）。
C语言中的Byte类型就是8个比特的数据类型。
C语言中的char类型是8比特的字符类型。都是8比特，有什么区别吗？
C语言中的int类型是表示整数类型，32比特，即4个字节。

```

直观上，给定任意一个变量，我们可以把它看成能装n个比特的“盒子”，比如一个byte变量就是可以装8个比特的盒子。

那么，比如把37（16进制）装进盒子里，就得到：

```
0 0 1 1 0 1 1 1

```

请注意开头的3个0，这里必须写，因为我们需要把8个比特写出来。大家计算这个16进制数等于10进制的几？对它乘2等于在末尾补零，对这种形象化的说法，我们可以有更直观的认识，即把比特值向**左移动**一个比特位，得到：

```
0 1 1 0 1 1 1 0

```

除2等于向**右移动**一个比特位，在左边补零，得到：

```
0 0 0 1 1 0 1 1 

```

这些规则都是在第一章中已经归纳出来的内容，这里只是在有限计算的框架下重信陈述。同样，我们还可以重新理解这里的加法与乘法。

我们怎么再认识计算机的有限计算呢？比如，对于加法，我们可以这样玩一下：

```
byte a = 255, b = 2;
a = a + b;
printf("a ＝＝ %d", a);

```

比如，对于乘法，我们这样编程尝试一下嘛：

```
int n = 16; #你们可以尝试不同的数值；
byte a = 1；#或者尝试一下int类型；我不会告诉你们什么unsigned的！
for(int i = 1; i < = n; i++){
    a = a*2；
    printf("我这里偷个懒，你们直接输出a的值嘛，%d", a)；
｝

```

当n为什么的时候a的值会出现异常？这种异常代表什么？如果a的初始值为任意的，比如3，或者5，又会如何？

通过尝试，也许我们会发现，其实，这里的所谓加法或者乘法，只是一种mod运算，mod什么？mod的是2的某个次方，比如int类型，mod 2^32（2的32次方）。byte类型mod什么？请一定要设置特定数值进行尝试一下。

这里也许需要解释一下，经典书籍当中所谓的“溢出”。这里没有什么溢出，只是mod运算。

好了，现在我们需要了解一下mod运算的好处了。运算规则如下，希望你们中学的时候学过(*感谢15级的会智同学发现我书写的错误。我的错误一如既往地存在，请帮我改正。谢谢！*)：

```
(a + b) mod n ＝＝( (a mod n) + (b mod n)) mod n
(a * b) mod n ＝＝( (a mod n) * (b mod n)) mod n

```

这个时候，你们之前写的代码就可以这样玩一下了。如果写了factorial，不妨看看，当n变得很大时候会怎么样？比如n＝100，1000，10000......可以看到，其实mod 2^n并不好玩！（非常可惜对于我提示的这些计算，很少有同学会自觉取编程玩一下！）怎么样才好玩？我们会回来的。不过，现在我们还是先停顿一下。

之前有不少同学已经迫不及待地问到八进制，16进制。其实，这并不是很特殊到东西。如果我们把比特三位为一组去认识，就得到八进制，四位为一组去认识就得到16进制。比如：

```
000 ，001，...，110， 111，这里有多少个数？2的3次方，8个。111 + 1 == ?，1000 ？对不起，我们只有3个比特，所以是0！即，逢八进一。

同样，0000到1111，有16个数，逢16进一，是16进制。呃，这里要注意，1010，1011，到1111，这几个数还没有名字，所以，起名为A，B，...，F。没有什么特别！对吧？

```

16进制的命名：

```
 1000  为 8；  1001  为 9   #老名字，以下是新名字
 1010  为 A；  1011  为 B
 1100  为 C；  1101  为 D
 1110  为 E；  1111  为 F

```

为什么我们需要8进制，16进制，而不是3进制，5进制？[哪种进制的效率最高](http://blog.163.com/bintou_ics/blog/static/240582009201410932649868/)？

给定变量的长度我们就能立即知道这个变量所能表示数据的范围，反之，给定一个数字，我们能知道这个数值需要用多长的比特变量来表达。

例子：

```
8比特变量能表达的范围是：00 ~ FF，256个数值；
16比特能表达的范围是：0000 ~ FFFF，65536个数值；

```

例子：

```
 表达234这个十进制值需要 8 个比特；
 表达4294967295这个十进制值需要32个比特；

```

这里的一个观点是，长度n能表达的最大范围是2^n；而某个数x需要n比特进行表达，则是n ＝＝ log x （以2为底的对数）。这里的**指数与对数的对应关系**值得注意！

*第四次结束！*

### 5. 负数是什么－－兼解释什么是补码？

以上内容我故意忽略了负数，只讲正数。很多同学迫不及待提出什么是补码。其实关于补码，我看了很多书，有些讲得很复杂。其实，并没有什么可说的。

比如，我们要表示8比特的数，无非就是00到FF这256个数。01+01=02，0F + 01 = 10 。这些我们都已经懂了。现在要在8比特中同时表示负数，仅仅多这么个要求而已。那么也就一半是正数，一半是负数，一样一半，127 ＋ 127 ＝ 254 。看上去有点怪，我们不是要表达256个数吗？这么问题，稍微放下。马马虎虎先生先定下来说，大致上如此：00，不正也不负。正数是01到7F，127个。于是，我们已经有了128个数。接着，我们要问，－1是什么？

我们懂加法，那么我们一定会得到：

```
01 + FF == 00

```

我们是不是可以很高兴地说，哦，FF是-1！因为，1 + (-1) == 0。别急，我们要得到-2，-3...

```
02 + FE == 00
03 + FD == 00
...
7E + 82 == 00
7F + 81 == 00

```

所以，我们得到了-1，-2，-3，...，-127，一共127个数字，对吧？用二进制表达分别是：

```
1111,1110   代表   -2
1111,1101   代表   -3
...
1000,0010   代表   -126
1000,0001   代表   -127

```

这里担心7F + F1会溢出地同学一定要放心下来，8比特运算无论如何不会得到9比特的数值，多出来的只能扔掉。

现在我们基本已经胜利了。只是如果敏感的同学一定会发现，我们现在得到了128+127个数，但是8比特数可以表达256个数值。我们忽略了什么？80我们遗漏了。即二进制的10000000没有得到任用，它应该是什么？

首先，我们注意到，所有到负数都有一个特点，排在最左边到比特都是1。所以，这个10000000看上去应该是个负数。应该是什么呢？还是用加法试一下：

```
10000000(16进制的80) + 01111111(16进制的7F，十进制的127) + 01（十进制的1） == 0

```

某个负数加正数128等于0，所以，这个负数是-128。也就是说，80代表负的128。

至此我们已经完全胜利，这种表示负数的方式就是所谓的**二进制补码**。可以推广应用到任意长到比特负数表达。我们又把负数称为**带符号数**。在宣称胜利之后，我们还需要把之前的规则归纳一下，这就变成了所有教科书中给出的规则了。（讨厌教科书，讨厌教条主义，讨厌背诵规则的同学可以忽略以下规则。前提是，最好你有我以上把规则理解为操作的能力。）

补码规则：

```
n比特数的第n-1位为符号位，0代表正数，1代表负数。正数的表达与二进制数表达相同。负数的表达只是对正数进行取反操作，然后加1。

```

比如，还是8比特数为例：

```
08代表正8，二进制表达为00001000，那么-8就是对之前对二进制进行取反再加1。即，11110111 + 1 == 11111000，16进制表达即为F8。
7F，二进制数为01111111，-7F为：10000000 + 1 == 10000001，16进制为81。

```

**补码的好处？**使用补码，计算机中定义的加法，无论是否使用符号位，都一样操作。也就是说，在补码这里讲负数，但是加法还是原来都加法。同样，C语言中虽然允许你们定义带符号数和非带符号数，其实用到的操作是一样的。所以，你同样的一个变量，把它看成带符号数或者不带符号都可以。这个，你们完全可以通过编程来加深体会。

其实补码没有任何新东西，考虑mod 2^n的加法，比如下面等式：

```
给定n比特长的整数x，求x + -x == 0，-x就是x的负数。
x + -x == 0其实就是 x + -x == 0 mod 2^n
所以，-x == (2^n - x) mod 2^n

```

例子：

```
8比特数-7的二进制补码：
  2^8 - 7 == 249 
  00000111取反加1 == 11111001

```

不熟悉就拿笔比划一下。我认为这样教比[之前那样要好](http://blog.163.com/bintou_ics/blog/static/24058200920148281021244/)！

### 6、mod运算怎么样才有意思？

“有意思”这件事情对不同的人有不同的含义，所以，我们只能走走看。比如，如果你们可以执行这样的代码：

```
给定任意一个整数n，比如让n＝11.
for i in range(1, n):    #i循环从1到n-1
for j in range(1, n):    #j循环从1到n-1
    print ((i * j) % n), #输出 i*j mod n
print                    #只是控制换行

```

当然，你们可以用C语言来写写看。不断尝试，让n = 7，或者等于13，17 。当然，也可以尝试n等于10，20等等。

这个程序不断输出 i\*j mod n ！不看懂这个程序你往下能看到啥啊？？

关键是，看懂后，你们能归纳出什么结论吗？我想，发现规律比学到知识要重要得多。

比如，在n等于11的时候，我得到这样的输出。

```
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 1 3 5 7 9
3 6 9 1 4 7 10 2 5 8
4 8 1 5 9 2 6 10 3 7
5 10 4 9 3 8 2 7 1 6
6 1 7 2 8 3 9 4 10 5
7 3 10 6 2 9 5 1 8 4
8 5 2 10 7 4 1 9 6 3
9 7 5 3 1 10 8 6 4 2
10 9 8 7 6 5 4 3 2 1

```

似乎很容易发现，每一行只是1到n-1的重排。这是偶然还是规律？如果n取13，我们还能得到同样规律的输出吗？我们会不会得到：

```
1 2 3 4 5 6 7 8 9 10 11 12
2 4 6 8 10 12 1 3 5 7 9 11
3 6 9 12 2 5 8 11 1 4 7 10
4 8 12 3 7 11 2 6 10 1 5 9
5 10 2 7 12 4 9 1 6 11 3 8
6 12 5 11 4 10 3 9 2 8 1 7
7 1 8 2 9 3 10 4 11 5 12 6
8 3 11 6 1 9 4 12 7 2 10 5
9 5 1 10 6 2 11 7 3 12 8 4
10 7 4 1 11 8 5 2 12 9 6 3
11 9 7 5 3 1 12 10 8 6 4 2
12 11 10 9 8 7 6 5 4 3 2 1

```

如果n=12呢？得到了：

```
1 2 3 4 5 6 7 8 9 10 11
2 4 6 8 10 0 2 4 6 8 10
3 6 9 0 3 6 9 0 3 6 9
4 8 0 4 8 0 4 8 0 4 8
5 10 3 8 1 6 11 4 9 2 7
6 0 6 0 6 0 6 0 6 0 6
7 2 9 4 11 6 1 8 3 10 5
8 4 0 8 4 0 8 4 0 8 4
9 6 3 0 9 6 3 0 9 6 3
10 8 6 4 2 0 10 8 6 4 2
11 10 9 8 7 6 5 4 3 2 1

```

似乎是令人失望的结果！

**如果你并没有总结出规律，我想你暂时还是不要看下去，多思考思考，多尝试。如果你找到了规律，那请看下面。**

#### mod n运算中n为素数的情形

令n为素数：

```
任意取一个大于等于1且小于等于n-1的整数i，重复用所有大于等于1且小于等于n-1的整数j(n-1个数)对i进行mod n的乘法，即求 i*j mod n，所得的整数刚好是所有大于等于1且小于等于n-1的整数(n-1个数)的某个排列。

```

即，任取一个i之后，我们算这n-1个值：

```
i*1 mod n, i*2 mod n, ..., i*(n-1) mod n        (1)

```

得到的数刚好是（经过排列之后）：

```
1，2，3，...，n-1                                 (2)

```

我们把第(1)行的数乘起来并mod n：

```
i^(n-1) * (n-1)! mod n                                  (3)

```

把第二行的数乘起来并mod n：

```
(n-1)! mod n                                            (4)

```

我们知道(3) == (4)：

```
i^(n-1) * (n-1)! ≡ (n-1)! mod n                            (5)

```

由(5)我们可以得到（当然，我们必须问为什么？）：

```
i^(n-1) ≡ 1 mod n                                     (6)

```

这个(6)就是颇为有名的**费尔马小定理**！

这是我们需要的一个条件。有同学问这道题的答案，算了，作为习题给大家做一下。

```
if gcd(c,n)==1, and a*c ≡ b*c mod n, then a ≡ b mod n.

```

证明：略！想在“图灵班”混的同学请到“课堂派”交作业。

费尔马小定理：

```
 对于素数n，取任意大于1小于n-1的整数（此条件并不必要，为什么？），我们有，i^(n-1) ≡ 1 mod n 。

```

对于以上的推导你懂(不懂)吗？懂不值得骄傲。不懂，不如问一下自己，在哪个环节让自己失去了逻辑关联？任何人都应该懂。

费尔马小定理有什么用？这个，敬请期待......

暂时回到这个小定理的条件开始，n为素数，这是一个较强的要求，如果n为任意整数呢？我们已经知道n=12的时候，得到的结果没有n为素数时那么有规律。但是，n为合数是不是就没有规律呢？这个.....嗯？怎么办？

*第五次授课结束！*

#### mod n运算的n为合数时的情形

正如之前看到的，当n＝12，我们的程序输出：

```
1 2 3 4 5 6 7 8 9 10 11
2 4 6 8 10 0 2 4 6 8 10
3 6 9 0 3 6 9 0 3 6 9
4 8 0 4 8 0 4 8 0 4 8
5 10 3 8 1 6 11 4 9 2 7
6 0 6 0 6 0 6 0 6 0 6
7 2 9 4 11 6 1 8 3 10 5
8 4 0 8 4 0 8 4 0 8 4
9 6 3 0 9 6 3 0 9 6 3
10 8 6 4 2 0 10 8 6 4 2
11 10 9 8 7 6 5 4 3 2 1

```

是不是没有规律？呃，慢着，我看看......第1行怎么那么熟悉？慢着，似乎第5行的结果也很漂亮，因为结果就是1到11到一次重排。哦，原来第7行、第11行，结果都是1到11到一次重排。1、5、7、11都是什么数？不难看出，是与12互素的整数。似乎，规律出来了。我们是不是可以使用上一次课到方法得到：

如果i与n互素，那么i\*1 mod n，i\*2 mod n，i\*3 mod n，...，i\*(n-1) mod n是1到n－1这些数的重排。所以：

```
    i^(n-1)*(n-1)! ≡ (n-1)! mod n

```

所以，**i^(n-1) ≡ 1 mod n** ？啊，**一个新的“费尔马小定理”？！**

慢着，有点不对......因为(n-1)!并不与n互素！！！所以，我们并不可以做两边的“消去”术。似乎有点失望。那为什么费尔马小定理可以那样做？因为n是素数，1到n-1之间到所有数都与n互素。

既然如此，那么，如果n为合数，1到n-1之间的那些数与n互素？它们的相乘是不是还是与n互素？

答案是，1到n-1之间的那些与n互素的数（不就是gcd(i,n)==1 ?）的相乘确实与n互素！

现在，如果我们只考虑与n互素的数会怎么样？计算机程序就是帮助我们找规律的利器。为何不尝试用C语言写个程序看看？（虽然我给出的是Python代码。）

```
 for i in range(1, n): #1到n-1的循环
    if gcd(i, n)==1:   #如果i与n互素
        for j in range(1, n):   #1到n-1的循环
            if gcd(j, n) == 1:   #如果j与n互素
                print ((i * j) % n),  #输出(i * j) mod n
        print                    #内循环结束，输出换行

```

令n=12，程序输出是：

```
1 5 7 11
5 1 11 7
7 11 1 5
11 7 5 1

```

这是什么意思？规律是什么？看多一些数据。令n＝21，输出为：

```
1 2 4 5 8 10 11 13 16 17 19 20
2 4 8 10 16 20 1 5 11 13 17 19
4 8 16 20 11 19 2 10 1 5 13 17
5 10 20 4 19 8 13 2 17 1 11 16
8 16 11 19 1 17 4 20 2 10 5 13
10 20 19 8 17 16 5 4 13 2 1 11
11 1 2 13 4 5 16 17 8 19 20 10
13 5 10 2 20 4 17 1 19 11 16 8
16 11 1 17 2 13 8 19 4 20 10 5
17 13 5 1 10 2 19 11 20 16 8 4
19 17 13 11 5 1 20 16 10 8 4 2
20 19 17 16 13 11 10 8 5 4 2 1

```

请注意每一行开始的那个数字与n的关系！可以考虑30分钟再往下看。

规律：

```
一个与n互素的整数i，它分别与所有大于等于1、小于n且与n互素的整数相乘（mod n），所得的整数是所有大于等于1、小于n且与n互素的整数的排列。

```

记大于等于1、小于n且与n互素的整数的**个数**为phi(n)。记大于等于1、小于n且与n互素的整数的相乘为Pi(n)。利用在求费尔马小定理时的技巧:

```
i^phi(n) * Pi(n) ≡ Pi(n) mod n
即：i^phi(n) ≡ 1 mod n

```

这个公式就是大名鼎鼎的**欧拉定理**！当n为素数，那么phi(n) == n-1。所以，费尔马小定理只是欧拉定理的一种特殊情形。

**欧拉定理**：

```
若n，a为正整数，且 gcd(a,n)==1}，则 a^phi(n) ≡ 1 mod n.

```

注：

```
phi(n) = phi(n1)*phi(n2), if n == n1 * n2。

```

如何证明？略！

注意，无论是费尔马小定理还是欧拉定理，这里都没有严格证明。请有兴趣的同学自己完成。

#### mod n指数运算

给出i，j和n，求i的j次方，记住我们任何运算都必须mod n。i的j次方mod n，记为 i^j mod n，或者 i\*\*j mod n。求i^j mod n应该怎么做？

```
似乎有点难？这个是图灵班先修班作业！

```

在思考这个问题的时候，还是要找规律。比如，从最简单的思路开始，求i^j mod n，无非就是i\*i mod n做j次。一个循环就做完了。然后，你也许会想到（必须要想到），比如，i的8次方并不需要做8次乘法，因为只要知道了i^4，对i^4做一次平方就得到了i^8。至此，你至少知道求i的j次方并不需要做j次乘法，因为有中间结果可以利用。

再考虑几个例子，如果求i^10 mod n 如何？只需要对i^5 mod n求平方。如果是求i^11 mod n呢？只需要对i^5 mod n求平方再乘一个i。讲到这里，联想之前的乘法，我们是否可以得到些什么？能写出递归式吗？

```
    exp(i, j, n)
    #Input: three integers, 
    #Output: i^j mod n
    #递归初始步
    if j == 0:
        return 1;
    if j == 1:
        return i % n;
    #否则，展开递归步
    tmp = exp(i, j/2, n)
    if j is even:
        return tmp*tmp % n
    else:
        return (tmp*tmp % n) * i mod n

```

我们从i^2开始列这样一个表，统计计算i^j的所需的乘法次数。

```
i^2          1次乘法
i^3          2次乘法
i^4          2次乘法
i^5          3次乘法
i^6          3次乘法
i^7          4次乘法
i^8          3次乘法
......
i^1024       ??次乘法

```

由这个表，我们可以得到求i^j mod所需乘法数与i，j，n这三个参数的哪一个相关，且关系是什么？

使用指数运算来继续寻找规律。这次我们练习使用一下指数运算。你们能把以下代码写成C语言的程序吗？

```
for i in range(1, n):
   for j in range(1, n):
       print i**j % n,       ＃调用自己编写的exp(i, j, n)
   print

```

这段代码的含义是什么？请自己C语言编程实现。

先看mod素数的情况，令n = 7，得到输出为：

```
1 1 1 1 1 1
2 4 1 2 4 1
3 2 6 4 5 1
4 2 1 4 2 1
5 4 6 2 3 1
6 1 6 1 6 1

```

能看出什么吗？再取大一点的数字，令n = 11，得到输出如下：

```
1 1 1 1 1 1 1 1 1 1
2 4 8 5 10 9 7 3 6 1
3 9 5 4 1 3 9 5 4 1
4 5 9 3 1 4 5 9 3 1
5 3 4 9 1 5 3 4 9 1
6 3 7 9 10 5 8 4 2 1
7 5 2 3 10 4 6 9 8 1
8 9 6 4 10 3 2 5 7 1
9 4 3 5 1 9 4 3 5 1
10 1 10 1 10 1 10 1 10 1

```

能看出什么？既然我们之前都在看1到n-1的排列，你们能先找出是1到n-1的排列的哪几行吗？

至少我们可以知道：

```
 存在某些数i，i^1, i^2, i^3, ... , i^(n-1), 在mod n运算下，刚好是1到n-1的排列。

```

慢着，这是n为素数的情形。为什么不尝试一下n为合数的情况呢？比如，令n=8。得到：

```
1 1 1 1 1 1 1
2 4 0 0 0 0 0
3 1 3 1 3 1 3
4 0 0 0 0 0 0
5 1 5 1 5 1 5
6 4 0 0 0 0 0
7 1 7 1 7 1 7

```

我们并没有发现有一个i可以通过指数运算刚好恢复出所有的1，2，...，n-1。mod素数情况下存在这样的i，mod合数的情况下不一定存在。因此，我们只能把刚才的结论修订为：

在mod n运算下（n为素数），存在某些数, 刚好是1到n-1的排列。此时，把满足这个属性的  称为mod n的原根。或者称这些i为群的生成元。

在没有涉及群的概念时，我们大概只需要知道通过指数运算，i **生成** 了n-1个数。换个角度，如果我们给定生成元i，然后选任意一个大于1小于n的数j，我们如何能求出x，使得 i^x ≡ j mod n ? 注意，n为素数。我们把这种求x的过程称为求**离散对数**。其实并不难理解，回想一下中学所学到的对数：

***求, 即求，使得.***

离散对数的区别无非是多了一个mod n。**编个程序求离散对数问题将是你们的作业。**

### 7、计算机擅长做什么？

我总认为，如果你是计算机新手，首先要问的是计算机**不能做什么**，而不是现在大家普遍问的，“如何成为计算机高手”，“学计算机如何就业”。当然，这个问题非常难回答。其次，你应该问计算机**最擅长做什么**，而不要把计算机想象得无所不能，干什么事情都一副吃苦耐劳轻而易举的模样。

这样问的意思是，我们之前学过的算法，计算机是否都可以同样的效率来完成。讲到效率，我们当然是指计算机完成任务所需的时间。但是，为了陈述一种普遍的通用的结论，实际上我们通常用计算机完成某项任务所需执行的（主意）步骤来衡量计算效率。因为，针对特定计算机去计算执行任务的时间往往无法说明问题。例如，我们说求整数a、b的最大公因子需要1秒钟的时间，那么我们到底是指什么型号的计算机呢？而且输入数据到底有多大呢？大家总不能指望超级计算机与个人电脑使用相同的时间吧？也总不会任务无论多大的数据用时都相同。

因此，我们衡量算法效率的方法是要给出以下两大因数的关系：输入数据的大小n，还通常是输入数据的比特长度；在数据大小为n下，完成任务所需要执行的计算步骤。我们还通常称算法的效率为“**算法复杂性**”。

例子：

```
 求n!的算法factorial，输入大小为n，要计算n!，我们反复迭代进行乘法，n*(n-1)*(n-2)* ...* 2，需要n-2个乘法。所以我们任务这个算法的效率是O(n)。

```

记号O：大O表示法(可读为Big O)。

```
O可以理解为一个函数，O(f(n))表示是函数f(n)的上界。

```

所以，O(n)表示执行算法最多用n步（这是不准确的表示，暂时如此）。

习题：

```
 GCD算法的算法复杂性可用大O表示法表示为什么？
 exp算法的算法复杂性可用大O表示法表示为什么？

```

O的括号里面的函数可以分别是：常数、对数、线性、多项式、指数等，常数复杂性通常表示为O(1)，其他函数可以是：

```
 $log(N)$，$sqrt(N)$，$N$，$N^2$，$2^N$ ，$N!$

```

大家可以看到，以n为参数的这些函数的“大小”是不一样的，从左到右逐步增大。当我们说某个算法的计算复杂性是O(f(n))，我们是指，目前所能找到**最好的算法**所需要的计算复杂性是以f(n)为上界。

#### 素性判定

输入一个整数n，如果它是素数则输出为True，否则输出为False。最简单的方法就是不断用小于根号n的整数去除n，如果可以整除，则非素数。具体的做法当然是循环迭代，代码如下：

```
＃输入一个比3大大整数
def is_prime(n):  
＃不断用大于等于2，小于根号n的整数去除n
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        return False #可以被整除
return True

```

这个算法很普通，然而我们要考察其复杂性。因为输入是n，所以，for循环中执行的除法与判断是sqrt(n)步。我们的结论是素性判定算法的复杂性是？

结论似乎没问题。换一个角度看，通常我们对某个特定的整数n并没多大兴趣，我们反而是对某个特点长度的数字比较感兴趣。比如，我们不关心354224848179261915075是否素数，而通常关心一个有1000比特那么长的数，我们能否判定它是否素数。这里是说，我们关注n的比特长度。n的长度为l，n与l的关系是什么？n是小于的一个数，注意，这里是一个指数！所以，复杂性是，即当l增加，判断步骤指数式增加。我们把is\_prime的复杂性称为伪多项式的。

问题来了，我们能否有一个“真”多项式的算法判定某个数是否素数呢？

### 8、算法是核心

算法是计算机科学的核心，这个说法只能追溯到20世纪80年代，Knuth的TAOCP诞生之后。

我个人认为，算法导论（CLRS）是计算机新手必须尽快学习的一门课程。在过去的若干年我重复呼吁大家学习CLRS，在发现只有呼吁不够之后，我在14级展开了读书指导活动，尤其以15级的开展最为热烈。这份[CLRS授课笔记](https://www.zybuluo.com/bintou/note/196326)记录了当时的进展与问题。

加入图灵班的第一个重要任务就是与一群热血青年共同研读CLRS。希望这个任务可以在16级更好地完成。

大部分同学不缺乏对成功的渴望，缺乏的是潜心静气对基础知识的研读。请相信我的指导是正确的，你们只需要在这条道路上迈开坚实的步伐。

### 9、继续找规律

找规律远比知道一个规律要重要。学会编程，计算机可以帮助我们找到一些规律。请大家尝试编程做以下练习。

给定一个素数p，它可能是4n+1或者4n+3的形式，n是一个小于p的整数。比如，7 ＝ 4\*1+3，13 ＝ 4\*3+1。给定一个范围，比如100，1000，10000，请分别统计在范围内的这两种类型的素数的个数。也许你会得到一个结论。但是，这个结论是真的吗？为什么？能证明(证伪)吗？

给定一个素数p，对1到p-1之间的数i做平方再mod p。统计平方数中到底出现了多少个不同的数字？多试几个素数，也许你会得出一个结论。这个结论是对的吗？为什么？能证明？

### Appendix 1 大0新生看这里

总结一下新生的几个毛病：   

第一，自学能力差。   

第二，主动学习能力差。   

第三，都着急想出成绩，有理想，可是比较虚。   

第四，听到很多的意见，分辨不出好坏。   

第五，参加过多的社团活动，让自己忙得要命，分身乏术。

### Appendix 2 新手看这里

斌头老师这2014级《计算机科学导论》课上的一份[博客](http://blog.163.com/bintou_ics/)，里面的文章也许有些帮助。大家有空可以看看。其中关于数学、关于英语的阅读的一些建议，还是希望你们可以听听。[CS毕业生应具备的特质](http://user.qzone.qq.com/1626344361/blog/1398223530)。[CS2013第6章节选－计算机科学的数学要求](http://user.qzone.qq.com/1626344361/blog/1398181567)

新手入门从[我的建议](https://www.zybuluo.com/bintou/note/130334)开始。

推荐电子书：《[计算机科学基础](http://www.ituring.com.cn/book/1019)》。

课堂派中“[2016图灵班先修班](http://www.ketangpai.com/)”课程网站，邀请码：E2YJNK。[什么是图灵班](https://www.zybuluo.com/bintou/note/130481)？

### Appendix 3 关于本次授课的解释

大家好。说一下自己的看法。这两天可能给大家带来了一点困扰。我明白，可能很多同学看不懂。声明一下，不懂都是我的错，不怪你们。这些知识以后将对你们非常简单。只是我迫不及待地想看一下大家是否可以接受。所以，有不明白，不是你们的错。我讲解有跳跃，你们没看课本，加上Q群上教学也不方便，交流有困难等等因素，都带来了理解上的困难。一定一定要记住：没关系！千万不要想多了，什么完全不懂啊，自己不适合啦，其他同学懂得好多啦。没这些事情。我要是能有所帮助，我很高兴。要是没帮助，直接忽略我。我可能没做错的就是让你们看书。总结一句：多阅读，为即将来袭的大学生活做更充分的准备。如果能做到这一点，我将非常高兴。

### Appendix 4 你们的语文是不是计算机老师教的？

不是就太可惜了！如果你们的语文是我教出来的，那一定很棒！希望以后你们可以骄傲地宣称：我地语文是斌头老师教滴～

胡诗娴已经乐呵呵地宣传：斌头老师开始讲形容词了......主要是还太不了解我！

写作文，首先要客观！客观，就是要忘我，不要以个人感情来替代准确的表达、严格的论证。

其次，写作文一定要少用形容词，不要用成语和名人名言！

第三，写作文不要用套路！什么“随着社会的发展”或者“with the development of” 都是要给不及格的。

第四，写作文要禁止喊口号！

第五，现在懒得写！

### Appendix 5 留言

经过一个星期所谓的QQ授课，也该停止折腾了。一个星期来，提问的同学凤毛麟角，这是颇在意料之中，但是也是非常不愿意看到的局面。看来，老师求大家学的局面将持续保持，而主动求学的同学实在是少。也许有同学看了不服气。不服就不服，走着瞧。

这里的内容持续更新。课堂派的作业持续增加。想学的就看，有问题就Email见吧。

我说过，我在CS一呆就是20多年。现在所做的都不是什么心血来潮的事情，现在所见的学生无论有多优秀或者多糟糕都不会令人惊喜或令人失望或者......其实我是想说，无论你们怎么样，我都这个样！我懂你们，尽管你们不懂我。

不要跟我说你是小白，我反正不会同情。不要跟我说你不懂，我对“不懂”无能为力。不要跟我说你不想努力，你肯定做不了不努力的第一人。不要跟我说你很努力很有理想，talk is cheap，说的用处不大，拿出行动才是正道。

### Appendix 6 建议新生工作系统

1、电脑随便买一台，虽然你们都不是随便的人。最好买Mac book！

2、重点是要装Linux（Macbook就免了，只是千万别Macbook上装个Windows！），Ubuntu是新手的不错选择。上网下载安装。[为什么要完全工作在Linux下？](http://user.qzone.qq.com/1626344361/blog/1447647666)

3、是否可以虚拟机？是否一定要双系统？这不是关键，看着办。建议不要用虚拟机。

4、gcc编程，结合Think like a computer seientist，边看边动手。随便一个编辑软件：Atom、Emacs、Vim。

5、git＋hexo，搭建一个博客，[这是指南](http://user.qzone.qq.com/1626344361/blog/1401614489)。

6、自己练习一下Python，有Think like a computer scientist版本的电子书，网上一大把。第二版很不错。

7、[Sage](http://www.sagemath.org/)！CSers的好朋友。

### Appendix 7 你们的英语是体育老师教的吗？

同学们，你们还记得在幼儿园的时候自己背出了26个英文字母之后沾沾自喜向妈妈炫耀的情形吗？离你能背26个英文字母的那一刻到现在估计有个10-15年了吧？

这个月也许我听得最多的是，“我是小白”，“我英语好烂”。这种主观陈述意义不大。奇怪的是，每年我们的大一新生也最喜欢说这两句，我都听腻了。于是我就问，你们高考不是考了？你们应该学了啊。回答：都用来应付考试。我怎么知道不是应付考试，但是现在考完了，该用了啊。回答：没学好。**学啊！**

好吧，其实以上是可以忽略的废话。

正确的观点是：你们必须学习英语，并熟练地运用英语。其潜台词是，你们的英语都还不足以应付未来的需要。所以，最正确的建议就是，抛开高中英语学习模式，进入实战模式，即，在实际工作学习中使用英语、学习英语。我坚持大家需要英语课本的原因：

1、你们继续需要学习英语、考英语。   

2、你们需要在未来的学习工作中使用英语。   

3、目前有非常优秀的英语资料；未来最前沿的科技文献也将以英文的形式出现。   

4、中文的教材往往缺陷较多。

关于英语阅读我写过[一篇小文章](http://blog.163.com/bintou_ics/blog/static/2405820092014828111732873/)，希望有所帮助。

有兴趣的来Email联系！



---


`@bintou`
`2015-07-13 17:46:58`
`字数 1756`
`阅读 3569`


一位理工科老师的阅读推荐
============

`推荐` `阅读` `书单`

---

如果你觉得需要改变什么，但是又不知道做些什么，那就阅读吧。以下书目很庞大，你可以先考虑黑体字的作品。

以下分类是我的随便折腾出来的，大家见谅。每位作家列举一两部是因为我书架里只有这么些。

古典长篇小说
------

1. 维克多雨果 **《九三年》**、《悲惨世界》
2. 塞万提斯 **《堂吉诃德》**
3. 托尔斯泰 《战争与和平》、《安娜.卡列尼娜》
4. 司汤达 《红与黑》 《帕尔马修道院》
5. 狄更斯 《远大前程》 、《大卫.科波菲尔》
6. 福楼拜 《包法利夫人》
7. 梅尔维尔 《白鲸》
8. 拉伯雷 《巨人传 》
9. 乔叟 《坎特伯雷故事 》
10. 奥维德 《变形记》
11. 曹雪芹 **《红楼梦》**（排名不分先后！）

**注0**: 如果我说梅尔维尔的《白鲸》是福克纳的 《我弥留之际》、托妮.莫里森 《所罗门之歌》、麦卡锡 《血色子午线》等书的父亲，你知道我在说什么吗？不知道？噢，其实，我也只是随便问问，我也不知道！又据说胡安.鲁尔福的 **《佩德罗.巴勒莫》**是马尔克斯 **《百年孤独》**的父亲。

现代长篇小说
------

1. 马尔克斯 **《百年孤独》**《霍乱时代的爱情》 《族长的秋天》
2. 帕维奇 《哈扎尔词典》
3. 胡安.鲁尔福 **《佩德罗.巴勒莫》**
4. 毛姆 《月亮与六便士》、《刀锋》、《面纱》《人性的枷锁》
5. 托马斯.曼 《魔山》
6. 纳博科夫 《洛丽塔》
7. 帕斯捷尔纳克 《日瓦戈医生》
8. 普鲁斯特 《追忆似水年华》
9. 吴尔芙 《达洛维夫人》
10. 福克纳 **《喧哗与骚动》**《我弥留之际》
11. 托妮.莫里森 《所罗门之歌》
12. 卡夫卡 《城堡》 《审判》
13. 麦卡锡 《血色子午线》
14. 迈克尔·坎宁安《时时刻刻》
15. 乔伊斯 《尤利西斯》
16. 品钦 《万有引力之虹》《拍卖四十九批》
17. 雅﹒哈谢克《好兵帅克》
18. 约瑟夫・海勒《第二十二条军规》
19. 菲茨杰拉德《了不起的盖茨比》
20. 村上春树《挪威的森林》《世界尽头与奇异仙境》
21. 塞林格 《麦田里的守望者》
22. 陀思妥耶夫斯基 《卡拉马佐夫兄弟》《罪与罚》《白痴》
23. 帕特里克·莫迪亚诺 《暗店街》《青春咖啡馆》
24. 阿兰·罗伯-格里耶 《橡皮》《嫉妒》

短篇小说
----

1. 博尔赫斯 **《博尔赫斯短篇小说集》**
2. 卡夫卡
3. 契科夫
4. 莫泊桑
5. 欧亨利
6. 塞林格 《九故事》
7. 胡里奥.科塔萨尔 **《动物寓言集》**
8. 爱丽丝.门罗 《逃离》
9. 雷蒙德.卡佛 《大教堂》 《当我们谈论爱情的时候我们在谈论什么》
10. 巴别尔 **《骑兵军》**《敖德萨故事》

诗歌长篇
----

1. 荷马 《荷马史诗》
2. 弥尔顿 **《失乐园》**
3. 但丁 《神曲》
4. 歌德 《浮士德》
5. 里尔克 《杜伊诺哀歌》
6. 奥兹 《一样的海》
7. 艾略特 《荒原》

戏剧戏曲
----

1. 王实甫 **《西厢记》** （金圣叹点评版）
2. 莎士比亚 《哈姆雷特》
3. 王尔德
4. 易卜生
5. [法] 萨缪尔·贝克特 《等待戈多》

读书随笔
----

1. 毛姆 《毛姆读书随笔》
2. 伍尔夫 《伍尔夫读书随笔》
3. 布鲁姆 **《读什么，为什么读》**
4. 卡尔维诺 **《为什么读经典》** 《新千年文学备忘录》
5. 博尔赫斯 **《博尔赫斯谈艺录》**
6. 黑塞 《读书随感》
7. 夏尔.丹齐格 《为什么读书--毫无用处万能文学手册》

科普
--

1. **哥德尔，艾舍尔，巴赫：集异璧之大成** （简称：GEB ；作者：道·霍夫斯塔特）
2. 逻辑的引擎 （作者：马丁.戴维斯）
3. 通往实在之路 （作者：罗杰.彭罗斯）
4. 皇帝的新脑 （作者：罗杰.彭罗斯）
5. 哥德尔证明 （作者：内格尔 /纽曼）
6. **从一到无穷大** （作者：G. 伽莫夫）
7. 数学：确定性的丧失 （作者：M·克莱因）
8. 莎士比亚.牛顿和贝多芬 （作者：S.钱德拉塞卡）
9. 爱因斯坦·毕加索：空间、时间和动人心魄之美 （作者：米勒）
10. 费尔马大定理：一个困惑了世间智者358年的谜（作者：西蒙.辛格）
11. 一个数学家的辩白（作者：哈代）
12. **最迷人的数学趣题**（作者：彼得温克勒）
13. 图灵的秘密 （作者：Charles Petzold ）
14. 天才引导的历程（作者: William Dunham ）
15. 什么是数学 （作者: Richard Courant / Herbert Robbins / Ian Stewart ）
16. 啊哈，灵机一动 （作者: [美] 马丁·伽德纳 ）
17. 上帝掷骰子吗？（作者：曹天元）
18. 苏菲的世界（[挪威]乔斯坦·贾德）
19. 自私的基因（道金斯）
20. 枪炮、细菌与钢铁 （戴蒙德）
21. 数字情种--埃尔德什传 （作者: [美] 保罗·霍夫曼 ）
22. 知无涯者 （ 作者: 罗伯特·卡尼格尔 ）
23. 研究之美 （作者：高德纳 ，我对这个译名非常不满，原名叫：Surreal Number）

**注1**：没有选择足够多中国作家，一定是且仅仅是因为我见识短浅。如果这里没有列出你喜欢的著作，肯定是我犯了某种错误。   

**注2**：黑体字代表推荐中的推荐，每类选三或选一。   

**注3**：在所列出的小说中，最有文化的当属托马斯.曼的《魔山》。21世纪的中国应该不会有很多人看这本书，希望在22世纪得到重视吧。完全不能用于消遣的一本小说。

2015年7月整理.



---


`@bintou`
`2020-09-24 19:13:35`
`字数 3721`
`阅读 1612`


短评《THE CATCHER IN THE RYE》
==========================

`书评`

---

### 前言

我知道，许多人不喜欢《THE CATCHER IN THE RYE》。太正常了，其实《麦田里的守望者》这个标题的翻译就是让人误解。翻开整本书，全篇都是粗言秽语、絮絮叨叨、各种对现实的不满等等，整篇无非就是一个不良少年逃学记而已，Not a big deal！更何况如果译者序或出版前言中包括“*本书揭露了资本主义社会腐朽的精神文明本质*”等**尖锐深刻**的解读，读者不喜欢就太正常了。我首次读的时候也不喜欢，因为那时我很正常。

以下试图以几个未经充份论证的“事实”来说明这部作品的优越性，通过讨论来帮助大家认识这部作品。

### 事实1. 相关主题下的最佳作品

如果你感到疑惑，为何这部小说大名鼎鼎，得到了无数的好评，能成为经典？要说列举理由的话也许很难，但是要说一个事实的话，似乎就比较简单，而难以反驳。这么说吧，在人类的文学史中，有哪一本小说讲“青春”、“教育”能如这本那么深刻、感人、有力？浅薄如我，我真找不到在这方面可以与之匹敌的小说。故此，它自有其应有的地位。

不要拿它与《红楼梦》、《战争与和平》、《生存与命运》、《魔山》、《百年孤独》等经典去比，没有可比性。不过，即使不考虑该小说的题材、背景等因素，两大特点也会让它屹立于世界文学之林：**现实感、诗意**。

### 事实2. 主人公性格特征的普遍性及特殊性

客观地说，主人公Holden当然有非常令人可喜的优点，甚至可以说极具人格魅力。尽管如此，从最肤浅的认识上看，他确实就是一个让人讨厌的小混混，其鲜明特点就是：满嘴的污言秽语，一肚子的怨气，对任何事物都表示不满。

然而，考虑整本小说的主题：青春。难道这个世界上的年轻人不都是对现实充满了不满的一个群体吗？青春期的叛逆比比皆是，何必大惊小怪。既然如此，极力渲染一下Holden的各种不满、怨气，只不过是对现实的一种艺术性表达而已啊。

也许你读到这里会站出来抗议，“我就是一个年轻人，我就没有类似Holden的那种怨气！”那我只能恭喜你，好孩子！其次，我也只能遗憾地说，你没有Holden的怨气，也就缺少了Holden的善良。善良、忧郁、悲天悯人就是Holden的性格上的特殊性。这种普遍性与特殊性共同塑造了一个血肉丰满的中学生形象。

### 事实3. 主人公性格特征的多样性与融合性消解了所谓的对立性

作者通过故事表达了其对青春期叛逆的态度与策略。其中这一段被广为引用：

> What I have to do, I have to catch everybody if they start to go over the cliff--I mean if they're running and they don't look where they're going I have to come out from somewhere and catch them. That's all I'd do all day. I'd just be the catcher in the rye and all. I know it's crazy, but that's the only thing I'd really like to be. I know it's crazy.

多数读者将其解读为，“教育者应该对青春期的孩子保持一种守望者（Catcher）的态度”。但是请读者不要忘记，说这句话的人，或者说保持这种理想的人就是主人公Holden。而这个Holden在故事中就是那个“要掉下山崖”的小孩。因此，“教育者”与“被教育者”没有对立起来，“拯救者”与“被拯救者”没有对立起来，而是巧妙地融为一体。这样的融合在全书当中多次出现，实属非常巧妙的表现艺术。

主人公Holden体现出若干矛盾的性格，我称为矛盾的融合。也许大家都记得Holden满嘴喷脏话，可是大家是否记得Holden在他妹妹的学校看到“F\*\*k you”这种脏字时的反应呢？首先他想：

> It drove me damn near crazy. I thought how Phoebe and all the other little kids would see it, and how they'd wonder what the hell it meant, and then finally some dirty kid would tell them--all cockeyed, naturally--what it meant, and how they'd all think about it and maybe even worry about it for a couple of days.

然后呢？这个满嘴脏话的孩子对脏字也无法容忍，他要消灭“脏字”，他又一次成为战斗者：

> But I rubbed it out anyway, finally.

之后在博物馆帮助两位逃学的小朋友参观木乃伊的那一段，Holden又发现了一个可怕的“F\*\*k you”，他觉醒了：

> That's the whole trouble. You can't ever find a place that's nice and peaceful, because there isn't any. You may think there is, but once you get there, when you're not looking, somebody'll sneak up and write "Fuck you" right under your nose.

准确地说，他早在妹妹的学校就明白了：

> It's hopeless, anyway. If you had a million years to do it in, you couldn't rub out even half the "Fuck you" signs in the world. It's impossible.

Holden这个需要被拯救的孩子一直在扮演拯救世界者的角色，虽然他的“战斗”总以失败告终，他无助，他知道不可能，他只是固执地选择抗争。最终他没能离家出走，说不清是因为妹妹这个天使拯救了他，还是因为他需要拯救妹妹从而拯救了自己。没有对立，只有融合。

### 事实4. “守望”是一种高超而又独特的教学理念

“守望”态度在全书中通过不同的场景进行了多次的阐释。除了上文给出的引文，还包括，Holden出逃的晚上在出租车上与司机关于鸭子与鱼的讨论：

> "If you was a fish, Mother Nature'd take care of you, wouldn't she? Right? You don't think them fish just die when it gets to be winter, do ya?"

又比如这一段，Holden与其前任教师在晚上关于某位同学的一次对话：

> I mean you can't help it sometimes. What I think is, you're supposed to leave somebody alone if he's at least being interesting and he's getting all excited about something.

还包括在游乐场中妹妹玩旋转木马时Holden的思考：

> All the kids kept trying to grab for the gold ring, and so was old Phoebe, and I was sort of afraid she'd fall off the goddam horse, but I didn't say anything or do anything. The thing with kids is, if they want to grab the gold ring, you have to let them do it, and not say anything. If they fall off they fall off, but it's bad if you say anything to them.

这些对话都与“守望”的理念一致，可视为不同角度的阐释。更往大了说，这也与在中国古典中所谓的“无为之教”异曲同工。作为一名教学工作者，对此深以为然也！“无为”并非无所作为，每一位教学者都尽其所能地做自己的工作，其应有这样的觉悟：对某些事物保持不作为。在小说的最后，作者的这一段劝喻，可作为对“教育”的一个重要注解。

> Many, many men have been just as troubled morally and spiritually as you are right now. Happily, some of them kept records of their troubles. You'll learn from them--if you want to. Just as someday, if you have something to offer, someone will learn something from you. It's a beautiful reciprocal arrangement. And it isn't education. It's history. It's poetry.

### 小结

2017年5月底重读此作品，有感而匆匆写下以上短评。二十年的从教生涯告诉我，认真地教诲学生最终就是认真地教诲自己，所谓对学生的救赎无非就是对自己对救赎。不是否认教学、教育对学生的影响，而是需要强调这种教育的“相对性”。当这种“教育”与“被教育”完美融合，那么：**It's history. It's poetry.**

![麦田里的守望者](http://upload-images.jianshu.io/upload_images/52389-d2fab3e92eb62084.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2017.06.04晚起草   

2017.06.05晚修改



---


`@bintou`
`2022-09-01 18:24:51`
`字数 284`
`阅读 1985`


《计算机安全学》课程推荐代码
==============

`密码学` `安全学` `代码` `推荐`

---

以下推荐仅出于教学目的。也作为本人的学习记录。

### 课程

* [MIT公开课-- 网络与计算机安全](https://ocw.mit.edu/courses/6-857-network-and-computer-security-spring-2014/)
* [MIT公开课-- 计算机系统安全](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/)
* [UCB CS 161-- 计算机安全](https://textbook.cs161.org/)

### 密码算法库

* [libsodium](https://github.com/jedisct1/libsodium)
* [tinyCrypt](https://github.com/intel/tinycrypt)
* [OpenSSL](https://github.com/openssl/openssl)

### 加密软件

* [encpipe](https://github.com/jedisct1/encpipe)
* [age](https://github.com/FiloSottile/age)

### 签名软件

* [ed25519](https://ed25519.cr.yp.to/index.html)
* [Minisign](https://github.com/jedisct1/minisign)
* [FastECDSA](https://github.com/AntonKueltz/fastecdsa)

### Hash

* [TinySHA3](https://github.com/mjosaarinen/tiny_sha3)
* [HashlibExamples](https://www.programcreek.com/python/example/8674/hashlib.sha384)

### Password Hashing

* [Password Hashing Competition](https://password-hashing.net/)
* [Argon Online](https://argon2.online/)
* [Password Hashing: Scrypt, Bcrypt and ARGON2](https://medium.com/analytics-vidhya/password-hashing-pbkdf2-scrypt-bcrypt-and-argon2-e25aaf41598e)

---


`@bintou`
`2018-10-16 05:23:03`
`字数 1916`
`阅读 1990`


CINTA相关代码
=========

`代码`

---

> 以下代码用于CINTA的学习，建议大家自己敲代码，不要Ctrl c+ Ctrl v 。

### Multiplication and Power

```


1. # Simple mul
2. # Input unsigned integers a and b
3. # Output a * b
4. def multiply(a, b):
5. result = 0
6. #terminate when b == 0
7. while (b != 0):
8. # check if b is even or odd
9. if (b % 2):
10. result += a
11. # b / 2
12. b = b >> 1
13. # a *= 2
14. a = a << 1
15. return result
17. # Fast power
18. # Input: integer a, b
19. # Output a^b
20. def power(a, b):
21. result = 1
22. while (b != 0):
23. # check if b is even or odd
24. if(b % 2):
25. # b is odd
26. result *= a
27. b = b / 2
28. a *= a
29. return result

```
### EGCD

```


1. # Input: integers a and b, with a > b .
2. # Output: d=gcd(a,b), and
3. # r and s s.t. d = a*r + b*s
4. def egcd(a, b):
5. r0, r1, s0, s1 = 1, 0, 0, 1
6. while(b):
7. q, a, b = a/b, b, a%b
8. r0, r1 = r1, r0 - q*r1
9. s0, s1 = s1, s0 - q*s1
10. return a, r0, s0

```
### The Binary Euclidean Algorithm.

```


1. # Function to implement Stein's Algorithm
2. # Input: positive integers a and b, with a > b .
3. # Output: the greatest common divisor of a and b.
4. def binary_gcd( a, b):
5. # Finding 'k', which is the greatest power of 2
6. # that divides both 'a' and 'b'.
7. k = 0
8. while(((a | b) & 1) == 0) :
9. a = a >> 1
10. b = b >> 1
11. k = k + 1
12. # Dividing 'a' by 2 until 'a' becomes odd
13. while ((a & 1) == 0) :
14. a = a >> 1
15. # From here on, 'a' is always odd.
16. while(b != 0) :
17. # If 'b' is even, remove all factor of 2 in 'b'
18. while ((b & 1) == 0) :
19. b = b >> 1
20. # Now 'a' and 'b' are both odd.
21. #Swap if necessary so a <= b
22. if (a > b) :
23. a, b = b, a  # Swap 'a' and 'b'.
24. b = (b - a)      # b = b - a (which is even).
25. # restore common factors of 2
26. return (a << k)

```
### Pruduct tree

对比以下两个数列求积算法，说明并验证它们的效率。   

第一个算法逐个元素相乘；第二个算法使用递归，把元素分成两组分别进行相乘。除了理论分析，最好有实验数据。

```


1. # Input: Given a sequence of number X
2. # Output: The product of all the numbers in X
3. def product1(X):
4. res = 1
5. for i in range(len(X)):
6. res *= X[i]
7. return res

```
```


1. # Input: Given a sequence of number X
2. # Output: The product of all the numbers in X
3. def product2(X):
4. if len(X) == 0: return 1
5. if len(X) == 1: return X[0]
6. if len(X) == 2: return X[0]*X[1]
7. l = len(X)
8. return product2(X[0:(l+1)//2]) * product2(X[(l+1)//2: l])

```
```


1. def producttree(X):
2. result = [X]
3. while len(X) > 1:
4. #prod is a build-in function in Sage.
5. X = [prod(X[i*2:(i+1)*2]) for i in range((len(X)+1)/2)]
6. result.append(X)
7. return result

```
```


1. #Input: a, b, n
2. #Output: x, s.t. ax \equiv b (mod n)
3. def modular_linear_equation_Solver(a, b, n):
4. res = []
5. (d, x, y) = xgcd(a, n) #egcd in Sage.
6. if d.divides(b):
7. x0 = (x*(b//d)) % n
8. for i in range(d): #i from 0 to d - 1
9. res = res + [(x0 + i*(n//d)) % n]
10. else:
11. print("no solutions...")
12. return res

```

---


`@bintou`
`2016-01-31 23:49:20`
`字数 8332`
`阅读 2051`


中国的传统与将来
========

`杂文` `传统`

我代表出席会议的中国人说一句话：华盛顿大学主动积极地负责召集筹备这个中美学术会议，我们都要表示很热烈的感谢。最早有关这个会议的想法的人是泰勒先生（George Taylor），然而没有华盛顿大学的奥德伽校长（President Odegaard）、台湾大学的钱思亮热心赞助，会议是开不成的。这个国际学术合作的大胆尝试的几个发起人，几个合力支持的人，都抱着很高的期待，我们盼望这五天会议的收获不至于辜负他们的期待。

我被指定在会议开幕仪式里担任一篇演讲，是我很大的荣幸，我非常感动。但我必须说，指定给我的题目，“中国传统与将来”，是一个很难的题目，中国传统是什么，这个传统的将来又怎样？这两个问题，随便一个对我们的思想都是绝大的考验。可是现在要我在一篇简短的开幕仪式演讲里回答这个问题！我知道我一定失败的，我只盼望我的失败可以刺激会议里最能思想的诸位先生，让他们更进一步，更深刻地想想这个大题目。

### 一 中国传统

我今天提议，**不要把中国传统当作一个一成不变的东西看，要把这个传统当成一长串重大的历史变动进化的最高结果看**。这个历史的看法也许可以证明是一种很有用的办法，可以使人更能了解中国传统，——了解这个传统的性质，了解这个传统的种种长处和短处——这一切都要从造成这个传统的现状的那些历史变动来看。

中国的文化传统，在我的看法，是历史进化的几个大阶段的最后产物：

#### （一）上古的“中国教时代”.

很丰富的考古资料证明，在商朝已经发展出来一个高度进步的文明，有很发达的石雕骨雕，有精美的铜器手工，有千万件甲骨卜辞上所见的够进步的象形会意文字，有十分浪漫的祭祀祖先的国教，显然包括相当大规模的人殉人祭。后来，到了伟大的周朝，文明的种种方面又都再向前发展。好多个封建诸侯长成了大国，而几个有力量的独立国家并存竞争，自然会使战时与平时用的种种知识技术都提高。政治的方策术略愈来愈要讲求了，有才智的人得到鼓励了。“诗”三百篇渐渐成了通用的课本。诗的时代又渐渐引出来哲学的时代。

#### （二）中国固有哲学思想的“经典时代”.

也就是老子、孔子、墨子和他们的弟子们的时代。这个时代留给后世的伟大遗产有老子的自然的宇宙观，他的无为主义的政治哲学；有孔子的人本主义，他的看重人的尊严，看重人的价值的观念，他的爱知识，看重知识上的诚实的教训，他的“有教无类”的教育哲学；还有大宗教领袖墨子的思想，那就是反对一切战争，鼓吹和平，表扬一个他心目中的“兼爱”的“天志”，想凭表扬这个“天志”来维护并且抬高民间宗教的地位。

中国的古文明在这个思想的“经典时代”的几百年（公元前600至220年）里经过了一个基本的变化，这是无可疑的。中国文化传统的基本特色，多少都是这个“经典时代”几大派哲学塑造琢磨出来的。到了后来的各个时代，每逢中国陷入非理性、迷信、出世思想，——这在中国很长的历史上确有好几次——总是靠孔子的人本主义，靠老子和道家的自然主义，或者靠自然主义、人本主义两样结合起来，努力把这个民族从昏睡里救醒。

#### （三）第三段历史的大进化.

是公元前二二一年军国主义的秦国统一了战国，接着有公元前二零六年第二个帝国，汉帝国的建立，以后就是两千多年里中国人在一个大统一帝国之下的生活、经验，——这两千多年里没有一个邻国的文明可以与中国文明比，这样一个孤立的帝国生活里的很长很特殊的政治经验，完全失去了列国之间那种有生气的对抗竞争，也就是造成中国思想的“经典时代”的那种列国的对抗竞争，——是构成中国传统的特性的又一重要因素。

我们可以举出这两千年的帝国生活的几个特别色彩。（1）中国对于一个大的统一帝国里君主专政的问题始终无法解决。（2）一个有补救作用的特点是汉朝（公元前二OO年至二二O年）在头几十年里有意采用无为的政治哲学，使一个极广大的帝国在政治规模上有了一个尽量放任，尊重自由，容许地方自治的传统，使这样一个大帝国没有庞大的常备军，也没有庞大的警察势力。（3）再一个有补救作用的特点是逐渐发展出来一个挑选文官人才的公开竞争的考试制度，这就是世界上最早的文官考试制度。（4）汉朝定出来一套统一的法律，这套法律在以后各朝代里又经过一次次修改。不过中国的法制有个缺点，就是不曾容许公开辩护，不能养成律师这种职业。（5）帝国生活的又一个特点是长期继续使用已成了死文字的古文作为文官考试用的文字，作为极广大的统一帝国里通行的书写交通媒介。两千多年里，这个文字始终是公认的教育工具，是作诗作文用的高尚工具。

#### （四）第四阶段历史的大进化.

实在等于一场革命，就是中国人大量改信了外来的佛教。中国古代的固有宗教不知道有乐园似的天堂，也不知道有执行最后审判的地狱。佛教的大力量，佛教的一切丰富想家，美丽的仪式，大胆的宇宙论和形而上学，很容易地压倒征服了那个固有宗教。轮回观念，三生宿业是铁律，很快地代替了旧的简单的福善祸淫的观念。佛教送给中国的不是一层天，而是几十层天，不是一层地狱，而是好多层地狱，一层一层的森严恐怖各个不同。世界是不实在的，人生是痛苦而空虚的，性是不清洁的，家庭是净修的障碍，独生齐化是佛教生活不可少的条件，布施是最高美德，爱要推及于一切有情生物，应当吃素，应当严厉禁欲，说话念咒可以有神奇的力量。这一切，还有其他种种由海陆两面从印度传进来的非中国的信仰风尚，都很快地被接受了，都变成了中国人的文化生活的一部分了。

这是一场真正的革命。试举一个例说，儒家的“孝经”告诉人，身体是受自父母，不可毁伤的。古代中国的思想家说过，生是最可宝贵的。然而佛教说，人生是一场梦，生就是苦。这种教条又引出种种绝对违反中国传统的风气。用火烧自己的拇指，烧一根或几根手指，甚至烧整条臂，作对佛教一位神的舍身奉献：成了佛门弟子的一种“功德”！有时候，一个和尚预先宣布他遗身的日子，到了那一天，他自己手拿一把火点着用来烧死自己的一堆柴，不断念着佛号，直念到他自己被烧得整个身体倒下去。中国已经印度化了，在一段奇怪的宗教狂热里着了魔了。

#### （五）再下一段历史的大造化.

可以叫做中国对佛教的一串反抗。反抗的一种形式就是中古道教的开始和推广。本土的种种信仰和制度统一起来，加上一点新的民族愿望的刺激，想模仿那个外来的佛教的每一个特点而把佛教压倒、消灭，这就是道教。道教徒采取了佛教的天和地狱，给它们取了中国式的名字，还造了一些中国的神去作主宰！整部《道藏》是用佛教经典作范本编造的。好些佛教的观念，例如轮回，前生来世的因缘，都被整个儿借过来当作自己的。男女道士的清规是仿造佛教僧尼的戒律定的。总而言之**，道教是一个民族主义的排佛运动**，用的方法只是造出一种仿制品来夺取市场，运动的真正目的只是消灭那个外来的宗教，所以几次政府对佛教的迫害，最著名的是公元四四六年（北魏太平真君七年）和八四年（唐武宗会昌五年）两次，都有道教势力的操纵。

中国的佛教内部也起了佛教的种种反抗。这种种反抗的一个共同特点是要把佛教里的中国人不能接受不能消化的东西丢掉。早在四世纪，中国的佛教徒已渐渐看出佛教的精华只是“渐修”与“顿悟”，这两样合起来就是禅法（dhvana或ch’an 日语读作zen），禅的意思是潜修，但也靠哲学上的觉悟。从公元四OO年到七OO年，中国佛教的各派（如菩提达摩开创的楞伽宗，如天台宗）大半都是禅宗。

禅宗的所谓“南宗”——在八世纪以后禅宗成了南宗的专有名字——更进一步宣告，只要顿悟就够了，渐修都可以不要。说这句话的是神会和尚（公元六七O年至七六二年，据我的研究，是南宗的真正开创人）。整个儿所谓“南宗”的运动全靠一串很成功的说谎造假。他们说的菩提达摩故事是一篇谎，他们的西天二十八祖故事是捏造的，他们的袈裟传法故事是骗人的，他们的“六祖”也大部分完全是假的。但是他们最伟大的编造还是那个禅法起源的故事：如来佛在灵山会说法。他只在会众面前拈了一朵花，没有说一句话。没有人懂得他的意思。只有一个聪明的伽叶尊者懂得了，他只对着佛祖微微一笑。据说这就是禅法的源头，禅法的开始。

最足以表示禅宗运动的历史意义的一句作战口号是：“不著语言，不立文字，直指本心”。篇幅多得数不尽的经卷，算得八世纪的中文翻译保存下来已有五千万字之多（不算几千万字中国人写的注疏讲说），全没有一点用处！这是何等惊人的革命！那些惊人的编谎家、捏造家，真正值得赞颂，因为他们只靠巧妙的大谎竟做到了一个革命，打倒了五千万字的神圣经典。

#### （六）中国传统的再下一段大进化.

可以叫做“**中国的文艺复兴时代**”或“中国的几种文艺复兴时代”。因为不只有一种复兴。

第一个是中国的**文学复兴**，在八、九世纪已经蓬蓬勃勃地开始，一直继续发展到我们当代。唐朝的几个大诗人——八世纪的李太白、杜甫、九世纪的白居易——开创了一个中从诗歌的新时代。韩愈（死在八二四年）做到了复兴古文，使古文成为了以后八百年里散文作品的一个可用而且很有力量的利器。八、九世纪的禅门和尚最先用活的白话记录他们的谈话和讨论。十一世纪的禅宗大师继续使用活的文字。十二世纪的理学家也用这种活文字，他们的谈话都是用语录体记下来的。普通男女唱歌讲故事都只是他们自己懂得的话，也就是他们自己说的话。有了九世纪的木板印刷，又有了十一世纪的活字版印刷，于是民间的、“俗”的故事、小说、戏曲、歌词，都可以印给多数人看了。十六、十七世纪有些民间故事和伟大的小说都成了几百年销行很广的作品。这些小说把白话文写定了。这些小说就是白话的教师，就是推广白话的力量。假如没有这些伟大的故事和小说，现代的文学革命绝不会在短短几年里就得到胜利。

第二是**中国哲学的复兴**，到十一、二世纪已经进入了成熟期，产生了理学的几个派别，几个运动。理学是一个有意使佛教进来以前的中国固有文化复兴起来，代替中古的佛教与道教的运动。这个运动的主要目的只是恢复孔子、孟子的道德哲学和政治哲学，并且重新解释，用来代替那个为己的、反社会的、出世的佛教哲学。有一个禅门和尚提到，儒家的学说太简单太没有趣味，不能吸引国中第一等的人。因此，理学的任务只是使先佛教期的中国的非宗教性的思想变得像佛教像禅法一样有趣味有吸引力。这些中国哲学家居然能够弄出一套非宗教性的、合理的理学思想，居然有了一套宇宙论，一套或几套关于知识的性质和方法的理论，一套道德与政治哲学。

理学也有好几个派别，大半是因为对于知识的性质和方法的观点不同而发生的。经过一段时间，理学的各派也居然能够吸引最能思想的人了，居然使他们不再成群的追随佛门的禅师了。而最能思想的人一旦对佛教不再感兴趣，那个伟大过来的宗教就渐渐衰落到无人理会的地步了，几乎到了死的时候不见一声哀悼。

第三，中国文艺复兴的第三方面可以叫做**学术复兴**，是在一种科学方法——考据方法——刺激之下发生的学术复兴。“无证则不信”，是孔子以后一部很早的名著里的一句话，孔子也曾郑重说，“知之为知之，不知为不知，是知也。”然而淹没了中古中国的宗教狂热与轻信是很有力量的大潮，很容易卷走那些求真求证的告诫。只有最好的讯案的法官还能够保持靠证据思想的方法和习惯，但是有些第一流的经学大师居然也能够有这样的方法和习惯，这是最可庆幸的。要等到有了印刻书的流行，中国学者才容易有比较参考的资料，容易校正古书的文字，容易搜求证据，批判证据。有书籍印刷以来的头二三百年里，金石学的开创，一部根据仔细比较审定的资料写成的大历史著作的出现，都可以看得出有考证或考据的精神和方法。又有一派新的经学起来，也是大胆应用这种精神和方法去审查几部儒家的神圣经典。朱子（一一三O年——一二OO年）就是这一派新经学的一个创始人。

考证或考据的方法到了十七世纪更走上有意的发展。有一位学者肯举出一百六十条证据来论定一个单字的古音，又有一位学者化了几十年功夫找证据来证明儒家一部大经书几乎一半是很晚的伪作。这种方法渐渐证明是有用处的，有收获的，所以到了十八、九世纪竟成了学问上的时髦。整三百年的一个时代（一六OO年 – 一九OO年）往往被称为考据的时代。

### 二 大对照与将来

以上的历史叙述已把中国传统文化带到了历史变动最后阶段的前夕，——这个最后阶段就是中国文明与西方文明对照、冲突的时代。西方与中国和中国文明的第一次接触是十六世纪的事。但是真正对照和冲突的时代到十九世纪才开始。这一个半世纪来，中国传统才真正经过了一次力量的测验。这是中国文化史上一次最重要的力量的测验，生存能力的测验。

在我们谈过的历史纲要里，我们已经看到古代中国的固有文明，因为有了经典时代丰富的滋养和适当的防疫，足可以应付佛教传入引起的文化危机。不过因为本土的宗教过于单纯，中国人在一段时间里被那个高度复杂又有吸引力的佛教压倒了，征服了。差不多整整一千年，中国几乎接受了印度输入的每一样东西，中国的文化生活大体上是“印度化”了。但是中国很快的又觉醒过来，开始反抗佛教。于是佛教受了迫害、抵制，同时又有人认真努力把佛教本土化。有了禅宗的起来，佛教的内部也做到了一种革命，公开抛弃了不止五千万字的全部佛教经典。因此，到了最后，中国已能做到一串文学的、哲学的、学术的复兴，使自己的文化继续存在，有了新生命。尽管中国不能完全脱掉两千年信佛教与印度化的影响，中国总算能解决自己的文化问题，能继续建设一个在世的文化，一个基本上是“中国的”文化。

早在十六世纪的末尾几年和十七世纪的头几十年，有一个新奇的但又是高度进步的文化来敲中华帝国的大门。最初到中国来的那些耶稣会士都是仔细挑选出来的，都是有准备的。他们的使命是把欧洲文明和基督教开始介绍给当时欧洲以外最文明的民族。最初的接触是很友善又很成功的。经过一段时间，那些伟大的教士已不止能把欧洲数学、天文学上最好最新的成就介绍给中国头脑最好的人，而且凭他们圣人似的生活榜样介绍了基督教。

中国和西方的强烈对照和冲突是大约一百五十年前开始的。对着诸位这样有学问的人，这样特别懂得近代历史的人，我用不着重说中国因为无知、自大、自满，遭了怎样可悲的屈辱。我也用不着提中国在民族生活各个方面的改革工作因为不得其法，又总是做得太晚，遭了怎样数不清的失败。我更用不着说中国在晚近，尤其是民国以来，这样认真努力对自己的文明重新估价，又在文化传统的几个更基本的方面，如文字方面、文学方面、思想方面、教育方面，怎样认真努力发动改革。诸位和我都是亲眼看见了这种种努力和变化的，我们中国代表团年长些人都是亲身参与这些活动的。

我今天的任务是请诸位注意“中国传统的将来”这个题目直接或间接有关的几件事。我想我们要推论中国传统的将来，应当先给这个传统在与西方有了一百五十年的对照之后的状况开一份清单。我们应当先大致估量一下的中国传统在与西方有了这样的接触之后，有多少成分确是被破坏或被丢弃了。西方文化又有多少成分确是被中国接受了？最后，中国传统还有多少成分保存下来？中国传统有多少成分可算禁得住对照还能存在？

我在好些年前说过，中国已经确实热心努力打掉自己的文化传统里种种最坏的东西：“短短几十年里，中国已经废除了几千年的酷刑，一千年以上的小脚，五百年的八股……”。我们还要记得，中国是欧洲以外第一个废除君主世袭的民族。中国的帝制存在了不止五千年之久，单单“皇帝也要走开”这一件事对广大国民心理的影响就够大了。

这些以及其他几百件迅速的崩溃或慢慢的消蚀，都只是这个文化冲突激荡时期的自然的牺牲。

这些文化的牺牲都不值得惋惜哀悼。这种革除或崩溃都应当看作中国从孤立的旧文明枷锁之下得到解放一部分现象。几千年来中国的政治思想家没有解决一个大一统帝国里君主专制的问题，然而几十年与西方民主国家的接触就够提出解决的方法了：“赶掉皇帝，废除帝制”。其他许多自动的改革也是一样。八百年的理学不能指出裹小脚是不人道的野蛮行为，然而几个传教士带来了一个新观点就能唤起中国人的道德意识，能够把小脚永远废了。

中国从西方文明自动采取吸收的又有多少成分呢？这个清单是开不完的。中国自动采取的东西，—— 无论是因为从来没有那些东西，或者没有相当的东西，还是因为虽有相当的东西但要差一等 —— 确实总有几千件。中国人采取了奎宁、玉蜀荞（荞?）、花生、烟草、眼镜，还有论千种别的东西，都是因为以前没有这些东西。所以愿意要这些东西。用钟表是很早的事，不要多久滴漏就被淘汰了。这是一个高一等的机械代替一个次一等的东西的最明显的例。从钟表到飞机和无线电，论千件的西方科学工艺文明的产物都可以列在我们的清单上。就智识和艺术的范围而论，这份清单可以从欧几里德起一直开到当代的许多科学家、音乐家、电影明星。这个单子真是开不完的。

然后还有一个问题。——从旧文明里丢掉冲刷掉这一切，又从近代西方文明自动采取了这上千个项目，然后中国传统保留下来的成分又还有多少呢？

不止四分之一世纪前，在一九三三年，我有一回演讲，专论中国与日本文化反应的不同形态，我指出日本的现代化可以叫做“中央统制型”，而中国，因为没有一个统治阶级，所以中国的现代化是文化反应的另一个形态，可以叫做“长期暴露与慢慢渗透造成的文化变动”。我接着说：

*这样，我们实在是让一切观念、信仰、制度很自由地与西方文明慢慢接触，慢慢接受感染，接受影响，于是有时起了一步步渐进的改革，也有时起了相当迅速或激烈的变动。……我们没有那一件东西封闭起来，我们也不武断禁止那一样东西有这样接触和变化。……*

过了几年，我又抱着差不多同样的看法说：

*中国的西方化只是种种观念渐渐传播渗透的结果，往往是先有少数几个人的提倡，渐渐得着些人赞成，最后才有够多的人相信这些观念是很合用或很有效验的，于是引起来一些影响深远的变化。从穿皮鞋到文学革命，从用口红到推翻帝制，一切都是自动的，都是经过广义的《理智判断》的。中国没有一件东西神圣到不容有这样的暴露和接触，也没有一个人，或一个阶级，有力量防止哪一种制度受外来文化感染侵蚀的影响。*

我从前说过的话的要点只是：**我认为那许多慢慢的但是自动的变化，正好构成一个可以算是民主而又可取的文化变动形态，——一个长期暴露，自然吸收的形态**。我的意思也是要说，那种种自动的革除淘汰，那种种数不清的采纳吸收，都不会破坏这个站在受方的文明的性格与价值。正好相反，革除淘汰掉那些要不得的成分，倒有一个大解放的作用；采纳吸收进来新的文化成分，只会使那个老文化格外发辉光大。我绝不担忧站在受方的中国文明因为抛弃了许多东西，又采纳了许多东西，而蚀坏、毁灭。我正是说：   

慢慢地、悄悄地，可以是非常明显地，中国的文艺复兴已经渐渐成了一件事实了。这个再生的结晶品看起来似乎使人觉得是带着西方的色彩。但是试把表面剥掉，你就可以看出**做成这个结晶品的材料在本质上正是那个饱经风雨侵蚀而更可以看得明白透彻的中国根底，——正是那个因为接触新世界的科学民主文明而复活起来的人本主义与理智主义的中国**。

这是我在一九三三年说的话。我在当时可是过分乐观了吗？随后这十年来的事变可曾把我的话推翻了吗？

然而将来又怎样呢？“中国根底”，“人本主义与理智主义的中国”，现在成了什么样子呢？在整个中国大陆经过十一年的共产统治之后，这个中国根底又将要变得怎样呢？铁幕统治绝不容许接触自由世界的毒素影响，绝不容许受这种影响的感染，当然更绝不容许“长期暴露”，试问那个“人本主义与理智主义的中国”，长期受了这样的统治，是不是还能继续存在呢？

预料将来总是一件冒险的事。但是，我近几年来看了不止四百万字的“清算”文献。每一篇清算文献都告诉我们，中国共产党和他们的政府所怕的是什么，他们费尽了心机想要连根消灭的是什么？看了这种大量的清算文献，我深信我有根据可以说：今日控制大陆的那些人还是怕自由精神，怕独立思想的精神，怕怀疑的精神或方法，怕考据的功夫。作家胡风被判了罪，因为他和追随他的人表示了自由精神，表示了独立思考，而且竟敢反抗党对文学艺术的控制。梁漱溟，我的朋友，也是老同学，逃不掉整肃，只因为他表示了可怕的怀疑精神。“胡适的幽灵”也值得用三百万字讨伐，因为胡适对传统经学大师的考据精神和方法的传布负的责任最大，更因为胡适有不可饶恕的胆量说那种精神和方法就是科学方法的精华。

看了这许多整肃文献，我才敢相信我所推崇的那个“人本主义与理智主义的中国”在中国大陆还存在着，才相信那个曾尽大力量反抗中古中国那些大宗教，而且把那些宗教终于推倒的大胆怀疑、独立思考、独立表示异议的精神，即使在最不可忍的极权控制压迫之下，也会永久存在，继续传布。总而言之，我深信那个“人本主义与理智主义的中国”的传统没有毁灭，而且无论如何没有人能毁灭。

胡适 --于1960年7月10日，中美学术合作会议-西雅图   

注：原稿胡适用英文写成，本篇由徐高阮先生翻译。



---


`@bintou`
`2019-08-05 18:34:58`
`字数 3743`
`阅读 1817`


反思计算机科学中的理论与工程
==============

`反思` `理论` `工程` `计算机`

---

> “理论联系实践简单来说就是理论不够实践来凑吗？” --by 唐三藏

### 提出问题

计算机学科发展至今，是时候做一些反思了！尽管有人还在怀疑，但是我已经不想再讨论“计算机科学是否科学”这样的问题，而想就计算机科学中的理论与工程进行若干思考。在过去的若干年，在各个不同的层面与场合，有识之士一直在强调“理论联系实践”。看得出，说这话的人很多，但真正能理解其中真实意味的太少。

什么是理论，什么是工程？避免陷入繁杂的考证，思考人类造房子的衍化的过程。不妨猜测，一个造房子的原始人是希望模拟出一个优雅的山洞，即对物理世界中客体的模拟。然后，在建造过程中发现了若干问题，比如：如何防止塌方、方便排水通风等，并不断总结经验得到某些原则，再进行不断改进。这些原则是否就是理论呢？也许是，也许不是。然而有点可以肯定，当“某个人造一所房子”发展为“某个地区的人造某种类型的房子”的时候，当这种原则可以适用于不同的地区与人民，可以流传并衍化，那么这种原则就接近于理论了，或者就成为了理论。要注意的是，理论并非僵化之物，它在变动。当人类可以造出摩天大楼的时候，当我们骄傲地声称人类掌握了建筑的理论的时候，建筑理论不会因为之前“原始人造房子”的理论肤浅而抹杀了其存在的价值，更不应该认为理论源自理论反作用于理论而脱离实践（工程）。

但是，**理论必然需要脱离实践**。所谓*脱离*，我指的是，理论必须是对实践的抽象，是对某些原则的推广。也就是说，抽象是理论与工程之间的区分标准。注意，如上所述，理论到工程并非一蹴而就，可能会经历多个时代的抽象与演进。并且，理论的演进的基础往往又是无数次对理论进行应用的工程实践。因此我们必须小心，当讨论某种理论的时候，我们必须留意自己所处的特定**抽象高度**、理论对工程的**指导意义**及工程实践对理论建立的**挑战**。否则，我们往往将陷入一种无的放矢。

### 实例说明理论与实践的关系

比如，很多小同学在忙着自己的*理论*，而老同学们看了就会嘲笑，“嘿，这也算理论”。更严肃地，很多专家会说，**在数学家眼里，计算机科学这些理论都不是理论**！请不要轻易地下如此结论，任何给出结论的人必须论证他的结论。我们可以承认计算机科学理论的幼稚，但是评判某种“理论”是否是理论只应该应用一种评判标准：这种理论是否对实践的高度抽象，是否可作用于一类问题（而不是一个问题），是否具有发展扩充的可能。以下我们举例说明刚才这些“*理论*”。

就程序设计而言，我们往往认为编程只是一项工程实践活动，是否真的如此呢？以下试图就此探讨，比如，我们要写一个`Fibonacci`数列的程序。无论是用C语言或者Lisp，最直观的方法就是写一个递归函数。如下程序（请大家用直觉来阅读这一段代码）：

 `def fib_recursive(n):   

if n == 0:   

return 0   

elif n == 1:   

return 1   

else:   

return fib_recursive(n-1) + fib_recursive(n-2)`   

没有人会怀疑这是一项实践活动，然而这里存在这样的分歧。如果这是大学一年级的小同学写的程序，大家会觉得没问题；但是有可能一个大三的同学就会说（实际上，很多大一的同学也已经知道）：噢，这个程序真是太不高效了，不用递归而用迭代法可以获得更好的效率。于是，高手大神们就写了如下程序：

 `def fib_iterative(n):   

a, b = 0, 1   

while n > 0:   

a, b = b, a + b   

n -= 1   

return a`   

进一步，如果有好奇的大一同学要问，为什么迭代会高效？高效了多少？我们可以给出很工程的回答：你看，在求第10个Fibonacci数的时候，前一个程序用了10s而后一个程序只用了1s，很显然会快啊！为什么会这样？噢，你看递归程序重复计算了很多的中间值，对吧，只要你花一点点小脑的分析就可以知道了......然后小菜鸟就会惊呼，哇，师兄威武厉害大神！我们必须问，从一个工程的问题出发找到一个工程问题的解决方案，这里有从工程到理论吗？No！这里只是靠直觉，离理论尚远。

在学习了《算法导论 》一书之后，我们掌握了一些算法效率的表示方法，也许可以用`Theta(2^n)`或者`Theta(n)`来分别标注两个程序的效率，然后我们回答说，迭代算法的复杂性是`Theta(n)`，是线性时间，很快。请注意，当走到这一步的时候，`BigO`、`Theta`等的概念并不是针对`Fibonacci`数列的，而是针对广泛的算法而言；我们也不仅仅是关注某种机器下运行多少秒，而是关注一种抽象的概念：线性时间或者指数时间等。于是，我们说，在工程实践中我们主动地应用了某种理论。

这种理论（复杂性理论）当然源自于长期对算法的分析与实践，作用于算法的分析与实践，又脱离了算法的分析与实践独立形成自己的知识体系。这使得在工程实践中，许多人根本没办法把理论与实践清晰地区分开来。谨慎地，我们还是要把握评判的准则：抽象。

再回到`Fibonacci`这个例子，如果有一个偏执的师弟坚持要问：是不是递归一定会比迭代要慢？请看，问题从`Fibonacci`出发但又脱离了原问题走向更宽泛的实例去。我相信，对于这个问题，不见得有多少人能准确地回答，这是一个非常好的问题。

为了更清晰，我们思考一下`GCD算法`（求两个整数的最大公因子）。我们可以递归也可以迭代，问题就变成：迭代是不是一定比递归要强？相信大部分的同学一定会说，无论如何，递归一定要消耗时间，尽管你递归的程序也是`lg n`次递归，但是必然要比迭代的`lg n`要慢。对此我暂且不反驳，我进一步问，**是不是所有的递归程序都可以转换为迭代程序**？如果有，难道就没有一个聪明的编译器可以把递归程序直接编译成迭代的程序吗？如果有这样的编译器，我可以非常直观地写递归程序，让编译器来处理效率的问题。

相信，走到这一步，大部分的同学对我都会有意见了：哪来这么智能的编译器啊？！ 你自己直接写迭代程序不就好了？！鬼知道你这是什么鬼问题?！其实我是在问一个“理论”问题而不是问一个工程的问题，因为似乎这与工程无关了，不是吗？这个问题试图从具体的实例中脱离开来，成为一类问题。想象不出会有哪个工程师需要解决递归到迭代转换的问题。这就是理论开始的地方，但这离理论还有很长的距离！

联想到原始人在建造房子的事情，多年来他们肯定在造房子、住房子的循环中不断地发现问题提出问题解决问题，直至形成建筑科学，这是一个漫长的过程。关于程序设计的理论也是如此，只有一系列“鬼问题”被提出、被解决并形成通用的方法的时候，当递归的问题形成“递归论”的时候，当程序设计的组合技术成为“进程代数”的时候，程序设计才形成理论。当某种（或多种）理论成为某学科的中心与基础的时候，这门学科就成为了科学。 所以，要判断“计算机科学是否科学”就只需要考察一下计算机这门学科形成了多少种理论。

### 理论与实践之间的认知误区

要解答上述一系列问题只靠小脑肯定不行，要足够大的大脑经过长时间折腾才行，这并非本文的目的，在此我更多的是想反思，在我们计算机的教学中形成了什么样的误区。大部分同学奉命学C、C++和Java等，用一种语言为工具依葫芦画瓢写了很多（少）很多（少）的程序。努力编程的成了Coder，他们学习更多的热门的编程语言和技巧，直到这些工具能成为他养家糊口的主要手段。醒目的Coder们会很快就觉醒了，他们认为程序设计没有理论只有工程，直到多年以后，当面向大型程序束手无策的时候，依然没有认识到本应该在本科的时候得到更多理论与抽象的训练。不努力编程的同学诅咒大学只教了理论而不知什么是理论，认为大学只是浪费时间的地方而不知道是自己在浪费时间。后者是一种普遍的存在，但不是本文主要讨论的内容。状况很可悲，值得反思。   

现在的大学非常强调实践，强调工程。为什么在大学里面就没有多少人敢于真诚地承认：课程需要理论呢？我们需要脱离（高于）实践的理论！如何评判一门课程有没有理论？抽象！在《程序设计》中我们有没有教抽象；在《算法设计》中我们有没有教抽象；在《操作系统》中我们有没有教抽象。在《计算机安全学》中我试图教但永远没人听的也是抽象。我认为，当我一直在灌输“[安全的要务首先是定义](http://blog.163.com/wlb_cis/blog/static/23441105620143143374812/)”时，很多同学坐在课堂上想要冲上讲台揍我的感觉，因为我看到一片冷漠的眼神。

走在另一个反面，还有一部分先知先觉的同学，他们接触到了计算机理论的范畴，经过了多年的学习，他们成了计算机理论的最反动者！因为他们发现计算机理论真是太丑陋了，同时他们发现了数学之美，于是他们对计算机理论避之唯恐不及，他们论断：计算机科学不是科学，计算机理论不是真正的理论是工程的一部分而已！就算计算机科学是科学，它也仅仅是数学的一部分。诸如此类的论调颇为流行。持这种观点的往往是专家教授，所以流毒特别深。

果真如此“计算机科学不是科学”么？再次强调，理论、工程不可简单地在一个层面一个维度进行考察。必须坚持一种批判标准：抽象。理论不会因为它丑陋就会变成工程，工程不会因为漂亮就直接成为理论。简单地否定或者承认某种“理论”是或者不是理论毫无意义，反而会轻易地忽略了其中许多重要的内涵。 理性地运用自己的知识与能力去探索答案将更有价值。

---

2015年2月20日下午   

2017年7月5日晚修订   

2019年8月5日晨修改、添加小标题



---


`@bintou`
`2016-07-17 17:52:25`
`字数 79846`
`阅读 2577`


《庄子》
====

`古典` `哲學`

---

逍遥游
---

北冥有鱼，其名为鲲。鲲之大，不知其几千里也。化而为鸟，其名为鹏，鹏之背，不知其几千里也；怒而飞，其翼若垂天之云。是鸟也，海运则将徙于南冥。南冥者，天池也。

齐谐者，志怪者也。谐之言曰：“鹏之徙于南冥也，水击三千里，抟扶摇而上者九万里。去以六月息者也。”野马也，尘埃也，生物之以息相吹也。天之苍苍，其正色邪？其远而无所至极邪？其视下也，亦若是则已矣。

且夫水之积也不厚，则其负大舟也无力。覆杯水于坳堂之上，则芥为之舟，置杯焉则胶，水浅而舟大也。风之积也不厚，则其负大翼也无力。故九万里，则风斯在下矣，而后乃今培风。背负青天而莫之夭厄者，而后乃今将图南。

蜩与学鸠笑之曰：“我决起而飞，枪榆枋，时则不至，而控于地而已矣。奚以之九万里而南为？”适莽苍者，三飧而反，腹犹果然。适百里者，宿舂粮。适千里者，三月聚粮。之二虫，又何知？小知不及大知，小年不及大年。奚以知其然也？朝菌不知晦朔，惠蛄不知春秋，此小年也。楚之南有冥灵者，以五百岁为春，五百岁为秋；上古有大椿者，以八千岁为春，八千岁为秋；而彭祖乃今以久特闻，众人匹之，不亦悲乎？

汤之问棘也是已。湯問棘曰：“上下四方有極乎？” 棘曰：“無極之外，復無極也。 穷发之北有冥海者，天池也。有鱼焉，其广数千里，未有知其修者，其名为鲲。有鸟焉，其名为鹏，背若泰山，翼若垂天之云，抟扶摇羊角而上者九万里，绝云气，负青天，然后图南，且适南冥也。斥鹌笑之曰：‘彼且奚适也？我腾跃而上，不过数仞而下，翱翔蓬蒿之间，耻亦飞之至也。而彼且奚适也？’” 此小大之辨也。

故夫知效一官，行比一乡，德合一君而征一国者，其自视也亦若此矣。而宋荣子犹然笑之。且举世誉之而不加劝，举世非之而不加沮。定乎内外之分，辨乎荣辱之境，斯已矣。彼其于世未数数然也，虽然，犹有未树也。夫列子御风而行，泠然善也，旬有五日而后反。彼于致福者，未数数然也。此虽免乎行，犹有所待者也。若夫乘天地之正，而御六气之辩，以游无穷者，彼且恶乎待哉！故曰：至人无己，神人无功，圣人无名。

尧让天下于许由，曰：“日月出矣，而爝火不息，其于光也，不亦难乎？时雨降矣，而犹浸灌，其于泽也，不亦劳乎？夫子立而天下治，而我犹尸之，吾自视缺然。请致天下。”许由曰：“子治天下，天下既已治也，而我犹代子，吾将为名乎？名者，实之宾也，吾将为宾乎？鹪鹩巢于深林，不过一枝；偃鼠饮河，不过满腹。归休乎君，予无所用天下为。庖人虽不治庖，尸祝不越樽俎而代之矣。”

肩吾问于连叔曰：“吾闻言于接舆，大而无当，往而不返。吾惊怖其言，犹河汉而无极也。大有径庭，不近人情焉。”连叔曰：“其言谓何哉？”曰：“藐姑射之山，有神人居焉，肌肤若冰雪，淖约若处子，不食五谷，吸风饮露，乘云气，御飞龙，而游乎四海之外。其神凝，使物不疵厉而年谷熟。吾是以狂而不信也。”连叔曰：“然。瞽者无以与乎文章之观，聋者无以与乎钟鼓之声。岂惟形骸有聋盲哉，夫知亦有之。是其言也，犹时汝也。之人也，之德也，将磅礴万物以为一。世蕲乎乱，孰弊弊焉以天下为事？之人也，物莫之伤，大浸稽天而不溺，大旱金石流土山焦而不热。是其尘垢秕糠，将犹陶铸尧舜者也。孰肯以物为事？宋人资章甫适诸越，越人断发文身，无所用之。尧平治天下之民，平海内之政，往见四子藐姑射之山，汾水之阳，杳然丧其天下焉。”

惠子谓庄子曰：“魏王贻我大瓠之种，我树之成而实五石。以盛水浆，其坚不能自举也。剖之以为瓢，则瓠落无所容。非不枵然大也，吾为其无用而掊之。”庄子曰：“夫子固拙于用大矣。宋人有善为不龟手之药者，世世以并辟光为事。客闻之，请买其方百金。聚族而谋曰：我世世为并辟光，不过数金，今一朝而鬻技百金，请与之。客得之以说吴王。越有难，吴王使之将，冬与越人水战，大败越人，裂地而封之。能不龟手一也，或以封，或不免与并辟光，则所用之异也。今子有五石之瓠，何不虑以为大樽，而浮于江湖。而忧其瓠落无所容，则夫子犹有蓬之心也夫？”

惠子曰：“吾有大树，人谓之樗。其大本臃肿而不中绳墨，其小枝卷曲而不中规矩。立之途，匠者不顾。今子之言，大而无用，众所同去也。”庄子曰：“子独不见狸生乎？卑身而伏，以候敖者，东西跳梁，不辟高下，中于机辟，死于网罟。今夫嫠牛，其大若垂天之云，此能为大矣，而不能执鼠。今子有大树，患其无用，何不树之于无何有之乡，广莫之野，彷徨乎无为其侧，逍遥乎寝卧其下。不夭斤斧，物无害者。无所可用，安所困苦哉！”

齐物论
---

南郭子綦隐机而坐，仰天而嘘，答焉似丧其耦。颜成子游立侍乎前，曰：“何居乎？形固可使如槁木，而心固可使如死灰乎？今之隐机者，非昔之隐机者也。”子綦曰：“偃，不亦善乎？而问之也。今者吾丧我，汝知之乎？汝闻人籁而未闻地籁，汝闻地籁而未闻天籁夫。”子游曰：“敢问其方？”子綦曰：“夫大块噫气，其名为风。是唯无作，作则万窍怒呺。而独不闻之翏翏乎？山林之畏佳，大木百围之窍穴，似鼻，似口，似耳，似枅，似圈，似臼，似洼者，似污者，激者，稿者，叱者，吸者，叫者，嚎者，窈者，咬者。前者唱于而随者唱喁。泠风則小和，飘风则大和，厉风济则众窍为虚。而独不见之调调之刁刁乎？”子游曰：“地籁则众窍是已，人籁则比竹是已。敢问天籁？”子綦曰：“夫吹万不同，而使其自己也，咸其自取，怒者其谁邪！”

大知闲闲，小知间间，大言炎炎，小言詹詹。其寐也魂交，其觉也形开，与接为构，日以心斗。缦者，窖者，密者。小恐惴惴，大恐缦缦。其发若机括，其司是非之谓也。其留如诅盟，其守胜之谓也。其杀若秋冬，以言其日消也。其溺之所为之，不可使复之也。其厌也如缄，以言其老洫也。近死之心，莫使复阳也。喜怒哀乐，虑叹变絷，姚佚启态。乐出虚，蒸成菌，日夜相代乎前而莫知其所萌。已乎已乎，旦暮得此其所由以生乎？

非彼无我，非我无所取。是亦近矣，而不知其所为使。必有真宰，而特不得其朕。可形已信，而不见其形，有情而无形。百骸、九窍、六藏，赅而存焉，吾谁与为亲？汝皆悦之乎？其有私焉？如是皆有为臣妾乎？其臣妾不足以相治也。其递相为君臣乎？其有真君存焉。如求得其情与不得，无益损乎其真。一受其成形，不亡以待尽，与物相刃相靡，其行尽如驰，而莫之能止，不亦悲乎！终身役役，而不见其成功，祢然疲役，而不知其所归，可不哀邪！人谓之不死，奚益？其形化，其心与之然，可不谓大哀乎？人之生也，固若是芒乎？其我独芒，而人亦有不芒者乎？

夫随其成心而师之，谁独且无师乎？奚必知代，而心自取者有之？愚者与有焉。未成乎心而有是非，是今日适越而昔至也，是以无有为有。无有为有，虽有神禹且不能知，吾独且奈何哉？

夫言非吹也，言者有言。其所言者特未定也，果有言邪？其未尝有言邪？其以为异于彀音，亦有辨乎，其无辨乎？道恶乎隐而有真伪？言恶乎隐而有是非？道恶乎往而不存？言恶乎存而不可？道隐于小成，言隐于荣华。故有儒墨之是非，以是其所非，而非其所是。欲是其所非而非其所是，则莫若以明。

物无非彼，物无非是。自彼则不见，自知则知之。故曰：彼出于是，是亦因彼。彼是方生之说也。虽然，方生方死，方死方生，方可方不可，方不可方可。因是因非，因非因是。是以圣人不由，而照之于天。彼亦一是非，此亦一是非。果且有彼是乎哉，果且无彼是乎哉？彼是莫得其偶，谓之道枢。枢始得其环中，以应无穷。是亦一无穷，非亦一无穷。故曰：莫若以明。

以指喻指之非指，不若以非指喻指之非指也。以马喻马之非马，不若以非马喻马之非马也。天地一指也，万物一马也。可乎可，不可乎不可。道行之而成，物谓之而然。恶乎然？然于然。恶乎不然？不然于不然。物固有所然，物固有所可。无物不然，无物不可。故为是举莛与楹，厉与西施，恢诡谲怪，道通为一。其分也，成也。其成也，毁也。凡物无成与毁，复通为一。唯达者知通为一。为是不用，而寓诸庸。庸也者，用也。用也者，通也。通也者，得也。适得而几已。因是已，已而不知其然，谓之道。

劳神明为一，而不知其同也，谓之朝三。何谓朝三？狙公赋芋，曰：“朝三而暮四。”众狙皆怒。曰：“朝四而暮三。”众狙皆悦。名实未亏而喜怒为用，亦因是也。是以圣人和之以是非，而休乎天钧。是之谓两行。

古之人，其知有所至矣。恶乎至？有以为未始有物者，至矣尽矣，不可以加矣。其次以为有物矣，而未始有封也。其次以为有封也焉，而未始有是非也。是非之彰也，道之所以亏也。道之所以亏，爱之所以成。果且有成与亏乎哉？果且无成与亏乎哉？有成与亏，故昭氏之鼓琴也，无成与亏，故昭氏之不鼓琴也。昭文之鼓琴也，师旷之枝策也，惠子之据梧也。三子之知几乎，皆其盛者也，故载之末年。唯其好之，以异于彼，其好之也，欲以明之彼。非所明而明之，故以坚白之昧终。而其子又以文之纶终，终身无成。若是而可谓成乎，虽我亦成也。若是而不可谓成乎，物与我无成也。是故滑疑之耀，圣人之所图也。为是不用而寓诸庸，此之谓以明。

今且有言于此，不知其与是类乎，其与是不类乎？类与不类，相与为类，则与彼无以异矣。虽然，请尝试言之。有始也者，有未始有始也者，有未始夫未始有始也者。有有也者，有无也者，有未始有无也者，有未始夫未始有无也者。俄而有无矣，而未知有无之果孰有孰无也。今我则已有谓矣，而未知吾所谓之果有谓乎，其果无谓乎？天下莫大于秋毫之末，而太山为小，莫寿于殇子，而彭祖为夭。天地与我并生，而万物与我为一。既已为一矣，且得有言乎？既已谓之一矣，且得无言乎？一与言为二，二与一为三。自此以往，巧历不能得，而况其凡乎？故自无适有以至于三，而况自有适有乎？无适焉，因是已。

夫道未始有封，言未始有常。为是而有畛也，请言其畛。有左有右，有伦有义，有分有辩，有竞有争，此之谓八德。六合之外，圣人存而不论；六合之内，圣人论而不议；春秋经世先王之志，圣人议而不辩。故分也者，有不分也；辩也者，有不辩也。曰何也？圣人怀之，众人辩之以相示也。故曰：辩也者，有不见也。夫大道不称，大辩不言，大仁不仁，大廉不慊，大勇不歧。道昭而不道，言辩而不及，仁常而不成，廉清而不信，勇歧而不成。五者园而几向方矣。故知止其所不知，至矣。孰知不言之辩，不道之道。若有能知，此之谓天府。注焉而不满，酌焉而不竭，而不知其所由来。此之谓葆光。

故昔者尧问于舜曰：“我欲伐宗、脍、胥敖，南面而不释然。其故何也？”舜曰：“夫三子者，犹存乎蓬艾之间，若不释然，何哉？昔者十日并出，万物皆照，而况德之进乎日者乎？”

啮缺问乎王倪曰：“子知物之所同是乎？”曰：“吾恶乎知之？”“子知子之所不知邪？”曰：“吾恶乎知之？”“然则物无知邪？”曰：“吾恶乎知之？虽然，尝试言之。庸讵知吾所谓知之非不知邪？庸讵知吾所谓不知之非知邪？且吾尝试问乎汝。民湿寝则腰疾而偏死，鳅然乎哉？木处则惴栗恂惧，猿猴然乎哉？三者孰知正处？民食刍豢，麋鹿食荐，鲫蛆甘带，鸱鸦嗜鼠，四者孰知正味？猿，蝙狙以为雌，麋与鹿交，鳅与鱼游，毛嫱丽姬，人之所美也，鱼见之深入，鸟见之高飞，麋鹿见之决骤。四者孰知天下之正色哉？自我观之，仁义之端，是非之途，樊然淆乱。吾恶能知其辩？”啮缺曰：“子不知利害，则至人固不知利害乎？”王倪曰：“至人神矣。大泽焚而不能热，河汉冱而不能寒，疾雷破山，风振海，而不能惊。若然者，乘云气，骑日月，而游乎四海之外，死生无变于己，而况利害之端乎？”

瞿鹊子问于长梧子曰：“吾闻诸夫子，圣人不从事于务，不就利，不违害，不喜求，不缘道，无谓有谓，有谓无谓，而游乎尘垢之外。夫子以为孟浪之言，而我以为妙道之行也。吾子以为奚若？”长梧子曰：“是黄帝之所听荧也，而求也何足以知之。且汝亦大早计，见卵而求时夜，见弹而求枭炙。予尝为汝妄言之，汝亦以妄听之。奚旁日月，挟宇宙，为其吻合，置其滑昏，以隶相尊。众人役役，圣人愚钝。参万岁而一成纯，万物尽然而以是相蕴。予恶乎知说生之非惑邪？予恶乎知恶死之非弱丧而不知归者邪？丽之姬，艾封人之子也。晋国之始得之，涕泣沾襟，及其至于王所，与王同筐床，食刍豢，而后悔其泣也。予恶乎知夫死者不悔其始之蕲生乎？梦饮酒者，旦而哭泣，梦哭泣者，旦而田猎。方其梦也，不知其梦也。梦之中又占其梦焉，觉而后知其梦也，且有大觉而后知此其大梦也。而愚者自以为觉，窃窃然知之。君乎牧乎？固哉！丘也与汝皆梦也，予谓汝梦亦梦也。是其言也，其名为吊诡。万世之后，而一遇大圣，知其解者，是旦暮遇之也。既使我与若辩矣，若胜我，我不若胜，若果是也，我果非也邪？其俱是也，其俱非也邪？我与若不能相知也。则人固受其黯暗，吾谁使正之？使同乎若者正之，既与若同矣，恶能正之？使同乎我者正之，既同乎我矣，恶能正之？使异乎我与若者正之，既异乎我与若矣，恶能正之？使同乎我与若者正之，既同乎我与若矣，恶能正之？然则我与若与人，俱不能相知也，而待彼也邪。化声之相待，若其不相待。和之以天倪，因之以曼衍，所以穷年也。”“何谓和之以天倪？”曰：“是不是，然不然。是若果是也，则是之异乎不是也亦无辩，然若果然也，则然之异乎不然也亦无辩。忘年忘义，振于无竟。”

罔两问景曰：“曩子行，今子止，曩子坐，今子起。何其无特操与？”景曰：“吾有待而然者邪？吾所待又有待而然者邪？吾待蛇蝮蜩翼邪？恶识所以然？恶识所以不然？”

昔者庄周梦为蝴蝶，栩栩然蝴蝶也，自喻适志与，不知周也。俄然觉，则遽遽然周也。不知周之梦为蝴蝶与？蝴蝶之梦为周与？周与蝴蝶，则必有分矣。此之谓物化。

养生主
---

吾生也有涯，而知也无涯，以有涯随无涯，殆已！已而为知者，殆而已矣！为善无近名，为恶无近刑。缘督以为经，可以保身，可以全生，可以养亲，可以尽年。

庖丁为文惠君解牛，手之所触，肩之所倚，足之所履，膝之所倚，砉然响然，奏刀嚯然。莫不中音，合于桑林之舞，乃中经首之会。文惠君曰：“嘻，善哉！技盍至乎此乎？”庖丁释刀对曰：“臣之所好者，道也，进乎技矣。始臣之解牛之时，所见无非牛者。三年之后，未尝见全牛也。方今之时，臣以神遇，而不以目视。官知止而神欲行，依乎天理，批大隙，导大款，因其固然。技经肯綮之未尝，而况大觚乎？良庖岁更刀，割也。族庖月更刀，折也。今臣之刀，十九年矣，所解数千牛矣，而刀刃若新发于硎。彼节者有间，而刀刃者无厚，以无厚入有间，恢恢乎其于游刃必有余地矣。是以十九年而刀刃若新发于硎。虽然，每至于族，吾见其难为，怵然为戒，视为止，行为迟，动刀甚微，诘然已解，如土委地，提刀而立，为之四顾，为之踌躇满志，善刀而藏之。”文惠君曰：“善哉！吾闻庖丁之言，得养生焉。”

公文轩见右师而惊曰：“是何人也？恶乎介也？天与？其人与？”曰：“天也，非人也。天之生是使独也，人之貌有与焉。以是知其天也，非人也。”

泽雉十步一啄，百步一饮，不蕲畜乎樊中。神虽王，不善也。

老聃死，秦失吊之，三号而出，弟子曰：“非夫子之友邪？”曰：“然。”“然则吊焉若此，可乎？”曰：“然。始也吾以为其人也，而今非也。向吾入而吊焉，有老者哭之，如哭其子，少者哭之，如哭其母。彼其所以会之，必有不蕲言而言，不蕲哭而哭者，是遁天倍情，忘其所受，古者谓之遁天之刑。适来，夫子时也；适去，夫子顺也。安时而处顺，哀乐不能入也。古者谓是帝之悬解。

指穷于为薪，火传也，不知其尽也。

人间世
---

颜回见仲尼，请行。曰：“奚之？”曰：“将之卫。”曰：“奚为焉？”曰：“会闻卫君，其年壮，其行独，轻用其国，而不见其过，轻用民死，死者以国量乎。泽若蕉，民其无如矣。回尝闻之夫子曰：治国去之，乱国就之，医门多疾。愿以所闻思其则，庶几其国有瘳乎！”仲尼曰：“嘻，若殆往而刑耳。夫道不欲杂，杂则多，多则扰，扰则忧，忧而不救。古之至人，先存诸己，而后存诸人。所存于己者未定，何暇至于暴人之所行！且若亦知夫德之所荡，而知之所为出乎哉？德荡乎名，知出乎争。名也者，相轧也；知也者，争之器也。二者凶器，非所以尽行也。且德厚信杠，未达人气；名闻不争，未达人心。而强以仁义绳墨之言，术暴人之前者，是以人恶有其美也，命之曰灾人。灾人者，人必反灾之。若殆为人灾夫。且苟为悦贤而恶不肖，恶用而求有以异？若唯无诏，王公必将乘人而斗其捷，而目将荧之，而色将平之，口将营之，容将形之，心且成之，是以火救火，以水救水，名之曰益多。顺始无穷，若殆以不信厚言，必死于暴人之前矣。且昔者桀杀关逢龙，纣杀王子比干，是皆修其身，以下伛拊人之民，以下拂其上者也。故其君因其修以挤之，是好名者也。昔者尧攻丛枝胥敖，禹攻有扈，国为虚厉，身为刑戮，其用兵不止，其求实无已，是皆求名实者也。而独不闻之乎，名实者，圣人之所不能胜也，而况若乎？虽然，若必有以也，尝以语我来。”颜回曰：“端而虚，勉而一，则可乎？”曰：“恶。恶可！夫以阳为充，孔阳，采色不定，常人之所不违，因案人之所感，以求容与其心，名之曰日渐之德不成，而况大德乎？将执而不化，外合而内不訾。其庸讵可乎！”“然则我内直而外曲，成而上比。内直者，与天为徒。与天为徒者，知天子之与己，皆天之所子，而独以己言蕲乎而人善之，蕲乎而人不善之邪。若然者，人谓之童子。是之谓与天为徒。外曲者，与人之为徒也。擎跽曲拳，人臣之礼也，人皆为之，吾敢不为邪？为人之所为者，人亦无疵焉。是之谓与人为徒。成而上比者，与古为徒。其言虽教，谪之实也，古之有也，非吾有也。若然者，虽直而不病。是之谓与古为徒。若是则可乎？”仲尼曰：“恶，恶可！大多政，法而不谍，虽固亦无罪，虽然，止是?ú矣，夫胡可以及化，犹师心者也。”颜回曰：“吾无以进矣，敢问其方？”仲尼曰：“齐，吾将语若。有而为之，其易邪。易之者，杲天不宜。”颜回曰：“毁回之家贫，唯不饮酒，不茹荤者数月矣。如此，则可以为斋乎？”曰：“是祭祀之斋，非心斋也。”回曰：“敢问心斋？”仲尼曰：“一若志，无听之以耳，而听之以心，无听之以心，而听之以气。听止于耳，心止于符，气也者，虚而待物者也。唯道集虚，虚者，心斋也。”颜回曰：“回之未始得使，实自回也。得使之也，未始有回也。可谓虚乎？”夫子曰：“尽矣。吾语若。若能入游其樊，而无感其名，入则鸣，不入则止。无门无毒，一宅而寓于不得已，则几矣。绝迹易，无行地难。为人使易以伪，为天使难以伪。闻以有翼飞者矣，未闻以无翼飞者也。闻以有知知矣，未闻以无知知者也。瞻彼揆者，虚室生白，吉祥止止，夫且不止，是之谓坐驰。夫徇耳目内通，而外于心知，鬼神将来舍，而况人乎！是万物之化也，尧舜之所纽也，伏羲几遽之所行终，而况散焉者乎！”

公子高将使于齐，问于仲尼曰：“王使诸梁也甚重。齐之待使者，盖将甚敬而不急。匹夫犹未可动，而况诸侯乎。吾甚栗之。子常语诸梁也，曰：凡事若小若大，寡不道以欢成。事若不成，则必有人道之患。事若成，则必有阴阳之患。若成若不成，而后无患者，唯有德者能之。吾食也执粗而不臧，馨无欲清之人。今吾朝受命而夕饮冰，我其内热与。吾未至乎事之情，而既有阴阳之患矣。事若不成，必有人道之患。是两也，为人臣者不足以任之，子其有以语我来？”仲尼曰：“天下有大戒二，其一命也，其一义也。子之爱亲，命也，不可解于心。臣之事君，义也，无适而非君也，无所逃于天地之间，是之谓大戒。是以夫事其亲者，不择地而安之，孝之至也。夫事其君者，不择事而安之，忠之盛也。自事其心者，哀乐不易施乎前。知其不可奈何而安之若命，德之至也。为人臣子者，固有所不得已。行事之情而忘其身，何暇至于悦生而恶死。夫子其行可矣。丘请复以所闻。凡交，近则必相靡以信，远则必忠之以言。言必或传之，夫传两喜两怒之言，天下之难者也。夫两喜必多溢美之言，两怒必多溢恶之言。凡溢之类妄，妄则其信之也莫，莫则传言者殃。故法言曰：传其常情，无传其溢言，则几乎全。且以巧斗力者，始乎阳，常卒乎阴，大至则多奇巧。以礼饮酒者，始乎治，常卒乎乱，大至则多奇乐。凡事亦然，始乎谅，常卒乎鄙。其作始也简，其将毕也必巨。夫言者风波也，行者实丧也。风波易以动，实丧易以危。故忿设无由，巧言偏辞。兽死不择音，气息沸然，于是并生心厉。克核大至，则必有不肖之心应之，而不知其然也。苟为不知其然也，孰知其所终？故法言曰：无迁令，无欢成，过度益也。迁令劝成殆事，美成在久，恶成不及改，可不慎与！且夫乘物以游心，托不得已以养中，至矣。何作为报也？莫若为致命，此其难者。”

颜阖将傅卫灵公太子，而问于遽伯玉曰：“有人于此，其德天杀，与之为无方，则危吾国，与之为有方，则危吾身。其知适足以知人之过，而不知其所以过。若然者，吾奈之何？”遽伯玉曰：“善哉问乎！戒之慎之，正汝身也哉。形莫若就，心莫若和。虽然，之二者有患，就不欲入，和不欲出。形就而入，且为颠为灭，为崩为蹶。心和而出，且为声为名，为妖为孽。彼且为婴儿，亦与之为婴儿。彼且为无町畦，亦与之为无町畦。彼且为无崖，亦与之为无崖。达之入于无疵。汝不知夫螳螂乎，怒其臂以当车辙，不知其不胜任也，是其才之美者也。戒之慎之。积伐而美者以犯之，几矣。汝不知夫养虎者乎，不敢以生物与之，为其杀之之怒也。不敢以全物与之，为其决之之怒也。时其饥饱，达其怒心。虎之与人异类，而媚养己者，顺也。故其杀者，逆也。夫爱马者以筐盛矢，以赈盛溺，适有蚤虻仆缘，而拊之不时，则缺衔毁首碎胸。意有所至，而爱有所亡。可不慎邪！”

匠石之齐，至乎曲辕，见栎社树，其大蔽数千牛，挈之百围，其高临山十仞而后有枝，其可以为舟者旁十数。观者如市，匠伯不顾，遂行不辍。弟子厌观之，走及匠石曰：“自吾执斧斤以随夫子，未尝见材如此其美也。先生不肯视，行不辍，何邪？”曰：“已矣，勿言之矣。散木也，以为舟则沉，以为棺椁则速腐，以为器则速毁，以为门户则液螨，以为柱则蠹。是不材之木也，无所可用，故能若是之寿。”匠石归，栎社树见梦曰：“汝将恶乎比予哉？若将比予于文木邪？夫且梨橘柚果瓜之属，实熟则剥，剥则辱，大枝折，小枝泄。此以其能苦其生者也，故不终其天年而中道夭，自掊击于世俗者也。物莫不若是。且予求无所可用久矣，几死，乃今得之，为予大用。使予也而有用，且得有此大也邪？且也若与予也皆物也，奈何哉其相物也！而几死之散人，又恶知散木？”匠石觉而诊其梦，弟子曰：“趣取无用，则为社何邪？”曰：“密！若无言，彼亦直寄焉，以为不知己者诟厉也。不为社者，且几有翦乎！且也彼其所保与众异，以义誉之，不亦远乎？”

南伯子綦游乎商之丘，见大木焉，有异，结驷千乘，隐将芘其所赖。子綦曰：“此何木也哉，此必有异材夫。”仰而视其细枝，则拳曲而不可以为栋梁。俯而见其大根，则轴解而不肯可为棺椁。舌其叶，则口烂而为伤，嗅之，则使人狂酲三日而不已。子綦曰：“此果不材之木也，以至于此其大也。嗟夫，神人以此不材。宋有荆氏者，宜楸柏桑，其拱把而上者，求狙猴之弋者斩之。三围四围，求高名之丽者斩之。七围八围，贵人富商之家求禅傍者斩之。故未终其天年，而中道已夭于斧斤。此材之患也。故解之以牛之白颡者，与豚之亢鼻者，与人之有痔病者，不可以适河。此皆巫祝以知之矣，所以为不祥也，此乃神人之所以为大祥也。

支离疏者，颐隐于脐，肩高于顶，会撮指天，五管在上，两髀为肋，挫针治獬，足以糊口。鼓荚播精，足以食十人。上征武士，则支离攘臂而游于其间。上有大役，则支离以有常疾不受功。上与病者粟，则受三钟与十束薪。夫支离其形者，犹足以养其身，终其天年，由况支离其德者乎！

孔子适楚，楚狂接舆游其门曰：“凤兮凤兮，何如德之衰也！来世不可待，往世不可追也。天下有道，圣人成焉。天下无道，圣人生焉。方今之时，仅免刑焉。福轻乎羽，莫之知载；祸重乎地，莫之知避。已乎已乎，临人以德；殆乎殆乎，画地而趋。迷阳迷阳，无伤吾行，吾行却曲，无伤吾足。

山木自寇也，膏火自煎也。桂可食，故伐之。漆可用，故割之。人皆知有用之用，而莫知无用之用也。

德充符
---

鲁有兀者王骀，从之游者，与仲尼相若。常季问于仲尼曰：“王骀，兀者也，从之游者，与夫子中分鲁。立不教，坐不议，虚而往，实而归。固有不言之教，无形而心成者邪？是何人也？”仲尼曰：“夫子，圣人也。丘也直后而未往耳。丘将以为师，而况不如丘者乎？奚假鲁国，丘将引天下而与从之。”常季曰：“彼兀者也，而王先生，其与庸亦远矣。若然者，其用心也独若之何？”仲尼曰：“死生亦大矣，而不得与之变。虽天地覆坠，亦将不与之遗。审乎无假而不与物迁，命物之化而守其宗也。”常季曰：“何谓也？”仲尼曰：“自其异者视之，肝胆楚越也。自其同者视之，万物皆一也。夫若然者，且不知耳目之所宜，而游心于德之和。物视其所一，而不见其所丧。视丧其足犹遗土也。”常季曰：“彼为己，以其知得其心，以其心得其常心。物何为最之哉？”仲尼曰：“人莫鉴于流水，而鉴于止水。唯止能止众止。受命于地，唯松柏独也在，冬夏青青。受命于天，唯舜独也正，幸能正生，以正众生。夫保始之征，不惧之实，勇士一人，雄入于九军。将求名而能自要者，而犹若此，而况官天地、府万物，直寓六骸，象耳目，一知之所知，而心未尝死者乎！彼且择日而登假，人则从是也。彼且何肯以物为事乎！”

申徒嘉，兀者也，而与郑子产同师于伯昏无人。子产谓申徒嘉曰：“我先出则子止，子先出则我止。”其明日，又与合堂同席而坐。子产谓申徒嘉曰：“我先出则子止，子先出则我止。今我将出，子可以止乎？其未邪？且子见执政而不违，子齐执政乎？”申徒嘉曰：“先生之门，固有执政焉如此哉？子而说子之执政而后人者也？闻之曰：鉴明则尘垢不止，止则不明也。久与贤人处则无过。今子之所取大者，先生也。而犹出言若是，不亦过乎？”子产曰：“子既若是矣，犹与尧争善，计子之德，不足以自反邪？”申徒嘉曰：“自状其过，以不当亡者众；不状其过，以不当存者寡。知不可奈何而安之若命，惟有德者能之。游于羿之彀中，中央者，中地也，然而不中者，命也。人以其全足笑吾不全足者多矣，我怫然而怒，而适先生之所，则废然而反。不知先生之洗我以善邪。吾与夫子游十九年矣，而未尝知吾兀者也。今子与我游于形骸之内，而子索我与形骸之外，不亦过乎？”子产蹴反改容更貌曰：“子无乃称。”

鲁有兀者叔山无趾，踵见仲尼，仲尼曰：“子不谨前，既犯患若是矣，虽今来何及矣！”无趾曰：“吾唯不知务而轻用吾身，吾是以亡足。今吾来也，犹有尊足者存，吾是以务全之也。夫天无不覆，地无不载。吾以夫子为天地，安知夫子之犹若是也？”孔子曰：“丘则陋矣。夫子胡不入乎，请讲以所闻。”无趾出，孔子曰：“弟子勉之，夫无趾，兀者也，犹务学以复补前行之恶，而况全德之人乎？”无趾语老聃曰：“孔丘之于至人，其未邪？彼何宾宾以学子为？彼且蕲以皎诡幻怪之名闻，不知至人之以是为己桎梏邪！”老聃曰：“胡不直使彼以死生为一条，以可不可为一贯者，解其桎梏。其可乎？”无趾曰：“天刑之，安可解？”

鲁哀公问于仲尼曰：“卫有恶人焉，曰哀骀它。丈夫与之处者，思而不能去也。妇人见之，请于父母曰：与为人妻，宁为夫子妾者。十数而未止也，未尝有闻其唱者也，常和而已矣。无君之位以济乎人之死，无聚禄以望人之腹，又以恶骇天下。和而不唱，知不出乎四域，且而雌雄合乎前，是必有异乎人者也。寡人召而观之，果以恶骇天下。与寡人处，不至以月数，而寡人有意乎其为人也。不至乎期年，而寡人信之。国无宰，寡人传国焉，闷然而后应，泛而若辞。寡人丑乎，足卒授之国，无几何也，去寡人而行。寡人恤焉若有亡也，若无与乐是国也。是何人者也？”仲尼曰：“丘也尝使于楚矣，适见豚子食于其死母者，少焉郇若，皆弃之而走。不见己焉尔，不得类焉尔。所爱其母者，非爱其形也，爱使其形者也。战而死者，其人之葬也，不以羿资。刖者之履，无为爱之。皆无其本矣。为天子之诸御，不爪翦，不穿耳，娶妻者，止于外，不得复使。形全犹足以为尔，而况全德之人乎？今哀骀它未言而信，无功而亲，使人授己国，唯恐其不受也。是必才全而德不形者也。”哀公曰：“何谓才全？”仲尼曰：“死生存亡，穷达富贵，贤与不肖，毁誉饥渴寒暑，是事之变，命之行也。日夜相代乎前，而知不能规乎其始者也，故不足以滑和，不可入于灵府。使之和豫通而不失于兑，使日夜无却，而与物为春，是接而生时于心者也，是之谓全才。”“何谓德不形？”曰：“平者水停之盛也，其可以为法也。内保之而外不荡也。德者成和之修也，德不形者，物不能离也。”哀公异日以告闵子曰：“始也吾以南面而君天下，执民之纪而忧其死，吾自以为至通矣。今吾闻至人之言，恐吾无其实，轻用吾身而亡其国。吾与孔丘，非君臣也，德友而已矣。”

茵歧支离无胗，说卫灵公，灵公说之，而视全人，其豆肩肩。臃鞅大瘿说齐桓公，桓公说之，而视全人，其豆肩肩。

故德有所长而形有所忘，人不忘其所忘，而忘其所不忘，此谓诚忘。故圣人有所游，而知为孽，约为胶，德为接，工为商。圣人不谋，恶用知！不断，恶用胶！无丧，恶用德！不货，恶用商！四者天鬻也，天鬻者，天食也。既受食于天，又恶用人？有人之形，无人之情。有人之形，故群于人；无人之情，故是非不得于身。眇乎小哉，所以属于人也。鏊乎大哉，独成其天。

惠子谓庄子曰：“人故无情乎？”庄子曰：“然。”惠子曰：“人而无情，何以谓之人？”庄子曰：“道与之貌，天与之形，恶得不谓之人？”惠子曰：“既谓之人，恶得无情？”庄子曰：“是非吾所谓情也。吾所谓无情者，言人之不以好恶内伤其身，常因自然而不益生也。”惠子曰：“不益生何以有其身？”庄子曰：“道与之貌，天与之形，无以好恶内伤其身。今子外乎子之神，劳乎子之精，倚树而吟，据槁梧而瞑。天选子之形，子以坚白鸣。”

大宗师
---

知天之所为，知人之所为者，至矣。知天之所为者，天而生也。知人之所为者，以其知之所知，以养其知之所不知，终其天年而不中道夭者，是知之盛也。虽然，有患。夫知有所待而后当，其所待者特未定也。庸讵知吾所谓天之非人乎？所谓人之非天乎？且有真人而后有真知。何谓真人？

古之真人，不逆寡，不雄成，不谋士。若然者，过而弗悔，当而不自得也。若然者，登高不栗，入水不濡，入火不热。是知之能登假于道也若此。古之真人，其寝不梦，其觉无忧，其食不甘，其息深深。真人之息以踵，众人之息以喉。屈服者，其嗌言若哇。其嗜欲深者，其天机浅。

古之真人，不知说生，不知恶死。其出不忻，其入不距。倏然而往，倏然而来而已矣。不忘其所始，不求其所终，受而喜之，忘而复之。是之谓不以心捐道，不以人助天。是之谓真人。若然者，其心志，其容寂，其颡颃。凄然似秋，暖然似春。喜怒通四时，与物有宜，而莫知其极。故圣人之用兵也，亡国而不失人心；利泽施于万物，不为爱人。故乐通物，非圣人也。有亲，非仁也；天时，非贤也；利害不通，非君子也；行名失己，非士也；亡身不真，非役人也。若狐不偕、务光、伯夷、叔齐、纪他、申徒狄，是役人之役，适人之适，而不自适其适者也。

古之真人，其状义而不朋，若不足而不承。与乎其觚而不坚也，张乎其虚而不华也，邴邴乎其似喜乎，崔乎其不得已乎，蓄乎进我色也，与乎止我德也，厉乎其似世乎，鏊乎其未可制也，连乎其似好闭也，娩乎忘其言也。以刑为体，以礼为翼，以知为时，以德为循。以刑为体者，绰乎其杀也。以礼为翼者，所以行于世也。以知为时者，不得已于事也。以德为循者，言其与有足者至于丘也，而人真以为勤行者也。故其好之也一，其弗好之也一。其一也一，其不一也一。其一，与天为徒；其不一，与人为徒。天与人不相胜也。是之谓真人。

死生，命也；其有夜旦之常，天也；人之有所不得与，皆物之情也。彼特以天为父，而身犹爱之，而况其卓乎！人特以有君为愈乎已，而身犹死之，而况其真乎！泉涸，鱼相与处于陆，相句以湿，相濡以沫，不如相忘于江湖。与其誉尧而非桀，不如两忘而化其道。夫大块载我以形，劳我以生，佚我以老，息我以死。故善吾生者，乃所以善吾死也。夫藏舟于壑，藏山于泽，谓之固矣。然而夜半，有力者负之而走，昧者不知也。藏大小有宜，由有所遁，若夫藏天下于天下，而不得所遁，是恒物之大情也。特犯人之形，而犹喜之，若人之形者，万化而未始有??也，其为荣可胜计邪？故圣人将游于物之所不得遁而皆存。善夭善老，善始善终，人犹效之，又况万物之所系，而一化之所待乎？

夫道，有情有信，无为无形，可传而不可受，可得而不可见，自本自根。未有天地，自古以固存。神鬼神帝，生天生地。在太极之先而不为高，在六极之下而不为深，先天地生而不为久，长于上古而不为老。郗韦氏得之，以挈天地。伏羲氏得之，以袭气母。维斗得之，终古不忒。日月得之，终古不息。堪坏得之，以袭昆仑。冯夷得之，以游大川。肩吾得之，以处大山。黄帝得之，以登云天。颛顼得之，以处玄宫。禺强得之，立乎北极。西王母得之，坐乎少广，莫知其始，莫知其终。彭祖得之，上及有虞，下及五伯。傅说得之，以相武丁，奄有天下，乘东维，骑箕尾，而比于列星。

南伯子葵问乎女禹曰：“子之年长矣，而色若孺子，何也？”曰：“吾闻道矣。”南伯子葵曰：“道可得学邪？”曰：“恶，恶可！子非其人也。夫卜梁倚有圣人之才，而无圣人之道。我有圣人之道，而无圣人之才。吾欲以教之，庶几其果为圣人乎？不然。以圣人之道，告圣人之才，亦易矣。吾独守而告之，参日而后能外天下。已外天下矣，吾又守之，七日而后能外物。已外物矣，吾又守之，九日而后能外生。已外生矣，而后能朝彻，朝彻而后能见独，见独而后能无古今，无古今而后能入于不死不生。杀生者不死，生生者不生。为物无不将也，无不迎也，无不毁也，无不成也。其名为撄宁。撄宁也者，撄而后成者也。”南伯子葵曰：“子独恶乎闻之？”曰：“闻诸副墨之子。副墨之子，闻诸洛诵之孙。洛诵之孙，闻之瞻明。瞻明，闻之聂许。聂许，闻之需役。需役闻之于讴。于讴闻之玄冥。玄冥闻之参寮。参寮闻之疑始。

子祀、子舆、子犁、子来，四人相与语曰：“孰能以无为首，以生为脊，以死为尻，孰知生死存亡之一体者，吾与之友矣。”四人相视而笑，莫逆于心，遂相与为友。俄而子舆有病，子祀往问之，曰：“伟哉！夫造物者将以予为此拘拘也。曲偻发背，上有五管，颐隐于肩，肩高于项，句赘指天，阴阳之气有畛。”其心闲而无事，蹁跹而鉴于井，曰：“嗟乎，夫造物者又将以予为此拘拘也。”子祀曰：“汝恶之乎？”曰：“亡，予何恶！浸假而化予之左臂以为鸡，予因以求时夜。浸假而化予之右臂以为弹，予因以求枭炙。浸假而化予之尻以为轮，以神为马，予因以乘之，岂更驾哉！且夫得者，时也；失者，顺也。安时而处顺，哀乐不能入也，此古之所谓悬解也。而不能自解者，物有结之。且夫物不胜天久矣，吾又何恶焉？”俄而子来有病，喘喘然将死，其妻子环而泣之，子犁往问之，曰：“叱，避！无惮化！”倚其户与之语曰：“伟哉造物，又将奚以汝为，将奚以汝适？以汝为鼠肝乎？以汝为虫臂乎？”子来曰：“父母于子，东西南北，唯命之从。阴阳于人，不翅于父母。彼近吾死而我不听，我则悍矣。彼何罪焉？夫大块载我以形，劳我以生，佚我以老，息我以死。故善吾生者，乃所以善吾死也。今之大冶铸金，金踊跃曰：我必且为镆铘。大冶必以为不祥之金。今一犯人之形，而曰人耳人耳，夫造化者必以为不祥之人。今一以天地为大炉，以造化为大冶，恶乎往而不可哉？”成然寐，遽然觉。

子桑户、孟子反、子琴张，三人相与为友，曰：“孰能相与于无相与，相为于无相为？孰能登天游雾，挠挑无极，相忘以生，无所终穷？”三人相视而笑，莫逆于心，遂相与为友。莫然有间，而子桑户死，未葬，孔子闻之，使子贡往侍事焉，或鼓琴，相和而歌曰：“嗟来桑户乎！嗟来桑户乎！而已反其真，而我犹为人猗。”子贡趋而进曰：“敢问临尸而歌，礼乎？”二人相视而笑，曰：“是恶知礼意！”子贡反以告孔子曰：“彼何人者邪？修行无有，而外其形骸，临尸而歌，颜色不变，无以命之。彼何人者邪？”孔子曰：“彼游方之外者也，而丘游方之内者也。外内不相及，而求使汝往吊之，丘则陋矣。彼方且与造物者为人，而游乎天地之一气。彼以生为附赘悬疣，以死为决芄溃痈。夫若然者，又恶乎知死生先后之所在？假于异物，托于同体，忘其肝胆，遗其耳目，反复终始，不知端倪。芒然彷徨乎尘垢之外，逍遥乎无为之业。彼又恶能愦愦然为世俗之礼，以观众人之耳目哉！”子贡曰：“然则夫子何方之依？”孔子曰：“丘，天之戮民也。虽然，吾与汝共之。”子贡曰：“敢问其方？”孔子曰：“鱼相造乎水，人相造乎道。相造乎水者，穿池而养给。相造乎道者，无事而生定。故曰：鱼相忘乎江湖，人相忘乎道术。”子贡曰：“敢问畸人？”曰：“畸人者，畸于人而侔于天。故曰：天之小人，人之君子；人之君子，天之小人也。”

颜回问仲尼曰：“孟孙才，其母死，哭泣无涕，中心不戚，居丧不哀，无是三者，以善处丧盖鲁国。固有无其实而得其名者乎？回壹怪之。”仲尼曰：“夫孟孙氏尽之矣，进于知矣。唯简之而不得，夫已有所简矣。孟孙氏不知所以生，不知所以死，不知就先，不知就后。若化为物，以待其所不知之化已乎。且方将化，恶知不化哉？方将不化，恶知已化哉？吾特与汝其梦未始觉者邪。且彼有骇形而无损心，有旦宅而无情死。孟孙氏特觉，人哭亦哭，是自其所以乃。且也相与吾之耳矣。庸讵知吾所谓吾之乎！且汝梦为鸟而厉乎天，梦为鱼而没于渊，不识今之言者，其觉者乎，梦者乎？造适不及笑，献笑不及排，安排而去化，乃入于寮天一。”

意而子见许由，许由曰：“尧何以资汝？”意而子曰：“尧谓我汝必躬服仁义而明言是非。”许由曰：“而奚为来轵？夫尧既以黥汝以仁义，而鼻汝以是非矣！汝将何以游夫遥荡恣雎转徙之涂乎？”意而子曰：“虽然，吾愿游于其藩。”许由曰：“不然。夫盲者无以与乎眉目颜色之好，瞽者无以与乎青黄黼黻之观。”意而子曰：“夫无庄之失其美，据梁之失其力，黄帝之无其知，皆在炉捶之间耳。庸讵知夫造物者之不息我黥而补我鼻，使我乘成以随先生邪？”许由曰：“噫，未可知也。我为汝言其大略。吾师乎，吾师乎，齑万物而不为义，泽及万世而不为仁，长于上古而不为老，覆载天地雕刻众形而不为巧，此所游已。”

颜回曰：“回益矣！”仲尼曰：“何谓也？”曰：“回忘仁义矣！”曰：“可矣，犹未也。”他日复见曰：“回益矣！”曰：“何谓也？”曰：“回忘礼乐矣！”曰：“可矣，犹未也。”他日复见曰：“回益矣！”曰：“何谓也？”曰：“回坐忘矣！”仲尼蹴然曰：“何谓坐忘？”颜回曰：“堕肢体，黜聪明，离形去知，同于大通。此谓坐忘。”仲尼曰：“同则无好也，化则无常也，而果其贤乎！丘也请从而后也。”

子舆与子桑友，而霖雨十日。子舆曰：“子桑殆病矣。”裹饭而往食之，至子桑之门，则若歌若哭，鼓琴曰：“父邪母邪？天乎人乎？”有不任其声而趋举其诗焉。子舆入曰：“子之歌诗，何故若是？”曰：“吾思乎使我至此极者而弗得也。父母岂欲吾贫哉？天无私覆，地无私载，天地岂私贫我哉？求其为之者而不得也。然而至此极者，命也夫！”   


应帝王
---

啮缺问于王倪，四问而四不知，啮缺因跃而大喜，行以告蒲衣子。蒲衣子曰：“而乃今知之乎！有虞氏不及泰氏，有虞氏其犹藏仁以要人，亦得人矣，而非始出于非人。泰氏其卧徐徐，其觉于于，一已己为马，一以己为牛，其知情信，其的德甚真，而未始入于非人。

肩吾见狂接舆，狂接舆曰：“日中始何以语汝？”肩吾曰：“告我君人者以己出经式，人孰敢不听而化诸？”狂接舆曰：“是欺德也，其于治天下也犹涉海凿河，而使蚊负山也。夫圣人之知也治外乎，正而后行，确乎能其事者而已矣。且鸟高飞以避缯弋之害，鼹鼠深穴乎神丘之下，以避薰凿之患，而曾二虫之无知。

天根游于殷阳，至蓼水之上，适遭无名人而问焉，曰：“请问为天下？”无名人曰：“去，汝鄙人也，何问之不豫也！予方将与造物者为人，厌则又乘夫莽眇之鸟，以出六极之外，而游无何有之乡，以处圹琅之野，汝又何吊以治天下感予之心为？”又复问，无名人曰：“汝游心于淡，合气于漠，顺物自然而无容私焉，而天下治矣。”

阳子居讲老聃曰：“有人于此，向疾强梁，物彻疏明，学道不倦。如是者可比明王乎？”老聃曰：“是于圣人也，胥易技系，劳形怵心者也。且曰虎豹之文来田，猿狙之便、执嫠之狗来藉，如是者可比明王乎？”阳子居蹴然曰：“敢问明王之治？”老聃曰：“明王之治，功盖天下而似不自已，化贷万物而民弗恃，有莫举名，使物自喜，立乎不测，而游于无有者也。”

郑有神巫曰季咸，知人之生死存亡，祸福寿夭，期以岁月旬日若神，郑人见之，皆弃而走，列子见之而心醉，归以告壶子，曰：“始吾以夫子之道为至矣，则又有至焉者矣。”壶子曰：“吾与汝既其文，未既其实，而固得道与？众雌而无雄，而又奚卵焉？而以道与世亢，必信。夫故使人得而相汝，尝试与来，以予示之。”明日列子与之见壶子，出而谓列子曰：“嘻，子之先生死矣，弗活矣，不以旬数矣。吾见怪焉，见湿灰焉。”列子入，泣涕沾襟，以告壶子，壶子曰：“向吾示之以地文，萌乎不震不正，是殆见吾杜德机也。尝又与来。”明日，又与之见壶子，出而谓列子曰：“幸矣，子之先生遇我也，有瘳矣，全然有生矣。吾见其杜权矣。”列子入以告壶子，壶子曰：“向吾示之以天壤，名实不入，是殆见吾善者机也。尝又与来。”明日，又与之见壶子，出而谓列子曰：“子之先生不齐，吾无得而相焉。试齐，且复相之。”列子入，以告壶子，壶子曰：“吾向示之以太冲莫胜，是殆见吾衡气机也。鲵桓之审为渊，止水之审为渊，流水之审为渊，渊有九名，此处三焉。尝又与来。”明日，又与之见壶子，立未定，自失而走，壶子曰：“追之。”列子追之不及，反以报壶子，曰：“已灭矣，已失矣，吾弗及也。”壶子曰：“向吾示之以未始出吾宗，吾与之虚而委蛇，不知其谁何，因以为弟靡，因以为波流，故逃也。”然后列子自以为未始学而归，三年不出，我其妻炊，食豕如食人，于事无与亲，雕琢复朴，块然独以其形立，纷而封哉，一以是终。

无为名尸，无为谋府，无为事任，无为知主，体尽无穷，而游无朕，尽其所受于天，而无见得，亦虚而已。至人之用心若镜，不将不迎，应而不藏，故能胜物而不伤。

南海之帝为倏，北海之帝为忽，中央之帝为浑沌。倏与忽时相与遇于浑沌之地，浑沌待之甚善，倏与忽谋报浑沌之德，曰：“人皆有七窍以视听食息，此独无有，尝试凿之。”日凿一窍，七日而浑沌死。   


骈拇第八
----

骈拇枝指，出乎性哉，而侈于德；附赘悬疣，出乎形哉，而侈于性；多方乎仁义而用之者，列于五藏哉，而非道德之正也。是故骈于足者，连无用之肉也；枝于手者，树无用之指也；多文骈枝于五藏之情者，淫僻于仁义之行，而多方于聪明之用也。是故骈于明者，乱无色，淫文章。青黄黼黻之煌煌，非乎，而离朱是已。多于聪者，乱五声，淫六律，金石丝竹黄钟大吕之声，非乎，而师旷是已。枝于仁者，翟德塞性，以收名声，使天下簧鼓以奉不及之法，非乎，而曾史是已。骈于辩者，垒瓦结绳窜句，游心于坚白同异之间，而敝跬誉无用之言，非乎，而杨墨是已。故此皆骈旁枝之道，非天下之至正也。彼正正者，不失其性命之情。故合者不为骈，而枝者不为歧，长者不为有余，短者不为不足。是故凫胫虽短，续之则忧，鹤胫虽长，断之则悲。故性长非所断，性短非所续，我所去忧也。意仁义其非人情乎？彼仁人何其多忧也！且夫骈于拇者，决之则泣，枝于手者，纥之则啼。二者或有余于数，或不足于数，其于忧一也。今世之仁人，藁目而忧世之患，不仁之人，决性命之情而饕富贵。故意仁义之非人情乎。自三代以下者，天下何其嚣嚣也。且夫待钩绳规矩而正者，是削其性，代绳约胶漆而固者，是侵其德也。屈折礼乐，吁俞仁义，以慰天下之心者，此失其常然也。天下有常然，常然者，曲者不以钩，直者不以绳，圆者不以规，方者不以矩，附离不以胶漆，约束不以耱索。故天下诱然，皆生而不知其所以生，同焉皆得，而不知其所以得。故古今不二，不可亏也。则仁义奚连连如胶漆耱索，而游乎道德之间为哉？使天下之惑也。夫小惑易方，大惑易性。何以知其然邪？自虞氏招仁义以挠天下也，天下莫不奔命于仁义，是非以仁义易其性与？故尝试论之，自三代以下者，天下莫不以物易其性矣。小人则以身殉利，士则以身殉名，大夫则以身殉家，圣人则以身殉天下。故此数子者，事业不同，名声异号，其于伤性以身为殉一也。臧与谷二人，相与牧羊而俱亡其羊，问臧奚事，则挟荚读书，问谷奚事，则博塞以游。二人者，事业不同，其于亡羊均也。伯夷死名于首阳之下，盗跖死利于东陵之上。二人者，所死不同，其于残生伤性均也。奚必伯夷之是，而盗跖之非乎？天下尽殉也。彼其所殉，仁义也，则俗谓之君子。其所殉，货财也，则俗谓之小人。其殉一也，则有君子焉，有小人焉。若其残生损性，则盗跖亦伯夷已，又恶取君子小人于其间哉！且夫属其性乎仁义则和，虽通如曾史，非吾所谓臧也。属其性于五味，虽通如俞儿，非吾所谓臧也。属其性乎五声，虽通如师旷，非吾所谓聪也。属其性乎五色，虽通如离朱，非吾所谓明也。吾所谓臧者，非仁义之谓也，臧于其德而已矣。吾所谓臧者，非所谓仁义之谓也，任其性命之情而已矣。吾所谓聪者，非谓其闻彼也，自闻而已矣。吾所谓明者，非谓其见彼也，自见而已矣。夫不自见而见彼，不自得而得彼者，是得人之得，而不自得其得，适人之适，而不自适其适者也。夫适人之适，而不自适其适，虽盗跖与伯夷，是同为淫僻也。余愧乎道德，是以上不敢为仁义之操，而下不敢为淫僻之行也。

马蹄第九
----

马蹄，可以践霜雪，毛可以御风寒，纥草饮水，翘足而陆，此马之真性也。虽有义台路寝，无所用之。及至伯乐曰：“我善治马。”烧之剔之，刻之络之，连之以羁络，编之以皂栈，马之死者十二三矣。饥之渴之，驰之骤之，整之齐之，前有橛饰之患，而后有鞭荚之威，而马之死者已过半矣。陶者曰：“我善治埴。”圆者中规，方者中矩。匠人曰：“我善治水。”曲者中钩，直者应绳。夫埴木之性，岂欲中规矩钩绳哉？然且世世称之，曰伯乐善治马，而陶匠善治埴水，此亦治天下者之过也。吾意善治天下者不然，彼民有常性，织而衣，耕而食，是谓同德。一而不党，命曰天放。故至德之世，其行填填，其视颠颠。当是时也，山无蹊隧，泽无舟梁，万物群生，连属其乡，禽兽成群，草木遂长。是故禽兽可系羁而游，鸟雀之巢可攀援而窥。夫至德之世，同与禽兽居，族与万物并，恶乎知君子小人哉！同乎无知，其德不离，同乎无欲，是谓素朴。素朴而民性得矣。及至圣人，蹩蹑为仁，缇歧为义，而天下始疑矣。澶漫为乐，摘僻为礼，而天下始分矣。故纯朴不残，孰为牺尊？白玉不毁，孰为圭璋？道德不废，安取仁义？性情不离，安用礼乐？五色不乱，孰为文采？五声不乱，孰应六律？夫残朴以为器，工匠之罪也。毁道德以为仁义，圣人之过也。夫马陆居则食草饮水，喜则交颈相靡，怒则分背相蹄，那马知已此矣！夫加之以衡扼，齐之以月题，而马知介倪、湮扼、鸷曼，诡衔窃辔。故马之知而态至盗者，伯乐之罪也。夫赫胥氏之时，民居不知所为，行不知所之，含哺而熙，鼓腹而游，民能矣此矣。及至圣人，屈折礼乐，以匡天下之形，悬企仁义，以慰天下之心，而民乃始蹄歧好知，争归于利，不可止也。此亦圣人之过也。

祛箧第十
----

将为祛箧探囊发匮之盗而为守备，则必摄缄滕，固扃谲，此世俗之所谓知也。然而巨盗至，则负匮揭箧担囊而趋，唯恐缄滕扃谲之不固也。然则向之所谓知者，不乃为大盗积者也？故尝试论之，世俗之所谓知者，有不为大盗积者乎？所谓圣者，有不为大盗守者乎？何以知其然邪？昔者齐国邻邑相望，鸡狗之音相闻，网罟之所布，耒缛之所刺，方二千余里，阖四境之内，所以立宗庙社稷，治邑屋州闾乡曲则和，曷尝不法圣人哉？然而田成子一旦杀齐君而盗其国，所盗者岂独其国邪，并与其圣知之法而盗之。故田成子有乎盗贼之名，而身处尧舜之安，小国不敢非，大国不敢诛，十二世有齐国。则是不乃窃齐国，并与其圣知之法，以守其盗贼之身乎？尝试论之，世俗之所谓至知者，有不为大盗积者乎？所谓至圣者，有不为大盗守者乎？何以知其然邪？昔者龙逢斩，比干剖，苌弘刖，子胥靡，故四子之贤，而身不免乎戮。故盗跖之徒，问于跖曰：“盗亦有道乎？”跖曰：“何适而无有道邪？夫妄意室中之藏，圣也。入先，勇也。出后，义也。知可否，知也。分均，仁也。五者不备，而能成大盗者，天下未之有也。”由是观之，善人不得圣人之道不立，跖不得圣人之道不行。天下之善人少而不善人多，则善人之利天下也少，而害天下也多。故曰：唇竭则齿寒，鲁酒薄而邯郸围，圣人生而大盗起。掊击圣人，纵舍盗贼，而天下始治矣。夫川竭而谷虚，丘夷而渊实，圣人已死，则大盗不起，天下平而无故矣。圣人不死，大盗不止。虽重圣人而治天下，则是重利盗跖也。为之斗斛以量之，则并与斗斛而窃之，为之权衡以称之，则并与权衡而窃之，为之符玺以信之，则并与符玺而窃之，为之仁义以矫之，则并与仁义而窃之。何以知其然邪？彼窃钩者诛，窃国者为诸侯。诸侯之门，而仁义存焉。则是非窃仁义圣知邪？故逐于大盗，揭诸侯，窃仁义，并斗斛权衡符玺之利者，虽有轩冕之赏弗能劝，斧钺之威弗能禁。此重利盗跖而使不可禁者，是乃圣人之过也。故曰：鱼不可脱于渊，国之利器不可以示人。彼圣人者，天下之利器也，非所以明天下也。故绝圣弃知，大盗乃止，挞玉毁珠，小盗不起，焚符破玺，而民朴鄙，掊斗折衡，而民不争，殚残天下之圣法，而民始可与论议。翟乱六律，铄绝竽瑟，塞瞽旷之耳，而天下始人含其聪矣。灭文章，散五采，胶离朱之目，而天下始人含其明矣。毁绝钩绳，而弃规矩，丽工捶之指，而天下始人有其巧矣。故曰：大巧若拙。削曾史之行，钳杨墨之口，攘弃仁义，而天下之德始玄同矣。彼人含其明，则天下不铄矣。人含其聪，则天下不累矣。人含其知，则天下不惑矣。人含其德，则天下不僻矣。彼曾史杨墨师旷工捶离朱，皆外立其德，而以瀹乱天下者也，法之所无用也。子独不知至德之世乎？昔者容成氏、大庭氏、伯皇氏、中央氏、栗陆氏、骊畜氏、轩辕氏、赫胥氏、尊庐氏、祝融氏、伏羲氏、神农氏，当是时也，民结绳而用之，甘其食，美其服，乐其俗，安其居，邻国相望，鸡狗之音相闻，民至老死而不相往来。若此之时，则至治已。今遂至使民延颈举踵曰：某所有贤者，赢粮而趣之。则内弃其亲，而外去其主之事，足迹接乎诸侯之境，车轨结乎千里之外，则是上好知之过也。上诚好知而无道，则天下大乱矣。何以知其然邪？夫弓弩毕弋机变之知多，则鸟乱于上矣。钩饵网罟罾句之知多，则鱼乱于水矣。削格罗落苴罘之知多，则兽乱于泽矣。知诈渐毒颉滑坚白解垢同异之变多，则俗惑于辩矣。故天下每每大乱，罪在于好知。故天下皆知求其所不知，而莫知求其所已知者，皆知非其所不善，而莫知非其所已善者，是以天下大乱。夫上悖日月知明，下烁山川知精，中堕四时知施，惴软知虫，肖翘之物，莫不失其性。甚矣，夫好知之乱天下也，自三代以下者是已。舍夫种种之民，而悦夫役役知佞，释夫恬淡无为，而悦夫谆谆知意，谆谆已乱天下矣！

在宥第十一
-----

闻在宥天下，不闻治天下也。在之也者，恐天下之淫其性也；囿之也者，恐天下之迁其德也。天下不淫其性，不迁其德，有治天下者哉？

昔尧之治天下也，使天下欣欣焉人乐其性，是不恬也。桀之治天下也，使天下瘁瘁焉人苦其性，是不愉也。夫不恬不愉，非德也。非德也而可长久者，天下无之。人大喜邪，毗于阳；大怒邪，毗于阴。阴阳并毗，四时不至，寒暑之和不成，其反伤人之形乎！使人喜怒失位，居处无常，思虑不自得，中道不成章，于是乎天下始乔诘卓鸷，而后有盗跖曾史之行。故举天下以赏其善者不足，举天下以伐其恶者不给。故天下之大，不足以赏罚。自三代以下者，匈匈焉终以赏罚为事，彼何暇安其性命之情哉？而且说明邪，是淫于色也；说聪邪，是淫于声也；说仁邪，是乱于德也；说义邪，是悖于理也；说礼邪，是相于技也；说乐邪，是相于淫也；说圣邪，是相于艺也；说知邪，是相于疵也。天下将安其性命之情，之八者存可也。天下将不安其性命之情，之八者乃始脔卷伧囊，而乱天下也。而天下乃始尊之惜之，甚矣天下之惑也！岂直过而去之邪，乃齐戒以言之，跪坐以进之，鼓歌以舞之，吾若是何哉？故君子不得已而临位天下，莫若无为。无为也而后安其性命之情。故贵以身于为天下，则可以托天下；爱以身于为天下，则可以寄天下。故君子苟能无解其五藏，无擢其聪明，尸居而龙见，渊默而雷声，神动而天随，从容无为而万物炊累焉。吾又何暇治天下哉！

崔瞿问于老聃曰：“不治天下，安藏人心？”老聃曰：“汝慎无撄人心。人心排下而进上，上下囚杀，淖约柔乎刚强，廉刿雕琢，其热焦火，其寒凝冰，其疾俯仰之间，而再抚四海之外，其居也渊而静，其动也悬而天，贲骄而不可系者，其唯人心乎！昔者黄帝始以仁义撄人之心，尧舜于是乎股无鲅，胫无毛，以养天下之形，愁其五藏以为仁义，矜其血气以规法度，然犹有不胜也。尧于是放欢兜于崇山，投三苗于三桅，流共工于幽都，此不胜天下也夫。施及三王，而天下大骇矣。下有桀跖，上有曾史，而儒墨毕起，于是乎喜怒相疑，愚知相欺，善否相非，诞信相讥，而天下衰矣。大德不同，而性命烂漫矣；天下好知，而百姓求竭矣。于是乎斫锯制焉，绳墨杀焉，锤凿决焉，天下脊脊大乱，罪在撄人心。故贤者伏处大山湛岩之下，而万乘之君忧栗乎庙堂之上。今世殊死者相枕也，衍杨者相推也，刑戮者相望也，而儒墨乃始离歧攘臂乎桎梏之间，意甚矣哉！其无愧而不知耻也甚矣。吾未知圣知之不为衍杨接习也，仁义之不为桎梏凿肭也，焉知曾史之不为桀跖藁矢也？故曰：绝圣弃知而天下大治。”

黄帝立为天子十九年，命行天下，闻广成子在于空同之上，故往见之，曰：“我闻吾子达于至道，敢问至道之精？吾欲取天地之精，以佐五谷，以养民人。吾又欲官阴阳以遂群生。”广成子曰：“而所欲问者，物之质也。而所欲官者，物之残也。自而治天下，云气不待族而雨，草木不待黄而落，日月之光，益以荒矣，而佞人之心翦翦者，又奚足以语至道？”黄帝退，捐天下，筑特室，席白茅，闲居三月，复往邀之，广成子南首而卧，黄帝顺下风，膝行而进，再拜稽手而问曰：“闻吾子达于至道，敢问治身奈何而可以长久？”广成子蹶然而起，曰：“善哉问乎！来，吾语汝至道。至道之精，窈窈冥冥；至道之极，昏昏默默，无视无听，抱神以静。形将自正，必静必清。无劳汝形，无摇汝精，乃可以长生。目无所见，耳无所闻，心无所知，汝神将守形，形乃长生。慎汝内，闭汝外，多知为败。我为汝遂于大明之上矣，至彼至阳之原也，为汝入于窈冥之门矣，至彼至阴之原也。天地有宫，阴阳有藏，慎守汝身，物将自壮。我守其一以处其和，故我修身千二百岁矣，吾形未尝衰。”黄帝再拜稽首曰：“广成子之谓天矣！”广成子曰：“来，吾语汝。彼其物无穷而人皆以为有终，彼其物无测而人皆以为有极。得吾道者，上为皇而下为王，失吾道者，上见光而下为土。今夫百昌，皆生于土，而反于土。故余将去汝，入无穷之门，以游无极之野。吾与日月参光，吾与天地为常。当我昏乎？远我昏乎？人其尽死，而我独存乎？”

云将东游，过扶摇之枝，而适遭鸿蒙，鸿蒙方将拊髀雀跃而游。云将见之，倘然止，贽然立，曰：“叟何人邪？叟何为此？”鸿蒙拊髀雀跃不辍，对云将曰：“游。”云将曰：“朕愿有问也。”鸿蒙仰而视云将曰：“吁！”云将曰：“天气不合，地气郁结，六气不调，四时不节。今我愿合六气之精，以育群生，为之奈何？”鸿蒙拊髀雀跃掉头曰：“吾弗知，吾弗知。”云将不得问。又三年，东游过有宋之野，而适遭鸿蒙，云将大喜，行趋而进曰：“曰天忘朕邪，天忘朕邪？”再拜稽首，愿闻于鸿蒙。鸿蒙曰：“浮游不知所求，猖狂不知所在。游者鞅掌，以观无妄。朕又何知！”云将曰：“朕也自以为猖狂，而百姓随予所往。朕也不得已于民。今则民之放也，愿闻一言。”鸿蒙曰：“乱天之经，逆物之情，玄天弗成。解兽之群，而鸟皆夜鸣，灾及草木，祸及止虫，意治人之过也。”云将曰：“然则无奈何？”鸿蒙曰：“意，毒哉！仟仟乎归矣！”云将曰：“吾遇天难，愿闻一言。”鸿蒙曰：“意，心养。汝徙处无为，而物自化。堕尔形体，吐尔聪明，伦与物忘，大同乎悻溟，解心释神，莫然吾魂。万物云云，各复其根。各复其根而不知，浑浑沌沌，终身不离。若彼知之，乃是离之。无问其名，无窥其情，物故自生。”云将曰：“天降朕以德，示朕以默，躬身求之，乃今也得。”再拜稽首，起辞而行。

世俗之人，皆喜人之同乎己，而恶人之异于己也。同于己而欲之，异于己而不欲者，以出乎众为心也。夫以出于众为心者，曷尝出乎众哉？因众以宁，所闻不如众技众矣，而欲为人之国者，此揽乎三王之利，而不见其患者也。此以人之国侥幸也，几何侥幸而不丧人之国乎？其存人之国也，无万分之一；其丧人之国也，一不成而万有余丧矣。悲夫，有土者之不知也。夫有土者，有大物也。有大物者，不可以物物，而不物故能物物。明乎物物者之非物也，岂独治天下百姓而已哉？出入六合，游乎九州，独往独来，是谓独有。独有之人，是谓至贵。

大人之教，若形之于影，声之于响。有问而应之，尽其所怀，为天下配。处乎无响，行乎无方，挈汝适复之，挠挠以游无端。出入无旁，与日无始，颂论形躯，合乎大同。大同而无已，无已而恶乎得有有？睹有者昔之君子，睹无者天地之友。

贱而不可不任者，物也；卑而不可不因者，民也；匿而不可不为者，事也；粗而不可不陈者，法也；远而不可不居者，义也；亲而不可不广者，仁也；节而不可不积者，礼也；中而不可不高者，德也；一而不可不易者，道也；神而不可不为者，天也。故圣人观于天而不助，成于德而不累，出于道而不谋，会于仁而不恃，薄于义而不积，应于礼而不讳，接于事而不辞，齐于法而不乱，恃于民而不轻，因于物而不去。物者莫足为也，而不可不为。不道于天下者，不纯于德。不通于道者，无自而可。不明于道者，悲夫！何谓道？有天道，有人道。无为而尊者，天道也；有为而累者，人道也。主者，天道也；臣者，人道也。相去远矣，不可不察也。

天地第十二
-----

天地虽大，其化均也；万物虽多，其治一也；人卒虽众，其主君也。君原于德，而成于天。故曰玄。古之君天下，无为也，天德而已矣。以道观言，而天下之君正。以道观分，而君臣之义明。以道观能，而天下之官??。以道泛观，而万物之应备。故通于天地者，得也；行于万物者，道也。上治人者，事也；能有所艺者，技也。技兼于事，事兼于义，义兼于德，德兼于道，道兼于天。故曰：古之畜天下者，无欲而天下足，无为而万物化，渊静而百姓定。记曰：通于一而万事毕，无心得而鬼神服。

夫子曰：夫道，覆载万物者也。洋洋乎大哉！君子不可以不刳心焉。无为为之之谓天，无为言之之谓德，爱人利物之谓仁，不同同之之谓大，行不崖异之谓宽，有万不同之谓富。故执德之谓纪，德成之谓力，循于道之谓备，不以物挫志之谓完。君子明于此十者，则韬乎其事心之大也，沛乎其为万物逝也。若然者，藏金于山，藏珠于渊，不利货财，不近富贵，不乐寿，不哀夭，不荣通，不丑穷，不拘一世之利以为己私分，不以王天下为己处显，显则明。万物一府，死生同状。

夫子曰：夫道，渊乎其居也，寥乎其清也。金石不得无以鸣。故金石有声，不考不鸣。万物孰能定之？夫王德之人，素逝而耻通于事，立之本原，而知通于神，故其德广。其心之出，有物采之。故形非道不生，生非德不明。存形穷生，立德明道，非王德者邪？荡荡乎忽然出，勃然动，而万物从之乎！此之谓王德之人。视乎冥冥，听乎无声，冥冥之中，独见晓焉。无声之中，独闻和焉。故深之又深，而能物焉。神之又神，而能精焉。故其与万物接也，至无而供其求，时骋而要其宿，大小长短修远。黄帝游乎赤水之北，登乎昆仑之丘，而南望还归，遗其玄珠，使知索之而不得，使离朱索之而不得，使吃诟索之而不得也。乃使象罔，象罔得之。黄帝曰：“异哉，象罔乃可以得之乎？”

尧之师曰许由，许由之师曰啮缺，啮缺之师曰王倪，王倪之师曰被衣。尧问于许由曰：“啮缺可以配天乎？吾藉王倪以要之。”许由曰：“殆哉圾乎天下。啮缺之为人也，聪明睿知，给数以敏，其性过人，而又乃以人受天。彼审乎禁过，而不知过之所由生。与之配天乎？彼且乘人而无天。方且本身而异形，方且尊知而火驰，方且为绪使，方且为物陔，方且四顾而物应，方且应众宜，方且与物化而未始有恒。夫何足以配天乎？虽然，有族有祖，可以为众父，而不可以为众父父。治乱之率也，北面之祸也，南面之贼也。”

尧观乎华，华封人曰：“嘻，圣人！请祝圣人，使圣人寿。”尧曰：“辞。”“使圣人富。”尧曰：“辞。”“使圣人多男子。”尧曰：“辞。”封人曰：“寿富多男子，人之所欲也，汝独不欲，何邪？”尧曰：“多男子则多惧，富则多事，寿则多辱。是三者，非所以养德也，故辞。”封人曰：“始也我以汝为圣人邪，今然君子也。天生万民，必授之职。多男子而授之职，则何惧之有？富而使人分之，则何事之有？夫圣人鹑居而彀食，鸟行而无彰。天下有道，则与物皆昌，天下无道，则修德就闲，千岁厌世，去而上仙，乘彼白云，至于帝乡，三患莫至，身常无殃，则何辱之有？”封人去之，尧随之曰：“请问。”封人曰：“退已。”

尧治天下，伯成子高立为诸侯。尧授舜，舜授禹，伯成子高辞为诸侯而耕，禹往见之，则耕在野。禹趋就下风，立而问焉，曰：“昔尧治天下，吾子立为诸侯，尧授舜，舜授予，而吾子辞为诸侯而耕，敢问其故何也？”子高曰：“昔尧治天下，不赏而民劝，不罚而民畏。今子赏罚而民且不仁，德自此衰，刑自此立，后世之乱，自此始矣。夫子盍行邪！无落吾事。”挹挹乎耕而不顾。

泰初有无，无有无名。一之所起，有一而未形。物得以生谓之德，未形者有分，且然无间，谓之命。留动而生物，物成生理，谓之形。形体保神，各有仪则，谓之性。性修反德，德至同于初，同乃虚，虚乃大，合喙鸣。喙鸣合，与天地为合，其合昏昏，若愚若昏，是谓玄德，同乎大顺。

夫子问于老聃曰：“有人治道若相放，可不可，然不然。辩者有言曰：离坚白，若悬寓。若是则可谓圣人乎？”老聃曰：“是胥易技系劳形怵心者也。执留之狗成思，猿狙之便，自山林来。丘，予告若而所不能闻与而所不能言。凡有首有趾，无心无耳者众，有形者与无形无状而皆存者尽无。其动止也，其死生也，其废起也。此又非其所以也。有治在人，忘乎物，忘乎天，其名为忘已，忘已之人，是之谓入于天。”

将闾勉见季彻曰：“鲁君谓勉也曰：请受教。辞不获，既已告矣，未知中否，请尝荐之。吾谓鲁君曰：必服恭俭，拔出公忠之属，而无阿私。民孰敢不辑？”季彻局局然笑曰：“若夫子之言于帝王之德，犹螳螂之怒臂以当车辙，则必不胜任矣。且若是，则其自为处危，其观台多物，将往投迹者众。”将闾勉觑觑然惊曰：“勉也茫若于夫子之所言矣。虽然，愿闻先生之言其风也。”季彻曰：“大圣之治天下也，摇荡民心，使之成教易俗，举灭其贼心，而皆进其独志。若性之自为，而民不知其所由然。若然者，岂兄尧舜之教民，溟滓焉弟之哉。欲同乎德而心居矣。”

子贡南游于楚，反于晋，过汉阴，见一丈人，方将为圃畦，凿隧而入井，抱瓮而出灌，骨骨然用力甚多，而见功寡。子贡曰：“有械于此，一日浸百畦，用力甚寡而见功甚多，夫子不欲乎？”为圃者仰而视之曰：“奈何？”曰：“凿木为机，后重前轻，挈水若抽，数如佚汤，其名为槔。”为圃者忿然作色而笑曰：“吾闻之吾师，有机械者必有机事，有机事者必有机心。机心存于胸中，则纯白不备。纯白不备，则神生不定。神生不定者，道之所不载也。吾非不知，羞而不为也。”子贡瞒然惭，俯而不对，有间，为圃者曰：“子奚为者邪？”曰：“孔丘之徒也。”为圃者曰：“子非夫博学以拟圣，于于以盖众，独弦哀歌以卖名声于天下者乎？汝方将忘汝神气，堕汝形骸，而庶几乎！而身之不能治，而何暇治天下乎？子往矣，无乏吾事。”

子贡卑陬失色，琐琐然不自得，行三十里而后愈。其弟子曰：“向之人何为者邪？夫子何故见之变容失色，终日不自反邪？”曰：“始以为天下一人耳，不知复有夫人也。吾闻之夫子，事求可，功求成，用功少，见功多者，圣人之道。今徒不然。执道者德全，德全者形全，形全者神全，神全者圣人之道也。托生与民并行，而不知其所之。茫乎搞备哉！功利机巧必忘夫人之心。若夫人者，非其志不之，非其心不为，虽以天下誉之，得其所谓，骜然不顾。以天下非之，失其所谓，傥然不受。天下之非誉，无益损焉。是谓全德之人哉。我之谓风波之民。”反于鲁，以告孔子。孔子曰：“彼假修浑沌氏之术者也。识其一不知其二，治其内不治其外。夫明白入素，无为复朴，体性抱神，以游世俗之间者，汝将固惊邪。且浑沌氏之术，予与汝何足以识之哉？”

谆芒将东之大壑，适遇苑风于东海之滨。苑风曰：“子将奚之？”曰：“将之大壑。”曰：“奚为焉？”曰：“夫大壑之为物也，注焉而不满，酌焉而不竭。吾将游焉！”苑风曰：“夫子无意横目之民乎？愿闻圣治。”谆芒曰：“圣治乎？官施而不失其宜，拔举而不失其能，毕见其情事而行其所为，行言自为而天下化。手挠顾指，四方之民莫不俱至，此之谓圣治。”“愿闻德人。”曰：“德人者，居无思，行无虑，不藏是非美恶。四海之内，共利之之谓悦，共给之之谓安。惆乎若婴儿之失其母也，傥乎若行而失其道也。财用有余而不知其所自来，饮食取足而不知其所从，此谓德人之容。”“愿闻神人。”曰：“上神乘光，与形灭亡，是谓照旷。致命尽情，天地乐而万事销亡，万物复情，此之谓混冥。”

门无鬼与赤张满稽观于武王之师，赤张满稽曰：“不及有虞氏乎！故离此患也。”门无鬼曰：“天下均治而有虞氏治之邪？其乱而后治之与？”赤张满稽曰：“天下均治之为愿，而何计以有虞氏为！有虞氏之药疡也，秃而施发，病而求医。孝子操药以修慈父，其色憔然，圣人羞之。至德之世，不尚贤，不使能，上如标枝，民如野鹿。端正而不知以为义，相爱而不知以为仁，实而不知以为忠，当而不知以为信，蠢动而相使不以为赐。是故行而无迹，事而无传。”

孝子不谀其亲，忠臣不谄其居，臣、子之盛也。亲之所言而然，所行而善，则世俗谓之不肖子；君之所言而然，所行而善，则世俗谓之不肖臣。而未知此其必然邪？世俗之所谓然而然之，所谓善而善之，则不谓之导谀之人也！然则俗故严于亲而尊于君邪？谓己道人，则勃然作色；谓己谀人，则怫然作色。而终身道人也，终身谀人也，合譬饰辞聚众也，是终始本末不相坐。垂衣裳，设采色，动容貌，以媚一世，而不自谓道谀；与夫人之为徒，通是非，而不自谓众人，愚之至也。知其愚者，非大愚也；知其惑者，非大惑也。大惑者，终身不解；大愚者，终身不灵。三人行而一人惑，所适者，犹可致也，惑者少也；二人惑则劳而不至，惑者胜也。而今也以天下惑，予虽有祈向，不可得也。不亦悲乎！大声不入于里耳，折杨、皇华，则嗑然而笑。是故高言不止于众人之心；至言不出，俗言胜也。以二缶钟惑，而所适不得矣。而今也以天下惑，予虽有祈向，其庸可得邪！知其不可得也而强之，又一惑也！故莫若释之而不推。不推，谁其比忧！厉之人，夜半生其子，遽取火而视之，汲汲然唯恐其似己也。

百年之木，破为牺尊，青黄而文之，其断在沟中，比牺尊于沟中之断，则美恶有间矣，其于失性一也。跖与曾、史，行义有间矣，然其失性均也。且夫失性有五：一曰无色乱目，使目不明；二曰五声乱耳，使耳不聪；三曰五臭熏鼻，困肿中颡；四曰五味浊口，使口厉爽；五曰趣舍滑心，使性飞扬。此五者，皆生之害也。而杨、墨乃始离岐自以为得，非吾所谓得也。夫得者困，可以为得乎？则鸠枭之在于笼也，亦可以为得矣。且夫趣舍声色以柴其内，皮弁鹬冠，缙笏绅修，以约其外。内支盈于柴栅，外重墨缴，皖皖然在墨缴之中，而自以为得，则是罪人交臂历指，而虎豹在于囊槛，亦可以为得矣！

天道第十三
-----

天道运而无所积，故万物成；帝道运而无所积，故天下归；圣道运而无所积，故海内服。明于天，通于圣，六通四辟于帝王之德者，其自为也，昧然无不静者矣！圣人之静也，非曰静也善，故静也。万物无足以铙心者，故静也。水静则明烛须眉，平中准，大匠取法焉。水静犹明，而况精神圣人之心静乎！天地之鉴也，万物之镜也。夫虚静恬淡寂漠无为者，天地之平而道德之至，故帝王圣人休焉。休则虚，虚则实，实者伦矣。虚则静，静则动，动则得矣。静则无为，无为也，则任事者责矣。无为则俞俞。俞俞者，忧患不能处，年寿长矣。

夫虚静恬淡寂漠无为者，万物之本也。明此以南向，尧之为君也；明此以北面，舜之为臣也。以此处上，帝王天子之德也；以此处下，玄圣素王之道也。以此退居而闲游，江海山林之士服；以此进为而抚世，则功大名显而天下一也。静而圣，动而王，无为也而尊，朴素而天下莫能与之争美。夫明白于天地之德者，此之谓大本大宗，与天和者也。所以均调天下，与人和者也。与人和者，谓之人乐；与天和者，谓之天乐。庄子曰：“吾师乎，吾师乎！齑万物而不为戾；泽及万世而不为仁；长于上古而不为寿；覆载天地、刻雕众形而不为巧。”此之谓天乐。故曰：知天乐者，其生也天行，其死也物化。静而与阴同德，动而与阳同波。故知天乐者，无天怨，无人非，无物累，无鬼责。故曰：其动也天，其静也地，一心定而王天下；其鬼不祟，其魂不疲，一心定而万物服。言以虚静推于天地，通于万物，此之谓天乐。天乐者，圣人之心以畜天下也。

夫帝王之德，以天地为宗，以道德为主，以无为为常。无为也，则用天下而有余；有为也，则为天下用而不足。故古之人贵夫无为也。上无为也，下亦无为也，是下与上同德。下与上同德则不臣。下有为也，上亦有为也，是上与下同道。上与下同道则不主。上必无为而用天下，下必有为为天下用。此不易之道也。故古之王天下者，知虽落天地，不自虑也；辩虽凋万物，不自说也；能虽穷海内，不自为也。天不产而万物化，地不长而万物育，帝王无为而天下功成。故曰：莫神于天，莫富于地，莫大于帝王。故曰：帝王之德配天地。此乘天地驰万物而用人群之道也。

本在于上，末在于下；要在于主，详在于臣，三军五兵之运，德之末也；赏罚利害，五刑之辟，教之末也；礼法度数，形名比详，治之末也；钟鼓之音，羽旄之容，乐之末也；哭泣衰垤，隆杀之服，哀之末也。此五末者，须精神之运，心术之动，然后从之者也。末学者，古人有之，而非所以先也。君先而臣从，父先而子从，兄先而弟从，长先而少从，男先而女从，夫先而妇从。夫尊卑先后，天地之行也，故圣人取象焉。天尊地卑，神明之位也；春夏先，秋冬后，四时之序也；万物化作，萌区有状，盛衰之杀，变化之流也。夫天地至神，而有尊卑先后之序，而况人道乎！宗庙尚亲，朝廷尚尊，乡党尚齿，行事尚贤，大道之序也。语道而非其序者，非其道也。语道而非其道也，安取道。

是故古之明大道者，先明天而道德次之，道德已明而仁义次之，仁义已明而分守次之。分守已明而形名次之，形名已明而因任次之，因任已明而原省次之，原省已明而是非次之，是非已明而赏罚次之，赏罚已明而愚知处宜，贵贱履位，仁贤不肖袭情。必分其能，必由其名，以此事上，以此畜下，以此治物，以此修身，知谋不用，必归其天。此之谓大平，治之至也。故书曰：“有形有名。”形名者，古人有之，而非所以先也。古之语大道者，五变而形名可举，九变而赏罚可言也。骤而语形名，不知其本也；骤而语赏罚，不知其始也。倒道而言，忤道而说者，人之所治也，安能治人！骤而语形名赏罚，此有知治之具，非知治之道。可用于天下，不足以用天下。此之谓辩士，一曲之人也。礼法数度，形名比详，古人有之，此下之所以事上，非上之所以畜下也。

昔者舜问于尧曰：“天王之用心何如？”尧曰：“吾不敖无告，不废穷民，苦死者，嘉孺子而哀妇人，此吾所以用心也。”舜曰：“美则美矣，而未大也。”尧曰：“然则何如？”舜曰：“天德而出宁，日月照而四时行，若昼夜之有经，云行而雨施矣！”尧曰：“胶胶扰扰乎！子，天之合也；我，人之合也。”夫天地者，古之所大也，而黄帝、尧、舜之所共美也。故古之王天下者，奚为哉？天地而已矣！

孔子西藏书于周室，子路谋曰：“由闻周之征藏史有老聃者，免而归居，父子欲藏书，则试往因焉。”孔子曰：“善。”往见老聃，而老聃不许，于是翻十二经以说。老聃中其说，曰：“大谩，愿闻其要。”孔子曰：“要在仁义。”老聃曰：“请问：仁义，人之性邪？”孔子曰：“然，君子不仁则不成，不义则不生。仁义真人之性也，又将奚为矣？”老聃曰：“请问：何谓仁义？”孔子曰：“中心物岂，兼爱无私，此仁义之情也。”老聃曰：“意，几乎后言夫兼爱，不亦迂乎！无私焉，乃私也。夫子若欲使天下无失其牧乎？则天地固有常矣，日月固有明矣，星辰固有列矣，禽兽固有群矣，树木固有立矣。夫子亦放德而行，循道而趋，已至矣！又何偈偈乎揭仁义，若击鼓而求亡子焉！意，夫子乱人之性也。”

士成绮见老子而问曰：“吾闻夫子圣人也。吾固不辞远道而来，愿见，百余重研而不敢息。今吾观子非圣人也，鼠壤有余蔬，而弃妹之者，不仁也！生熟不尽于前，而积敛无崖。”老子漠然不应。士成绮明日复见，曰：“昔者吾有刺于子，今吾心正隙矣，何故也？”老子曰：“夫巧知神圣之人，吾自以为脱焉。昔者子呼我牛也而谓之牛；呼我马也而谓之马。苟有其实，人与之名而弗受，再受其殃，吾服也恒服，吾非以服有服。”士成绮雁行避影，履行遂进，而问修身苦何。老子曰：“而容崖然，而目冲然，而颡颡然，而口阚然，而状义然。似系马而止也，动而持，发而机，察而审，知巧而睹于泰，凡以为不信边竟有人焉，其名为窃。”

夫子曰：“夫道，于大不终，于小不遗，故万物备。广广乎其无不容也，渊乎其不可测也。形德仁义，神之末也，非至人孰能定之！夫至人有世，不亦大乎，而不足以为之累；天下奋栋而不与之偕；审乎无假而不与利迁；极物之真，能守其本。故外天地，遗万物，而神未尝有所困也。通乎道，合乎德，退仁义，宾礼乐，至人之心有所定矣！”

世之所贵道者，书也。书不过语，语有贵也。语之所贵者，意也，意有所随。意之所随者，不可以言传也，而世因贵言传书。世虽贵之我犹不足贵也，为其贵非其贵也。故视而可见者，形与色也；听而可闻者，名与声也。悲夫！世人以形色名声为足以得彼之情。夫形色名声，果不足以德彼之情，则知者不言，言者不知，而世岂知之哉！桓公读书于堂上，轮扁斫轮于堂下，释椎凿而上，问桓公曰：“敢问公之所读者，何言邪？”公曰：“圣人之言也。”曰：“圣人在乎？”公曰：“已死矣。”曰：“然则君之所读者，古人之糟魄已矣！”桓公曰：“寡人读书，轮人安得议乎！有说则可，无说则死！”轮扁曰：“臣也以臣之事观之。斫轮，徐则甘而不固，疾则苦而不入，不徐不疾，得之于手而应于心，口不能言，有数存焉于其间。臣不能以喻臣之子，臣之子亦不能受之于臣，是以行年七十而老斫轮。古之人与其不可传也死矣，然则君之所读者，古人之糟魄已夫！”

天运第十四
-----

“天其运乎？地其外乎？日月其争于所乎？孰主张是？孰纲维是？孰居无事推而行是？意者其有机缄而不得已邪？意者其运转而不能自止邪？云者为雨乎？雨者为云乎？孰隆施是？孰居无事淫乐而劝是？风起北方，一西一东，有上彷徨。孰嘘吸是？孰居无事而披拂是？敢问何故？”巫咸召曰：“来，吾语女。天有六极五常，帝王顺之则治，逆之则凶。九洛之事，治成德备，监照下土，天下戴之，此谓上皇。”

商太宰荡问仁于庄子。庄子曰：“虎狼，仁也。”曰：“何谓也？”庄子曰：“夫子相亲，何为不仁！”曰：“请问至仁。”庄子曰：“至仁无亲。”太宰曰：“荡闻之，无亲则不爱，不爱则不孝。谓至仁不孝，可乎？”庄子曰：“不然，夫至仁尚矣，孝固不足以言之。此非过孝之言也，不及孝之言也。夫南行者至于郢，北面而不见冥山，是何也？则去之远也。故曰：以敬孝易，以爱孝难；以爱孝易，以忘亲难；忘亲易，使亲忘我难；使亲忘我易，兼忘天下难；兼忘天下易，使天下兼忘我难。夫德遗尧、舜而不为也，利泽施于万世，天下莫知也，岂直太息而言仁孝乎哉！夫孝悌仁义，忠信贞廉，此皆自勉以役其德者也，不足多也。故曰：至贵，国爵并焉；至富，国财并焉；至愿，名誉并焉。是以道不渝。”

北门成问于黄帝曰：“帝张咸池之乐于洞庭之野，吾始闻之惧，复闻之怠，卒闻之而惑，荡荡默默，乃不自得。”帝曰：“汝殆其然哉！吾奏之以人，徽之以天，行之以礼义，建之以太清。夫至乐者，先应之以人事，顺之以天理，行之以五德，应之以自然，然后调理四时，太和万物。四时迭起，万物循生。一盛一衰，文武伦经。一清一浊，阴阳调和，流光其声，蛰虫始作，吾惊之以雷霆。其卒无尾，其始无首。一死一生，一愤一起，所常无穷，而一不可待。汝故惧也。吾又奏之以阴阳之和，烛之以日月之明。其声能短能长，能柔能刚，变化齐一，不主故常。在谷满谷，在坑满坑。途隙守神，以物为量。其声挥绰，其名高明。是故鬼神守其幽，日月星辰行其纪。吾止之于有穷，流之于无止。予欲虑之而不能知也，望之而不能见也，逐之而不能及也。傥然立于四虚之道，倚于槁梧而吟：‘目知穷乎所欲见，力屈乎所欲逐，吾既不及，已夫！’形充空虚，乃至委蛇。汝委蛇，故怠。吾又奏之以无怠之声，调之以自然之命。故若混逐丛生，林乐而无形，布挥而不曳，幽昏而无声。动于无方，居于窈冥，或谓之死，或谓之生；或谓之实，或谓之荣。行流散徙，不主常声。世疑之，稽于圣人。圣也者，达于情而遂于命也。天机不张而五官皆备。此之谓天乐，无言而心悦。故有炎氏为之颂曰：‘听之不闻其声，视之不见其形，充满天地，苞裹六极。’汝欲听之而无接焉，而故惑也。乐也者，始于惧，惧故祟；吾又次之以怠，怠故遁；卒之以惑，惑故愚；愚故道，道可载而与之俱也。”

孔子西游于卫，颜渊问师金曰：“以夫子之行为奚如？”师金曰：“惜乎！而夫子其穷哉！”颜渊曰：“何也？”师金曰：“夫刍狗之未陈也，盛以荚衍，巾以文绣，尸祝齐戒以将之。及其已陈也，行者践其首脊，苏者取而鑫之。而已将复取而盛以荚衍，巾以文绣，游居寝卧其下，彼不得梦，必且数眯焉。今而夫子亦取先王已陈刍狗，聚弟子游居寝卧其下。故伐树于宋，削迹于卫，穷于商周，是非其梦邪？围于陈蔡之间，七日不火食，死生相与邻，是非其眯邪？夫水行莫如用舟，而陆行莫如用车。以舟之可行于水也，而求推之于陆，则没世不行寻常。古今非水陆与？周鲁非舟车与？今蕲行周于鲁，是犹推舟于陆也！劳而无功，身必有殃。彼未知夫无方之传，应物而不穷者也。且子独不见夫桔槔者乎？引之则俯，舍之则仰。彼，人之所引，非引人也。故俯仰而不得罪于人。故夫三皇五帝之礼义法度，不矜于同而矜于治。故譬三皇五帝之礼义法度，其犹诅梨橘柚邪！其味相反而皆可于口。故礼义法度者，应时而变者也。今取猿狙而衣以周公之服，彼必啮啮挽裂，尽去而后谦。观古今之异，犹猿狙之异乎周公也。故西施病心而颦其里，其里之丑人见之而美之，归亦捧心而颦其里。其里之富人见之，坚闭门而不出；贫人见之，挈妻子而去之走。彼知颦美，而不知颦之所以美。惜乎，而夫子其穷哉！”

```
孔子行年五十有一而不闻道，乃南之沛见老聃。老聃曰：“子来乎？吾闻子，北方之贤者也！子亦得道乎？”孔子曰：“未得也。”老子曰：“子恶乎求之哉？”曰：“吾求之于度数，五年而未得也。”老子曰：“子又恶乎求之哉？”曰：“吾求之于阴阳，十有二年而未得。”老子曰：“然，使道而可献，则人莫不献之于其君；使道而可进，则人莫不进之于其亲；使道而可以告人，则人莫不告其兄弟；使道而可以与人，则人莫不与其子孙。然而不可者，无它也，中无主而不止，外无正而不行。由中出者，不受于外，圣人不出；由外入者，无主于中，圣人不隐。名，公器也，不可多取。仁义，先王之遽庐也，止可以一宿而不可以久处。逗而多责。古之至人，假道于仁，托宿于义，以游逍遥之墟，食于苟简之田，立于不贷之圃。逍遥，无为也；苟简，易养也；不贷，无出也。古者谓是采真之游。以富为是者，不能让禄；以显为是者，不能让名。亲权者，不能与人柄，操之则栗，舍之则悲，而一无私鉴，以窥其所不休者，是天之戮民也。怨、恩、取、与、谏、教、生、杀八者，正之器也，唯循大变无私湮者为能用之。故曰：正者，正也。其心以为不然者，天门弗开矣。”

孔子见老聃而语仁义。老聃曰：“夫播糠眯目，则天地四方易位矣，蚊虻啮肤，则通昔不寐矣。夫仁义瓒然，乃愤吾心，乱莫大焉。吾子使天下无失其朴，吾子亦放风而动，总德而立矣！又奚杰然若负建鼓而求亡子者邪？夫鹄不日浴而白，乌不日黔而黑。黑白之朴，不足以为辩；名誉之观，不足以为广。泉涸，鱼相与处于陆，相吻以湿，相濡以沫，不若相忘于江湖。”

孔子见老聃，三日不谈。弟子问曰：“夫子见老聃，亦将何规哉？”孔子曰：“吾乃今于是乎见龙。龙，合而成体，散而成章，乘云气而养乎阴阳，予口张而不能协。予又何规老聃哉？”子贡曰：“然则人固有尸居而龙见，雷声而渊默，发动如天地者乎？赐亦可得而观乎？”遂以孔子声见老聃。老聃方将倨堂应，微曰：“予年运而往矣，子将何以戒我乎？”子贡曰：“夫三王五帝之治天下不同，其系声名一也，而先生独以为非圣人，如何哉？”老聃曰：“小子少进！予何以谓不同？”对曰：“尧授舜，舜授禹。禹用力而汤用兵，文王顺纣而不敢逆，武王逆纣而不肯顺，故曰不同。”老聃曰：“小子少进，余语汝三皇五帝之治天下：黄帝之治天下，使民心一。民有其亲死不哭而民不非也。尧之治天下，使民心亲。民有为其亲杀其杀而民不非也。舜之治天下，使民心竞。民孕妇十月生子，子生五月而能言，不至乎孩而始谁，则人始有夭矣。禹之治天下，使民心变，人有心而兵有顺，杀盗非杀人。自为种而天下耳。是以天下大骇，儒墨皆起。其作始有伦，而今乎妇女，何言哉！余语汝：三皇五帝之治天下，名曰治之，而乱莫甚焉。三皇之知，上悖日月之明，下睽山川之精，中堕四时之施。其知瓒于历万之尾，鲜规之兽，莫得安其性命之情者，而犹自以为圣人，不可耻乎？其无耻也！”子贡蹴蹴然立不安。

孔子谓老聃曰：“丘治《诗》、《书》、《礼》、《乐》、《易》、《春秋》六经，自以为久矣，孰知其故矣，以奸者七十二君，论先王之道而明周、召之迹，一君无所钩用。甚矣！夫人之难说也？道之难明邪？”老子曰：“幸矣，子之不遇治世之君也！夫六经，先王之陈迹也，岂其所以迹哉！今子之所言，犹迹也。夫迹，履之所出，而迹岂履哉！夫白猊之相视，眸子不运而风化；虫，雄鸣于上风，雌应于下风而风化。类自为雌雄，故风化。性不可易，命不可变，时不可止，道不可壅。苟得于道，无自而不可；失焉者，无自而可。”孔子不出三月，复见，曰：“丘得之矣。乌鹊孺，鱼传沫，细要者化，有弟而兄啼。久矣，夫丘不与化为人！不与化为人，安能化人。”老子曰：“可，丘得之矣！”

```

刻意 第十五
------

刻意尚行，离世异俗，高论怨诽，为亢而已矣。此山谷之士，非世之人，枯槁赴渊者之所好也。语仁义忠信，恭俭推让，为修而已矣。此平世之士，教诲之人，游居学者之所好也。语大功，立大名，礼君臣，正上下，为治而已矣。此朝廷之士，尊主强国之人，致功并兼者之所好也。就薮渊，处闲旷，钓鱼闲处，无为而已矣。此江海之士，避世之人，闲暇者之所好也。吹煦呼吸，吐故纳新，熊经鸟申，为寿而已矣。此导引之士，养形之人，彭祖寿考者之所好也。若夫不刻意而高，无仁义而修，无功名而治，无江海而闾，不导引而寿，无不忘也，无不有也。淡然无极，而众美从之，此天地之道，圣人之德也。

```
故曰：夫恬淡寂漠，虚无无为，此天地之平，而道德之质也。故曰：圣人休，休焉则平易矣。平易则恬淡矣。平易恬淡，则忧患不能入，邪气不能袭，故其德全而神不亏。故曰：圣人之生也天行，其死也物化。静而与阴同德，动而与阳同波。不为福先，不为祸始。感而后应，迫而后动，不得已而后起。去知与故，循天之理。故无天灾，无物累，无人非，无鬼责。其生若浮，其死若休。不思虑，不豫谋。光矣而不耀，信矣而不期。其寝不梦，其觉无忧。其神纯粹，其魂不罢。虚无恬淡，乃合天德。故曰：悲乐者，德之邪也；喜怒者，道之过也；好恶者，德之失也。故心不忧乐，德之至也；一而不变，静之至也；无所于忤，虚之至也；不与物交，淡之至也；无所于逆，粹之至也。故曰：形劳而不休则弊，精用而不已则劳，劳则竭。水之性，不杂则清，莫动则平；郁闭而不流，亦不能清；天德之象也。故曰：纯粹而不杂，静一而不变，淡而无为，动而以天行，此养神之道也。

夫有干越之剑者，押而藏之，不敢用也，宝之至也。精神四达并流，无所不极，上际于天，下蟠于地，化育万物，不可为象，其名为同帝。纯素之道，唯神是守。守而勿失，与神为一。一之精通，合于天伦。野语有之曰：“众人重利，廉士重名，贤士尚志，圣人贵精。”故素也者，谓其无所与杂也；纯也者，谓其不亏其神也。能体纯素，谓之真人。

缮性第十六

缮性于俗俗学，以求复其初；滑欲于俗思，以求致其明；谓之蔽蒙之民。古之治道者，以恬养知。知生而无以知为也，谓之以知养恬。知与恬交相养，而和理出其性。夫德，和也；道，理也。德无不容，仁也；道无不理，义也；义明而物亲，忠也；中纯实而反乎情，乐也；信行容体而顺乎文，礼也。礼乐偏行，则天下乱矣。彼正而蒙己德，德则不冒。冒则物必失其性也。古之人，在混芒之中，与一世而得淡漠焉。当是时也，阴阳和静，鬼神不扰，四时得节，万物不伤，群生不夭，人虽有知，无所用之，此之谓至一。当是时也，莫之为而常自然。

逮德下衰，乃燧人、伏羲始为天下，是故顺而不一，德又下衰，及神农、黄帝始为天下，是故安而不顺。德又下衰，及唐、虞始为天下，兴治化之流，泄淳散朴。离道以善，险德以行，然后去性而从于心。心与心识，知而不足以定天下，然后附之以文，益之以博。文灭质，博溺心，然后民始惑乱，无以反其性情而复其初。由是观之，世丧道矣，道丧世矣，世与道交相丧也。道之人何由兴乎世，世亦何由兴乎道哉？道无以兴乎世，世无以兴乎道，虽圣人不在山林之中，其德隐矣。隐故不自隐。古之所谓隐士者，非伏其身而弗见也，非闭其言而不出也，非藏其知而不发也，时命大谬也。当时命而大行乎天下，则反一无迹；不当时命而大穷乎天下，则深根宁极而待：此存身之道也。古之行身者，不以辩饰知，不以知穷天下，不以知穷德，危然处其所而反其性已，又何为哉？道固不小行，德固不小识。小识伤德，小行伤道。故曰：正己而已矣。乐全之谓得志。

古之所谓得志者，非轩冕之谓也，谓其无以益其乐而已矣。今之所谓得志者，轩冕之谓也。轩冕在身，非性命也，物之傥来，寄者也。寄之，其来不可圉，其去不可止。故不为性命肆志，不为穷约趋俗，其乐彼与此同，故无忧而已矣！今寄去则不乐。由之观之，虽乐，未尝不荒也。故曰：丧己于物，失性于俗者，谓之倒置之民。

```

秋水第十七

```
秋水时至，百川灌河。泾流之大，两泗渚崖之间，不辩牛马。于是焉河伯欣然自喜，以天下之美为尽在己。顺流而东行，至于北海，东面而视，不见水端。于是焉河伯始旋其面目，望洋向若而叹曰：“野语有之曰：闻道百，以为莫己若者。我之谓也。且夫我尝闻少仲尼之闻而轻伯夷之义者，始吾弗信。今我睹子之难穷也，吾非至于子之门则殆矣，吾长见笑于大方之家。”

北海若曰：“井蛙不可以语于海者，拘于虚也；夏虫不可以语于冰者，笃于时也；曲士不可以语于道者，束于教也。今尔出于崖泗，观于大海，乃知尔丑，尔将可与语大理矣。天下之水，莫大于海：万川归之，不知何时止而不盈；尾闾泄之，不知何时已而不虚；春秋不变，水旱不知。此其过江河之流，不可为量数。而吾未尝以此自多者，自以比形于天地，而受气于阴阳，吾在于天地之间，犹小石小木之在大山也。方存乎见少，又奚以子多！计四海之在天地之间也，不似垒空之在大泽乎？计中国之在海内，不似睇米之在大仓乎？号物之数谓之万，人处一焉；人卒九州谷食之所生，舟车之所通，人处一焉。此其比万物也，不似豪末之在于马体乎？五帝之所连，三王之所争，仁人之所忧，任士之所劳，尽此矣！伯夷辞之以为多，仲尼语之以为博。此其自多也，不似尔向之自多于水乎？”

河伯曰：“然则吾大天地而小毫末，可乎？”北海若曰：“否。夫物，量无穷，时无止，分无常，终始无故。是故大知观于远近，故小而不寡，大而不多：知量无穷。证向今故，故遥而不闷，掇而不岐：知时无止。察乎盈虚，故得而不喜，失而不忧：知分之无常也。明乎坦途，故生而不悦，死而不祸：知终始之不可故也。计人之所知，不若其所不知；其生之时，不若未生之时；以其至小，求穷其至大之域，是故迷乱而不能自得也。由此观之，又何以知毫末之足以定至细之倪，又何以知天地之足以穷至大之域！”

河伯曰：“世之议者皆曰：至情无形，至大不可围。是信情乎？”北海若曰：“夫自细视大者不尽，自大视细者不明。失精，小之微也；俘，大之殷也：故异便。此势之有也。夫精粗者，期于有形者也；无形者，数之所不能分也；不可围者，数之所不能穷也。可以言论者，物之粗也；可以意致者，物之精也；言之所不能论，议之所不能察致者，不期精粗焉。是故大人之行：不出乎害人，不多仁恩；动不为利，不贱门隶；货财弗争，不多辞让；事焉不借人，不多食乎力，不贱贪污；行殊乎俗，不多辟异；为在从众，不贱佞谄；世之爵禄不足以为劝，戮耻不足以为辱；知是非之不可为分，细大之不可为倪。闻曰：道人不闻，至德不得。大人无己。约分之至也。”

河伯曰：“若物之外，若物之内，恶至而倪贵贱？恶至而倪小大？”北海若曰：“以道观之，物无贵贱；以物观之，自贵而相贱；以俗观之，贵贱不在己。以差观之，因其所大而大之，则万物莫不大；因其所小而小之，则万物莫不小。知天地之为绨米也，知毫末之为丘山也，则差数睹矣。以功观之，因其所有而有之，则万物莫不有；因其所无而无之，则万物莫不无。知东西之相反而不可以相无，则功分定矣。以趣观之。因其所然而然之，则万物莫不然；因其所非而非之，则万物莫不非。知尧、桀之自然而相非，则趣操睹矣。

“昔者尧、舜让而帝，之、哙让而绝；汤、武争而王，白公争而灭。由此观之，争让之礼，尧、桀之行，贵贱有时，未可以为常也。梁丽可以冲城而不可以窒穴，言殊器也；骐骥骅骝一日而驰千里，捕鼠不如狸猩，言殊技也；鸱枭夜撮蚤，察毫末，昼出瞠目而不见丘山，言殊性也。故曰：盖师是而无非，师治而无乱乎？是未明天地之理，万物之情者也。是犹师天而无地，师阴而无阳，其不可行明矣！然且语而不舍，非愚则诬也！帝王殊禅，三代殊继。差其时，逆其俗者，谓之篡天；当其时，顺其俗者，谓之义徒。默默乎河伯，女恶知贵贱之门，小大之家！”

河伯曰：“然则我何为乎？何不为乎？吾辞受趣舍，吾终奈何？”北海若曰：“以道观之，何贵何贱，是谓反衍；无拘而志，与道大蹇。何少何多，是谓谢施；无一而行，与道参差。严乎若国之有君，其无私德；繇繇乎若祭之有社，其无私福；泛泛乎其若四方之无穷，其无所畛域。兼怀万物，其孰承翼？是谓无方。万物一齐，孰短孰长？道无终始，物有死生，不恃其成。一虚一满，不位乎其形。年不可举，时不可止。消息盈虚，终则有始。是所以语大义之方，论万物之理也。物之生也，若骤若驰。无动而不变，无时而不移。何为乎，何不为乎？夫固将自化。”

河伯曰：“然则何贵乎道邪？”北海若曰；“知道者必达于理，达于理者必明于权，明于权者不以物害己。至德者，火弗能热，水弗能溺，寒暑弗能害，禽兽弗能贼。非谓其薄之也，言察乎安危，宁于祸福，谨于去就，莫之能害也。故曰：天在内，人在外，德在乎天。知天人之行，本乎天，位乎得，踯躅而屈伸，反要而语极。”曰：“何谓天？何谓人？”北海若曰：“牛马四足，是谓天；落马首，穿牛鼻，是谓人。故曰：无以人灭天，无以故灭命，无以得殉名。谨守而勿失，是谓反其真。”

夔怜铉，铉怜蛇，蛇怜风，风怜目，目怜心。夔谓铉曰：“吾以一足跳踯而行，予无如矣。今子之使万足，独奈何？”铉曰：“不然。子不见夫唾者乎？喷则大者如珠，小者如雾，杂而下者不可胜数也。今予动吾天机，而不知其所以然。”铉谓蛇曰：“吾以众足行，而不及子之无足，何也？”蛇曰：“夫天机之所动，何可易邪？吾安用足哉！”蛇谓风曰：“予动吾脊胁而行，则有似也。今子蓬蓬然起于北海，蓬蓬然入于南海，而似无有，何也？”风曰：“然，予蓬蓬然起于北海而入于南海也，然而指我则胜我，蝤我亦胜我。虽然夫折大木，蜚大屋者，唯我能也。”故以众小不胜为大胜也。为大胜者，唯圣人能之。

孔子游于匡，宋人围之，数匝，而弦歌不辍。子路入见，曰：“何夫子之娱也？”孔子曰：“来，吾语汝。我讳穷久矣，而不免，命也；求通久矣，而不得，时也。当尧、舜而天下无穷人，非知得也；当桀、纣而天下无通人，非知失也；时势适然。夫水行不避蛟龙者，渔父之勇也；陆行不避兕虎者，猎夫之勇也；白刃交于前，视死若生者，烈士之勇也；知穷之有命，知通之有时，临大难而不惧者，圣人之勇也。由，处矣！吾命有所制矣！”无几何，将甲者进，辞曰：“以为阳虎也，故围之；今非也，请辞而退。”

公孙龙问于魏牟曰：“龙少学先王之道，长而明仁义之行；合同异，离坚白；然不然，可不可；困百家之知，穷众口之辩；吾自以为至达已。今吾闻庄子之言，茫焉异之，不知论之不及与？知之弗若与？今吾无所开吾喙，敢问其方？”公子牟隐几太息，仰天而笑曰：“予独不闻夫坎井之蛙乎？谓东海之鳖曰：‘吾乐与！出跳梁乎井干之上，入休乎缺砖之崖。赴水则接腋持颐，蹶泥则没足灭俯。还干蟹与蝌蚪，莫吾能若也。且夫擅一壑之水，而跨恃坎井之乐，此亦至矣。夫子奚不时来入观乎？’东海之鳖左足未入，而右膝已絷矣。于是逡巡而隙，告之海曰：‘夫千里之远，不足以举其大；千仞之高，不足以极其深。禹之时，十年九潦，而水弗加益；汤之时，八年七旱，而崖不为加损。夫不为顷久推移，不以多少进退者，此亦东海之大乐也。’于是坎井之蛙闻之，适适然惊，规规然自失也。且夫知不知是非之竟，而犹欲观于庄子之言，是犹使蚊负山，商巨驰河也，必不胜任矣。且夫知不知论极妙之言，而自适一时之利者，是非坎井之蛙与？且彼方呲黄泉而等大皇，无南无北，爽然四解，沦于不测；无东无西，始于玄冥，反于大通。子乃规规然而求之以察，索之以辩，是直用管窥天，用锥指地也，不亦小乎？子往矣！且子独不闻夫寿陵余子之学行于邯郸与？未得国能，又失其故行矣，直匍匐而归耳。今子不去，将忘子之故，失子之业。”公孙龙口祛而不合，舌举而不下，乃逸而走。

庄子钓于濮水。楚王使大夫二人往先焉，曰：“愿以境内累矣！”庄子持竿不顾，曰：“吾闻楚有神龟，死已三千岁矣。王巾笥而藏之庙堂之上，此龟者，宁其死为留骨而贵乎？宁其生而曳尾于涂中乎？”二大夫曰：“宁生而曳尾涂中。”庄子曰：“往矣！吾将曳尾于涂中。”

惠子相梁，庄子往见之，或谓惠子曰：“庄子来，欲代子相。”于是惠子恐，搜于国中，三日三夜，庄子往见之，曰：“南方有鸟，其名鸳雏，子知之乎？夫鸳雏发于南海而飞于北海，非梧桐不止，非练实不食，非醴泉不饮。于是鸱得腐鼠，鸳雏过之，仰而视之曰：‘吓！’今子欲以子之梁国而吓我邪？”

庄子与惠子游于濠梁之上。庄子曰：“攸鱼出游从容，是鱼之乐也。”惠子曰：“子非鱼，安知鱼之乐？”庄子曰：“子非我，安知我不知鱼之乐？”惠子曰：“我非子，固不知子矣；子固非鱼也，子之不知鱼之乐，全矣！”庄子曰：“请循其本。子曰‘汝安知鱼之乐’云者，既已知吾知之而问我。我知之濠上也。”

```

至乐第十八

```
天下有至乐无有哉？有可以活身者无有哉？今奚为奚据？奚避奚处？奚就奚去？奚乐奚恶？夫天下之所尊者，富贵寿善也；所乐者，身安厚味美服好色音声也；所下者，贫贱夭恶也；所苦者，身不得安逸，口不得厚味，形不得美服，目不得好色，耳不得音声。若不得者，则大忧以惧，其为形也亦愚哉！夫富者，苦身疾作，多积财而不得尽用，其为形也亦外矣！夫贵者，夜以继日，思虑善否，其为形也亦疏矣！人之生也，与忧俱生。寿者昏昏，久忧不死，何苦也！其为形也亦远矣！烈士为天下见善矣，未足以活身；以为不善矣，足以活人。故曰：“忠谏不听，蹲循勿争。”故夫子胥争之，以残其形；不争，名亦不成。诚有善吾有哉？

今俗之所为与其所乐，吾又未知乐之果乐邪？果不乐邪？吾观夫俗之所乐，举群趣者，径径然如将不得已，而皆曰乐者，吾未之乐也，亦未之不乐也，果有乐无有哉？吾以无为诚乐矣，又俗之所大苦也。故曰：“至乐无乐，至誉无誉。”天下是非果未可定也。虽然，无为可以定是非。至乐活身，唯无为几存。请尝试言之：天无为以之清，地无为以之宁。故两无为相合，万物皆化。芒乎忽乎，而无从出乎！忽乎芒乎，而无要象乎！万物职职，皆从无为殖。故曰：“天地无为也而无不为也。”人也孰能得无为哉！

庄子妻死，惠子吊之，庄子则方箕踞鼓盆而歌。惠子曰：“与人居，长子、老、身死，不哭亦足矣，又鼓盆而歌，不亦甚乎！”庄子曰：“不然。是其始死也，我独何能无慨然！察其始而本无生；非徒无生也，而本无形；非徒无形也，而本无气。杂乎芒忽之间，变而有气，气变而有形，形变而有生。今又变而之死。是相与为春秋冬夏四时行也。人且偃然寝于巨室，而我嗷嗷然随而哭之，自以为不通乎命，故止也。”

庄子之楚，见空骷髅，哓然有形。徼以马捶，因而问之，曰：“夫子贪生失理而为此乎？将子有亡国之事、斧钺之诛而为此乎？将子有不善之行，愧遗父母妻子之丑而为此乎？将子有冻馁之患而为此乎？将子之春秋故及此乎？”于是语卒，援骷髅，枕而卧。夜半，骷髅见梦曰：“子之谈者似辩士，视子所言，皆生人之累也，死则无此矣。子欲闻死之说乎？”庄子曰：“然。”骷髅曰：“死，无君于上，无臣于下，亦无四时之事，从然以天地为春秋，虽南面王乐，不能过也。”庄子不信，曰：“吾使司命复生子形，为子骨肉肌肤，反子父母、妻子、闾里、知识，子欲之乎？”骷髅深颦蹙颡曰：“吾安能弃南面王乐，而复为人间之劳乎？”

颜渊东之齐，孔子有忧色。子贡下席而问曰：“小子敢问：回东之齐，夫子有忧色，何邪？”孔子曰：“善哉汝问。昔者管子有言，丘甚善之，曰：‘褚小者不可以怀大，绠短者不可以汲深。’夫若是者，以为命有所成而形有所适也，夫不可损益。吾恐回与齐侯言尧、舜、黄帝之道，而重以燧人、神农之言。彼将内求于己而不得，不得则惑，人惑则死。且汝独不闻邪？昔者海鸟止于鲁郊，鲁侯御而觞之于庙，奏《九韶》以为乐，具太牢以为膳。鸟乃眩视忧悲，不敢食一脔，不敢饮一杯，三日而死。此以己养养鸟也，非以鸟养养鸟也。夫以鸟养养鸟者，宜栖之深林，游之坛陆，浮之江湖，食之鳅攸，随行列而止，委迤而处。彼唯人言之恶闻，奚以夫哓哓为乎！咸池九韶之乐，张之洞庭之野，鸟闻之而飞，兽闻之而走，鱼闻之而下入，人卒闻之，相与还而观之。鱼处水而生，人处水而死。彼必相与异其好恶，故异也。故先圣不一其能，不同其事。名止于实，义设于适，是之谓条达而福持。”

列子行食于道从，见百岁骷髅，攘蓬而指之曰：“唯予与汝，知而未尝死、未尝生也。汝果养乎？予果欢乎？”种有几，得水则为绝，得水土之际，死为蛙嫔之衣，生于陵屯，则为陵泻，陵泻得郁栖则为乌足，乌足之根为挤螬，其叶为蝴蝶。蝴蝶胥也，化而为虫，生于灶下，其状若脱，其名为煦掇。煦掇千日为鸟，其名为乾余骨。乾余骨之沫为斯弥，斯弥为食醢。颐辂生乎食醢，黄祝生乎九猷，瞀芮生乎腐螺，羊奚比乎不荀，久竹生青宁，青宁生程，程生马，马生人，人又反入于机。万物皆出于机，皆入于机。

```

达生第十九

```
达生之情者，不务生之所外以为；达命之情者，不务知之所无奈何。养形必先之以物，物有余而形不养者有之矣。有生必先无离形，形不离而生亡者有之矣。生之来不能却，其去不能止。悲夫！世之人以为养形足以存生，而养形果不足以存生，则世奚足为哉！虽不足为而不可不为者，其为不免矣！夫欲免为形者，莫如弃世。弃世则无累，无累则正平，正平则与彼更生，更生则几矣！事奚足弃而生奚足遗？弃事则形不劳，遗生则精不亏。夫形全精复，与天为一。天地者，万物之父母也。合则成体，散则成始。形精不亏，是谓能移。精而又精，反以相天。

子列子问关尹曰：“至人潜行不窒，蹈火不热，行乎万物之上而不栗。请问何以至于此？”关尹曰：“是纯气之守也，非知巧果敢之列。居，予语女。凡有貌象声色者，皆物也，物与物何以相远！夫奚足以至乎先！是色而已。则物之造乎不形，而止乎无所化。夫得是而穷之者，物焉得而止焉！彼将处乎不淫之度，而藏乎无端之纪，游乎万物之所终始。壹其性，养其气，合其德，以通乎物之所造。夫若是者，其天守全，其神无隙，物奚自入焉！夫醉者之坠车，虽疾不死。骨节与人同而犯害与人异，其神全也。乘亦不知也，坠亦不知也，死生惊惧不入乎其胸中，是故逆物而不习。彼得全于酒而犹若是，而况得全于天乎？圣人藏于天，故莫之能伤也。复仇者，不折镆干；虽有歧心者，不怨飘瓦，是以天下平均。故无攻战之乱，无杀戮之刑者。由此道也。不开人之天，而开天之天，开天者德生，开人者贼生。不厌其天，不忽于人，民几乎以其真。”

仲尼适楚，出于林中，见佝偻者承蜩，犹掇之也。仲尼曰：“子巧乎，有道邪？”曰：“我有道也。五六月累丸二而不坠，则失者锱铢；累三而不坠，则失者十一；累五而不坠，犹掇之也。吾处身也，若橛株拘；吾执臂也，若槁木之枝。虽天地之大，万物之多，而唯蜩翼之知。吾不反不侧，不以万物易蜩之翼，何为而不得！”孔子顾谓弟子曰：“用志不分，乃凝于神。其佝偻丈人之谓乎！”

颜渊问仲尼曰：“吾尝济乎觞深之渊，津人操舟若神。吾问焉曰：‘操舟可学邪？’曰：‘可。善游者数能。若乃夫没人，则未尝见舟而便操之也。’吾问焉而不吾告，敢问何谓也？”仲尼曰：“善游者数能，忘水也；若乃夫没人之未尝见舟而便操之也，彼视渊若陵，视舟之覆，犹其车却也。覆却万方陈乎前而不得入其舍，恶往而不暇！以瓦注者巧，以钩注者惮，以黄金注者昏。其巧一也，而有所矜，则重外也。凡外重者内拙。”

田开之见周威公，威公曰：“吾闻祝肾学生，吾子与祝肾游，亦何闻焉？”田开之曰：“开之操拔彗以侍门庭，亦何闻于夫子！”威公曰：“田子无让，寡人愿闻之。”开之曰：“闻之夫子曰：‘善养生者，若牧羊然，视其后者而鞭之。’”威公曰：“何谓也？”田开之曰：“鲁有单豹者，岩居而水饮，不与民共利，行年七十而犹有婴儿之色，不幸遇饿虎，饿虎杀而食之，有张毅者，高门县薄，无不走也，行年四十而有内热之病以死。豹养其内而虎食其外，毅养其外而病攻其内。此二子者，皆不鞭其后者也。”仲尼曰：“无入而藏，无出而阳，柴立其中央。三者若得，其名必极。夫畏涂者，十杀一人则父子兄弟相戒也，必盛卒徒而后敢出焉，不亦知乎！人之所取畏者，衽席之上，饮食之间，而不知为之戒者，过也！”

祝宗人玄端以临牢荚说彘，曰：“汝奚恶死！吾将三月豢汝，十日戒，三日齐，藉白茅，加汝肩尻乎雕俎之上，则汝为之乎？”为彘谋曰：“不如食以糠糟而错之牢荚之中。”自为谋，则苟生有轩冕之尊，死得于喙遁之上，聚偻之中，则为之。为彘谋则去之，自为谋则取之，所异彘者何也！

桓公田于泽，管仲御，见鬼焉。公抚管仲之手曰：“仲父何见？”对曰：“臣无所见。”公反，埃殆为病，数日不出。齐士有皇子告敖者，曰：“公则自伤，鬼恶能伤公！夫忿畜之气，散而不反，则为不足；上而不下，则使人善怒；下而不上，则使人善忘；不上不下，中身当心，则为病。”桓公曰：“然则有鬼乎？”曰：“有。沈有履。灶有髻。户内之烦壤，雷霆处之；东北方之下者，倍阿蛙蛰跃之；西北方之下者，则跌阳处之。水有罔象，丘有辛，山有夔，野有彷徨，泽有委蛇。”公曰：“请问委蛇之状何如？”皇子曰：“委蛇，其大如彀，其长如辕，紫衣而朱冠。其为物也恶，闻雷车之声则捧其首而立。见之者殆乎霸。”桓公振然而笑曰：“此寡人之所见者也。”于是正衣冠与之坐，不终日而不知病之去也。

纪省子为王养斗鸡。十日而问：“鸡已乎？”曰：“未也，方虚矫而恃气。”十日又问，曰：“未也，犹应向景。”十日又问，曰：“未也，犹疾视而盛气。”十日又问，曰：“几矣，鸡虽有鸣者，已无变矣，望之似木鸡矣，其德全矣。异鸡无敢应者，反走矣。”

孔子观于吕梁，县水三十仞，流沫四十里，鼋鼍鱼鳖之所不能游也。见一丈夫游之，以为有苦而欲死也。使弟子并流而拯之。数百步而出，被发行歌而游于塘下。孔子从而问焉，曰：“吾以子为鬼，察子则人也。请问：蹈水有道乎？”曰：“亡，吾无道。吾始乎故，长乎性，成乎命。与齐俱入，与汩偕出，从水之道而不为私焉。此吾所以蹈之也。”孔子曰：“何谓始乎故，长乎性，成乎命？”曰：“吾生于陵而安于陵，故也；长于水而安于水，性也；不知吾所以然而然，命也。”

梓庆削木为锯，锯成，见者惊犹鬼神。鲁侯见而问焉，曰：“子何术以为焉？”对曰：“臣，工人，何术之有！虽然，有一焉：臣将为锯，未尝敢以耗气也，必齐以静心。齐三日，而不敢怀庆赏爵禄；齐五日，不敢怀非誉巧拙；齐七日，辄然忘吾有四肢形体也。当是时也，无公朝，其巧专而外骨消，然后入山林，观天性形躯，至矣，然后成见锯，然后加手焉，不然则已。则以天合天，器之所以疑神者，其是与！”

东野稷以御见庄公，进退中绳，左右旋中规。庄公以为文弗过也。使之钩百而反。颜阖遇之，入见曰：“稷之马将败。”公密而不应。少焉，果败而反。公曰：“子何以知之？”曰：“其马力竭矣而犹求焉，故曰败。”

工陲旋而盖规矩，指与物化而不以心稽，故其灵台一而不桎。忘足，履之适也；忘腰，带之适也；知忘是非，心之适也；不内变，不外从，事会之适也；始乎适而未尝不适者，忘适之适也。

有孙休者，踵门而诧子扁庆子曰：“休居乡不见谓不修，临难不见谓不勇。然而田原不遇岁，事君不遇世，宾于乡里，逐于州部，则胡罪乎天哉？休恶遇此命也？”扁子曰：“子独不闻夫至人之自行邪？忘其肝胆，遗其耳目，芒然彷徨乎尘垢之外，逍遥乎无事之业，是谓为而不恃，长而不宰。今汝饰知以惊愚，修身以明污，昭昭乎若揭日月而行也。汝得全而形躯，具而九窍，无中道夭于聋盲跛蹇而比于人数亦幸矣，又何暇乎天之怨哉！子往矣！”

孙子出扁子入。坐有间，仰天而叹。弟子问曰：“先生何为叹乎？”扁子曰：“向者休来，吾告之以至人之德，吾恐其惊而遂至于惑也。”弟子曰：“不然。孙子之所言是邪，先生之所言是邪，非固不能惑是；孙子所言非邪，先生所言是邪，彼固惑而来矣，又奚罪焉！”扁子曰：“不然。昔者有鸟止于鲁郊，鲁君说之，为具太牢要飨之，奏九韶以乐之。鸟乃始忧悲眩视，不敢饮食。此之谓以己养养鸟也。若夫以鸟养养鸟者，宜栖之深林，浮之江湖，食之以委蛇，则平陆而已矣。今休，款启寡闻之民也，吾告以至人之德，譬之若载犀以车马，乐鼹以钟鼓也，彼又恶能无惊乎哉！”

```

山木第二十

```
庄子行于山中，见大木，枝叶盛茂。伐木者止其旁而不取也。问其故，曰：“无所可用。”庄子曰：“此木以不材得终天年。”夫子出于山，舍于故人之家。故人喜，命竖子杀雁而烹之。竖子请曰：“其一能鸣，其一不能鸣，请奚杀？”主人曰：“杀不能鸣者。”明日，弟子问于庄子曰：“昨日山中之木，以不材得终其天年；今主人之雁，以不材死。先生将何处？”庄子笑曰：“周将处乎材与不材之间。材与不材之间，似之而非也，故未免乎累。若夫乘道德而浮游则不然，无誉无訾，一龙一蛇，与时俱化，而无肯专为。一上一下，以和为量，浮游乎万物之祖。物物而不物于物，则胡可得而累邪！此神农、黄帝之法则也。若夫万物之情，人伦之传则不然，合则离，成则毁，廉则挫，尊则议，有为则亏，贤则谋，不肖则欺。胡可得而必乎哉！悲夫，弟子志之，其唯道德之乡乎！”

市南宜僚见鲁侯，鲁侯有忧色。市南子曰：“君有忧色，何也？”鲁侯曰：“吾学先王之道，修先君之业；吾敬鬼尊贤，亲而行之，无须臾离居。然不免于患，吾是以忧。”市南子曰：“君之除患之术浅矣！夫丰狐文豹，栖于山林，伏于岩穴，静也；夜行昼居，戒也；虽饥渴隐约，犹旦胥疏于江湖之上而求食焉，定也。然且不免于罔罗机辟之患，是何罪之有哉？其皮为之灾也。今鲁国独非君之皮邪？吾愿君刳形去皮，洒心去欲，而游于无人之野。南越有邑焉，名为建德之国。其民愚而朴，少私而寡欲；知作而不知藏，与而不求其报；不知义之所适，不知礼之所将。猖狂妄行，乃蹈乎大方。其生可乐，其死可葬。吾愿君去国捐俗，与道相辅而行。”

君曰：“彼其道远而险，又有江山，我无舟车，奈何？”市南子曰：“君无形倨，无留居，以为君车。”君曰：“彼其道幽远而无人，吾谁与为邻？吾无粮，我无食，安得而至焉？”市南子曰：“少君之费，寡君之欲，虽无粮而乃足。君其涉于江而浮于海，望之而不见其崖，愈往而不知其所穷。送君者皆自崖而反。君自此远矣！故有人者累，见有于人者忧。故尧非有人，非见有于人也。吾愿去君之累，除君之忧，而独与道游于大莫之国。方舟而济于河，有虚船来触舟，虽有偏心之人不怒。有一人在其上，则呼张翕之。一呼而不闻，再呼而不闻，于是三呼邪，则必以恶声随之。向也不怒而今也怒，向也虚而今也实。人能虚己以游世，其孰能害之！”

北宫奢为卫灵公赋敛以为钟，为坛乎郭门之外。三月而成上下之县。王子庆忌见而问焉曰：“子何术之设？”奢曰：“一之间，无敢设也。奢闻之：‘既雕既琢，复归于朴。’侗乎其无识，傥乎其怠疑。萃乎芒乎，其送往而迎来。来者勿禁，往者勿止。从其强梁，随其曲傅，因其自穷。故朝夕赋敛而毫毛不挫，而况有大涂者乎！”

孔子围于陈蔡之间，七日不火食。大公任往吊之，曰：“子几死乎？”曰：“然。”“子恶死乎？”曰：“然。”任曰：“予尝言不死之道。东海有鸟焉，其名曰意怠。其为鸟也，分分失失，而似无能；引援而飞，迫胁而栖；进不敢为前，退不敢为后；食不敢先尝，必取其绪。是故其行列不斥，而外人卒不得害，是以免于患。直木先伐，甘井先竭。子其意者饰知以惊愚，修身以明污，昭昭乎若揭日月而行，不不免也。昔吾闻之大成之人曰：‘自伐者无功，功成者堕，名成者亏。’孰能去功与名而还与众人！道流而不明居，得行而不名处；纯纯常常，乃比于狂；削迹捐势，不为功名。是故无责于人，人亦无责焉。至人不闻，子何喜哉！”孔子曰：“善哉！”辞其交游，去其弟子，逃于大泽，衣裘褐，食抒栗，入兽不乱群，入鸟不乱行。鸟兽不恶，而况人乎！

孔子问于桑乎曰：“吾再逐于鲁，伐树于宋，削迹于卫，穷于商周，围于陈蔡之间，吾犯此数患，亲友益疏，徒友益散，何与？”子桑乎曰：“子独不闻假人之亡与？林回弃千金之璧，负赤子而趋。或曰：‘为其布与？赤子之布寡矣；为其累与？赤子之累多矣。弃千金之璧，负赤子而趋，何也？’林回曰：‘彼以利合，此以天属也。’夫以利合者，迫穷患害相弃也；以天属者，迫穷患害相收也。夫相收之与相弃亦远矣，且君子之交淡若水，小人之交甘若醴。君子淡以亲，小人甘以绝，彼无故以合者，则无故以离。”孔子曰：“敬闻命矣！”徐行翔佯而归，绝学捐书，弟子无揖于前，其爱益加进。异日，桑乎又曰：“舜之将死，真泠禹曰：‘汝戒之哉！形莫若缘，情莫若率。’缘则不离，率则不劳。不离不劳，则不求文以待形。不求文以待形，固不待物。”

庄子布大衣而补之，正靡系履而过魏王。魏王曰：“何先生之惫邪？”庄子曰：“贫也，非惫也。士有道德不能行，惫也；衣弊履穿，贫也，非惫也，此所谓非遭时也。王独不见夫腾猿乎？其得冉梓豫章也，揽蔓其枝，而王长其间，虽羿、逢蒙不能裨睨也。及其得柘棘枳枸之间也，危行侧视，振动踔栗，此筋骨非有加急而不柔也，处势不便，未足以逞其能也。今处昏上乱相之间而欲无惫，奚可得邪？此比干之见剖心徵也夫！”

孔子穷于陈蔡之间，七日不火食。左据槁木，右击槁枝，而歌犬氏之风，有其具而无其数，有其声而无宫角。木声与人声，犁然有当于人之心。颜回端拱还目而窥之。仲尼恐其广己而造大也，爱己而造哀也，曰：“回，无受天损易，无受人益难。无始而非卒也，人与天一也。夫今之歌者其谁乎！”回曰：“敢问无受天损易。”仲尼曰：“饥渴寒暑，穷桎不行，天地之行也，运物之泄也，言与之偕逝之谓也。为人臣者，不敢去之。执臣之道犹若是，而况乎所以待天乎？”

“何谓无受人益难？”仲尼曰：“始用四达，爵禄并至而不穷。物之所利，乃非己也。吾命其在外者也。君子不为盗，贤人不为窃，吾若取之，何哉？故曰：鸟莫知于癔而，目之所不宜处不给视，虽落其实，弃之而走。其畏人也而袭诸人间。社稷存焉尔！”“何谓无始而非卒？”仲尼曰：“化其万物而不知其禅之者，焉知其所终？焉知其所始？正而待之而已耳。”“何谓人与天一邪？”仲尼曰：“有人，天也；有天，亦天也。人之不能有天，性也。圣人晏然体逝而终矣！”庄周游于雕陵之樊，睹一异鹊自南方来者。翼广七尺，目大运寸，感周之颡，而集于栗林。庄周曰：“此何鸟哉！翼殷不逝，目大不睹。”蹇裳攫步，执弹而留之，睹一蝉方得美荫而忘其身。螳螂执翳而搏之，见得而忘其形。异鹊从而利之，见利而忘其真。庄周怵然曰：“噫！物固相累，二类相召也。”捐弹而反走，虞人逐而啐之。庄周反入，三月不庭。蔺且从而问之：“夫子何为顷间甚不庭乎？”庄周曰：“吾守形而忘身，观于浊水而迷于清渊。且吾闻诸夫子曰：‘入其俗，从其令。’今吾游于雕陵而忘吾身，异鹊感吾颡，游于栗林而忘真。栗林虞人以吾为戮，吾所以不庭也。”

阳子之宋，宿于逆旅。逆旅人有妾二人，其一人美，其一人恶。恶者贵而美者贱。阳子问其故，逆旅小子对曰：“其美者自美，吾不知其美也；其恶者自恶，吾不知其恶也。”阳子曰：“弟子记之：行贤而去自贤之行，安往而不爱哉！”

```

田子方第二十一

```
田子方侍坐于魏文侯，数称溪公。文侯曰：“溪公，子之师邪？”子方曰：“非也，无择之里人也。称道数当，故无择称之。”文侯曰：“然则子无师邪？”子方曰：“有。”曰：“子之师谁邪？”子方曰：“东郭顺子。”文侯曰：“然则夫子何故未尝称之？”子方曰：“其为人也真。人貌而天虚，缘而葆真，清而容物，物无道，正容以悟之，使人之意也消。无择何足以称之！”子方出，文侯傥然，终日不言。召前立臣而语之曰：“远矣，全德之君子！始吾以圣知之言、仁义之行为至矣。吾闻子方之师，吾形解而不欲动，口钳而不欲言。吾所学者，直土梗耳！夫魏真为我累耳！”

温伯雪子适齐，舍于鲁。鲁人有请见者，温伯雪子曰：“不可。吾闻中国之君子，明乎礼义而陋于知人心。吾不欲见也。”至于齐，反舍于鲁，是人也又请见，温伯雪子曰：“往也蕲见我，今也又蕲见我，是必有以振我也。”出而见客，入而叹。明日见客，又入而叹。其仆曰：“每见之客也，必入而叹，何邪？”曰：“吾固告子矣：中国之民，明乎礼义而陋乎知人心。昔之见我者，进退一成规，一成矩，从容一若龙，一若虎。其谏我也似子，其道我也似父，是以叹也。”仲尼见之而不言。子路曰：“吾子欲见温伯雪子久矣。见之而不言，何邪？”仲尼曰：“若夫人者，目击而道存矣，亦不可以容声矣！”

颜渊问于仲尼曰：“夫子步，亦步；夫子趋，亦趋；夫子驰，亦驰；夫子奔逸绝尘，而回瞠若乎后矣！”夫子曰：“回，何谓邪？”曰：“夫子步，亦步也；夫子言，亦言也；夫子趋，亦趋也；夫子辩，亦辩也；夫子驰，亦驰也；夫子言道，回亦言道也；及奔逸绝尘而回瞠若乎后者，夫子不言而信，不比而周，无器而民滔乎前，而不知所以然而已矣。”仲尼曰：“恶！可不察与！夫哀莫大于心死，而人死亦次之。日出东方而入于西极，万物莫不比方。有目有趾者，待是而后成功。是出则存，是入则亡。万物亦然，有待也而死，有待也而生。吾一受其成形，而不化以待尽。效物而动，日夜无隙，而不知其所终。薰然其成形，知命不能规乎其前。丘以是日徂。吾终身与汝交一臂而失之，可不哀与？女殆著乎吾所以著也。彼已尽矣，而女求之以为有，是求马于唐肆也。吾服女也甚忘，女服吾也亦甚忘。虽然，女奚患焉！虽忘乎故吾，吾有不忘者存。”

孔子见老聃，老聃新沐，方将被发而干，鸷然似非人。孔子便而待之。少焉见，曰：“丘也眩与？其信然与？向者先生形体掘若槁木，似遗物离人而立于独也。”老聃曰：“吾游心于物之初。”孔子曰 ：“何谓邪？”曰：“心困焉而不能知，口辟焉而不能言。尝为女议乎其将：至阴肃肃，至阳赫赫。肃肃出乎天，赫赫发乎地。两者交通成和而物生焉，或为之纪而莫见其形。消息满虚，一晦一明，日改月化，日有所为而莫见其功。生有所乎萌，死有所乎归，始终相反乎无端，而莫知其所穷。非是也，且孰为之宗！”孔子曰：“请问游是。”老聃曰：“夫得是至美至乐也。得至美而游乎至乐，谓之至人。”

孔子曰：“愿闻其方。”曰：“草食之兽不疾易薮，水生之虫不疾易水，行小变而不失其大常也，喜怒哀乐不入于胸次。夫天下也者，万物之所一也。得其所一而同焉，则四肢百体将为尘垢，而死生终始将为昼夜，而莫之能滑，而况得丧祸福之所介乎！弃隶者若弃泥涂，知身贵于隶也。贵在于我而不失于变。且万化而未始有极也，夫孰足以患心！已为道者解乎此。”孔子曰：“夫子德配天地，而犹假至言以修心。古子君子，孰能脱焉！”老聃曰：“不然。夫水之于勺也，无为而才自然矣：至人之于德也，不修而物不能离焉。若天之自高，地之自厚，日月之自明，夫何修焉！”孔子出，以告颜回曰：“丘之于道也，其犹醢鸡与！微夫子之发吾覆也，吾不知天地之大全也。”

庄子见鲁哀公，哀公曰：“鲁多儒士，少为先生方者。”庄子曰：“鲁少儒。”哀公曰：“举鲁国而儒服，何谓少乎？”庄子曰：“周闻之，儒者冠园冠者知天时，履句履者知地形，缓佩袂者事至而断。君子有其道者，未必为其服也；为其服者，未必知其道也。公固以为不然，何不号于国中曰：‘无此道而为此服者，其罪死！’”于是哀公号之五日，而鲁国无敢儒服者。独有一丈夫，儒服而立乎公门。公即召而问以国事，千转万变而不穷。庄子曰：“以鲁国而儒者一人耳，可谓多乎？”

百里奚爵禄不入于心，故饭牛而牛肥，使秦穆公忘其贱，与之政也。有虞氏死生不入于心，故足以动人。

 宋元君将画图，众史皆至，受揖而立，舐笔和墨，在外者半。有一史后至者，檀檀然不趋，受揖不立，因之舍。公使人视之，则解衣般礴蠃。君曰：“可矣，是真画者也。”

武王观于臧，见一丈夫钓，而其钓莫钓。非持其钓有钓者也，常钓也。文王欲举而授之政，而恐大臣父兄之弗安也，欲终而释之，而不忍百姓之无天也。于是旦而属之大夫曰：“昔者寡人梦，见良人黑色而髯，乘驳马而偏朱蹄，号曰：‘寓而政于臧丈人，庶几乎民有瘳乎！’”诸大夫蹴然曰：“先君王也。”文王曰：“然则卜之。”诸大夫曰：“先君之命，王其无它，又何卜焉。”

遂迎臧丈人而授之政。典法无更，偏令无出。三年，文王观于国，则列士坏植散群，长官者不成德，谀斛者不敢入于四竟。列士坏植散群，则尚同也；长官者不成德，则同务也，谀斛者不敢入于四竟，则诸侯无二心也。文王于是焉以为大师，北面而问曰：“政可以及天下乎？”臧丈人昧然而不应，泛然而辞，朝令而夜遁，终身无闻。颜渊问于仲尼曰：“文王其犹未邪？又何以梦为乎？”仲尼曰：“默，汝无言！夫文王尽之也，而又何论刺焉！彼直以循斯须也。”

列御寇为伯昏无人射，引之盈贯，措杯水其肘上，发之，适矢复沓，方矢复寓。当是时，犹象人也，伯昏无人曰：“是射之射，非不射之射也。尝与汝登高山，履危石，临百仞之渊，若能射乎？”于是无人遂登高山，履危石，临百仞之渊，背逡巡，足二分垂在外，揖御寇而进之。御寇伏地，汗流至踵。伯昏无人曰：“夫至人者，上窥青天，下潜黄泉，挥斥八极，神气不变。今汝怵然有恂目之志，尔于中也殆矣夫！”

肩吾问于孙叔敖曰：“子三为令尹而不荣华，三去之而无忧色。吾始也疑子，今视子之鼻间栩栩然，子之用心独奈何？”孙叔敖曰：“吾何以过人哉！吾以其来不可却也，其去不可止也。吾以为得失之非我也，而无忧色而已矣。我何以过人哉！且不知其在彼乎？其在我乎？其在彼也亡乎我，在我也亡乎彼。方将踌躇，方将四顾，何暇至乎人贵人贱哉！”仲尼闻之曰：“古之真人，知者不得说，美人不得滥，盗人不得劫，伏戏、黄帝不得友。死生亦大矣，而无变乎己，况爵禄乎！若然者，其神经乎大山而无介，入乎渊泉而不濡，处卑细而不惫，充满天地，既以与人己愈有。”

楚王与凡君坐，少焉，楚王左右曰“凡亡”者三。凡君曰：“凡之亡也，不足以丧吾存。夫‘凡之亡不足以丧吾存’，则楚之存不足以存存。由是观之，则凡未始亡而楚未始存也。”

```

知北游第二十二

```
知北游于玄水之上，登隐分之丘，而适遭无为谓焉。知谓无为谓曰：“予欲有问乎若：何思何虑则知道？何处何服则安道？何从何道则得道？”三问而无为谓不答也。非不答，不知答也。知不得问，反于白水之南，登狐葵之丘，而睹狂屈焉。知以之言也问乎狂屈。狂屈曰：“唉！予知之，将语若。”中欲言而忘其所欲言。知不得问，反于帝宫，见黄帝而问焉。黄帝曰：“无思无虑始知道，无处无暇始安道，无从无道始得道。”

 知问黄帝曰：“我与若知之，彼与彼不知也，其孰是邪？”黄帝曰；“彼无为谓真是也，狂屈似之，我与汝终不近也。夫知者不言，言者不知，故圣人行不言之教。道不可致，德不可至。仁可为也，义可亏也，礼相伪也。故曰：‘失道而后德，失德而后仁，失仁而后义，失义而后礼。’礼者，道之华而乱之首也。故曰：‘为道者日损，损之又损，以至于无为。无为而无不为也。’今已为物也，欲复归根，不亦难乎！其易也其唯大人乎！生也死之徒，死也生之始，孰知其纪！人之生，气之聚也。聚则为生，散则为死。若死生为徒，吾又何患！故万物一也。是其所美者为神奇，其所恶者为臭腐。臭腐化为神奇，神奇复化为臭腐。故曰：‘通天下一气耳。’圣人故贵一。”知谓黄帝曰：“吾问无为谓，无为谓不应我，非不应我，不知应我也；吾问狂屈，狂屈中欲告我而不我告，非不我告，中欲告而忘之也；今予问乎若，若知之，奚故不近？”黄帝曰：“彼其真是也，以其不知也；此其似之也，以其忘之也；予与若终不近也，以其知之也。”狂屈闻之，以黄帝为知言。

 天地有大美而不言，四时有明法而不议，万物有成理而不说。圣人者，原天地之美而达万物之理。是故至人无为，大圣不作，观于天地之谓也。今彼神明至精，与彼百化。物已四时方圆，莫知其根也，扁然而无为，自古以固存。六合为巨，未离其内；秋毫为小，待之成体；天下莫不沉浮，终身不故；阴阳四时运行，各得其序；昏然若亡而存；油然不形而神；万物畜而不知，此之谓本根，可以观于天矣！

啮缺问道乎被衣，被衣曰：“若正汝形，一汝视，天和将至；摄汝居，一汝度，神将来舍。德将为汝美，道将为汝居。汝瞳焉如新生之犊，而无求其故。”言未卒，啮缺睡寐。被衣大说，行歌而去之。曰：“形若槁骸，心若死灰，真其实知，不以故自持。媒媒晦晦，无心而不可与谋。彼何人哉！”

 舜问乎丞曰：“道可得而有乎？”曰：“汝身非汝有也，汝何得有夫道！”舜曰：“吾身非吾有也，孰有之哉？”曰：“是天地之委形也；生非汝有，是天地之委和也；性命非汝有，是天地之委顺也；孙子非汝有，是天地之委蜕也。故行不知所往，处不知所持，食不知所味，天地之强阳气也，又胡可得而有邪！”

孔子问于老聃曰：“今日晏闲，敢问至道。”老聃曰：“汝齐戒，疏瀹而心，澡雪而精神，剖击而知。夫道杳然难言哉！将为汝言其崖略：夫昭昭生于冥冥，有伦生于无形，精神生于道，形本生于精，而万物以形相生。故九窍者胎生。八窍者卵生。其来无迹，其往无崖，无门无房，四达之皇皇也。邀于此者，四肢强，思虑恂达，耳目聪明。其用心不劳，其应物无方，天不得不高，地不得不广，日月不得不行，万物不得不昌，此其道与！且夫搏之不必知，辩之不必慧，圣人以断之矣！若夫益之而不加益，损之而不加损者，圣人之所保也。渊渊乎其若海，巍巍乎其终则复始也。运量万物而不匮，则君子之道，彼其外与！万物皆往资焉而不匮。此其道与！

“中国有人焉，非阴非阳，处于天地之间，直且为人，将反于宗。自本观之，生者，暗意物也。虽有寿夭，相去几何？须臾之说也，奚足以为尧、桀之是非！果瓜有理，人伦虽难，所以相齿。圣人遭之而不违，过之而不守。调而应之，德也；偶而应之，道也。帝之所兴，忘之所起也。

“人生天地之间，若白驹之过隙，忽然而已。注然勃然，莫不出焉；油然鹨然。莫不入焉。已化而生，又化而死。生物哀之，人类悲之。解其天鼗，堕其天囊。纷乎宛乎，魂魄将往，乃身从之。乃大归乎！不形之形，形之不形，是人之所同知也，非将至之所务也，此众人之所同论也。彼至则不论，论则不至；明见无值，辩不若默；道不可闻，闻不若塞：此之谓大得。”

东郭子问于庄子曰：“所谓道，恶乎在？”庄子曰：“无所不在。”东郭子曰：“期而后可。”庄子曰：“在蝼蚁。”曰：“何其下邪？”曰：“在梯稗。”曰：“何其愈下邪？”曰：“在瓦劈。”曰：“何其愈甚邪？”曰：“在屎溺。”东郭子不应。庄子曰：“夫子之问也，固不及质。正获之问于监市履烯也，每下愈况。汝唯莫必，无乎逃物。至道若是，大言亦然。周、遍、咸三者，异名同实，其指一也。尝相与游乎无何有之宫，同合而论，无所终穷乎！尝相与无为乎！澹而静乎！漠而清乎！调而间乎！寮已吾志，无往焉而不知其所至，去而来而不知其所止。吾已往来焉而不知其所终，彷徨乎冯闳，大知入焉而不知其所穷。物物者与物无际，而物有际者，所谓物际者也。不际之际，际之不际也。谓盈虚衰杀，彼为盈虚非盈虚，彼为衰杀非衰杀，彼为本末非本末，彼为积散非积散也。”

可荷甘与神农同学于老龙吉。神农隐几，阖户昼瞑。可荷甘日中爹户而入，曰：“老龙死矣！”神农隐几拥杖而起，曝然放杖而笑，曰：“天知予僻陋慢池，故弃予而死。已矣，夫子无所发予之狂言而死矣夫！”合冈吊闻之，曰：“夫体道者，天下之君子所系焉。今于道秋豪之端万分未得处一焉，而犹知藏其狂言而死，又况夫体道者乎！视之无形，听之无声，于人之论者，谓之冥冥，所以论道而非道也。”

于是泰清问乎无穷，曰：“子知道乎？”无穷曰：“吾不知。”又问乎无为，无为曰：“吾知道。”曰：“子之知道，亦有数乎？”曰：“有。”曰：“其数若何？”无为曰：“吾知道之可以贵，可以贱，可约，可以散，此吾所以知道之数也。”泰清以之言也问乎无始，曰：“若是，则无穷之弗知与无为之知，孰是而孰非乎？”无始曰：“不知深矣，知之浅矣；弗知内矣，知之外矣。”于是泰清中而叹曰：“弗知乃知乎，知乃不知乎！孰知不知之知？”无始曰：“道不可闻，闻而非也；道不可见，见而非也；道不可言，言而非也！知形形之不形乎！道不当名。”无始曰：“有问道而应之者，不知道也；虽问道者，亦未闻道。道无问，问无应。无问问之，是问穷也；无应应之，是无内也。以无待问穷，若是者，外不观乎宇宙，内不知乎太初。是以不过乎昆仑，不游乎太虚。”

光曜问乎无有曰：“夫子有乎？其无有乎？”光曜不得问，而孰视其状貌：杳然空然。终日视之而不见，听之而不闻，搏之而不得也。光曜曰：“至矣，其孰能至此乎！予能有无矣，而未能无无也。及为无有矣，何从至此哉！”

大马之捶钩者，年八十矣，而不失豪芒。大马曰：“子巧与！有道与？”曰：“臣有守也。臣之年二十而好捶钩，于物无视也，非钩无察也。”是用之者假不用者也，以长得其用，而况乎无不用者乎！物孰不资焉！

冉求问于仲尼曰：“未有天地可知邪？”仲尼曰：“可。古犹今也。”冉求失问而退。明日复见，曰：“昔者吾问，‘未有天地可知乎？’夫子曰：‘可，古犹今也。’昔日吾昭然，今日吾昧然。敢问何谓也？”仲尼曰：“昔之昭然也，神者先受之；今之昧然也，且又为不神者求邪！无古无今，无始无终。未有子孙而有子孙可乎？”冉求未对。仲尼曰：“已矣，未应矣！不以生生死，不以死死生。死生有待邪？皆有所一体。有先天地生者物邪？物物者非物，物出不得先物也，犹其有物也；犹其有物也无已！圣人之爱人也终无已者，亦乃取于是者也。”

颜渊问乎仲尼曰：“回尝闻诸夫子曰：‘无有所将，无有所迎。’回敢问其游。”仲尼曰：“古之人外化而内不化，今之人内化而外不化，与物化者，一不化者也。安化安不化？安与之相靡？必与之莫多。烯韦氏之囿，黄帝之圃，有虞氏之宫，汤武之室。君子之人，若儒墨者师，故以是非相齑也，而况今之人乎！圣人处物不伤物。不伤物者，物亦不能伤也。唯无所伤者，为能与人相将迎。山林与，皋壤与，使我欣欣然而乐与！乐未毕也，哀又继之。哀乐之来，吾不能御，其去弗能止。悲夫，世人直为物逆旅耳！夫知遇而不知所不遇，知能能而不能所不能。无知不能者，固人之所不免也。夫务免乎人之所不免者，岂不亦悲哉！至言去言，至为去为。齐知之所知，则浅矣！”

```

杂篇

庚桑楚第二十三

```
老聃之役，有庚桑楚者，偏得老聃之道，以北居畏垒之山。其臣之画然知者去之，其妾之挈然仁者远之。拥肿之与居，鞅掌之为使。居三年，畏垒大壤。畏垒之民相与言曰：“庚桑子之始来，吾洒然异之。今吾日计之而不足，岁计之而有余。庶几其圣人乎！子胡不相与尸而祝之，社而稷之乎？”庚桑子闻之，南面而不释然。弟子异之。庚桑子曰：“弟子何异于予？夫春气发而百草生，正得秋而万宝成。夫春与秋，岂无得而然哉？天道已行矣。吾闻至人，尸居环堵之室，而百姓猖狂，不知所如往。今以畏垒之细民，而窃窃欲俎豆予于贤人之间，我其勺人邪？吾是以不释于老聃之言。”

弟子曰：“不然。夫寻常之沟，臣鱼无所还其体，而鲵鳅为之制；步仞之丘陵，巨兽无所隐其躯，而蘖狐为之祥。且夫尊贤授能，先善与利，自古尧、舜以然，而况畏垒之民乎！夫子亦听矣！”庚桑子曰：“小子来！夫函车之兽，介而离山，则不免于罔罟之患；吞舟之鱼，炀而失水，则蚁能苦之。故鸟兽不厌高，鱼鳖不厌深。夫全其形生之人，藏其身也，不厌深眇而已矣！且夫二子者，又何足以称扬哉！是其于辩也，将妄凿垣墙而殖蓬蒿也，简发而栉，数米而炊，窃窃乎又何足以济世哉！举贤则民相轧，任知则民相盗。之数物者，不足以厚民。民之于利甚勤，子有杀父，臣有杀君；正昼为盗，日中穴杯。吾语女：大乱之本，必生于尧、舜之间，其末存乎千世之后。千世之后，其必有人与人相食者也。”

南荣珠蹴然正坐曰：“若珠之年者已长矣，将恶乎托业以及此言邪？”庚桑子曰：“全汝形，抱汝生，无使汝思虑营营。若此三年，则可以及此言矣！”南荣珠曰：“目之与形，吾不知其异也，而盲者不能自见；耳之与形，吾不知其异也，而聋者不能自闻；心之与形，吾不知其异也，而狂者不能自得。形之与形亦辟矣，而物或间之邪？欲相求而不能相得。今未珠曰：‘全汝形，抱汝生，勿使汝思虑营营。’珠勉闻道达耳矣！”庚桑子曰：“辞尽矣，曰：奔蜂不能化藿躅，越鸡不能伏鹄卵，鲁鸡固能矣！鸡之与鸡，其德非不同也。有能与不能者，其才固有巨小也。今吾才小，不足以化子。子胡不南见老子！”

南荣珠赢粮，七日七夜至老子所。老子曰：“子自楚之所来乎？”南荣珠曰：“唯。”老子曰：“子何与人偕来之众也？”南荣珠惧然顾其后。老子曰：“子不知吾所谓乎？”南荣珠俯而惭，仰而叹，曰：“今者吾忘吾答，因失吾问。”老子曰：“何谓也？”南荣珠曰：“不知乎人谓我朱愚，知乎反愁我躯；不仁则害人，仁则反愁我身；不义则伤彼，义则反愁我己。我安逃此而可？此三言者，珠之所患者。愿因楚而问之。”老子曰：“向吾见若眉睫之间，吾因以得汝矣。今汝又言而信之。若规规然若丧父母，揭竿而求诸海也，女亡人哉！惘惘乎，汝欲反汝情性而无由入，可怜哉！”

南荣珠请入就舍，召其所好，去其所恶。十日自愁，复见老子。老子曰：“汝自洒濯，熟哉郁郁乎！然而其中津津乎犹有恶也。夫外攉者不可繁而捉，将内捷；内攉者不可缪而捉，将外捷；外内攉者，道德不能持，而况放道而行者乎！”南荣珠曰：“里人有病，里人问之，病者能言其病，病者犹未病也。若珠之闻大道，譬犹饮药以加病也。珠愿闻卫生之经而已矣。”老子曰：“卫生之经，能抱一乎！能勿失乎！能无卜筮而知吉凶乎！能止乎！能已乎！能舍诸人而求诸己乎！能攸然乎！能侗然乎！能儿子乎！儿子终日嗥而嗌不嘎，和之至也；终日握而手不倪，共其德也，终日视而目不演，偏不在外也。行不知所之，居不知所为，与物委蛇而同其波。是卫生之经已。”

南荣珠曰：“然则是至人之德已乎？”曰：“非也。是乃所谓冰解冻释者，能乎？夫至人者，相与交食乎地而交乐乎天，不于人物利害相樱，不相与为怪，不相与为谋，不相与为事，攸然而往，侗然而来。是谓卫生之经已。”曰：“然则是至乎？”曰：“未也。吾固告汝曰：‘能儿子乎！’儿子动不知所为，行不知所之，身若槁木之枝而心若死灰。若是者，祸亦不至，福亦不来。祸福无有，恶有人灾也！”

宇泰定者，发乎天光。发乎天光者，人见其人。人有修者，乃今有恒。有恒者，人舍之，天助之。人之所舍，谓之天民；天之所助，谓之天子。

学者，学其所不能学也？行者，行其所不能行也？辩者，辩其所不能辩也？知止乎其所不能知，至矣！若有不即是者，天钧败之。备物以将形，藏不虞以生心，敬中以达彼。若是而万恶至者，皆天也，而非人也，不足以滑成，不可内于灵台。灵台者有持，而不知其所持，而不可持者也。不见其诚己而发，每发而不当；业入而不舍，每更为失。为不善乎显明之中者，人得而诛之；我不善乎幽间之中者，鬼得而诛之。明乎人，明乎鬼者，然后能独行。券内者，行乎无名；券外者，志乎期费。行乎无名者，唯庸有光；志乎期费者，唯贾人也。人见其歧，犹之魁然。与物穷者，物入焉；与物且者，其身之不能容，焉能容人！不能容人者无亲，无亲者尽人。兵莫谮于志，镆铘为下；寇莫大于阴阳，无所逃于天地之间。非阴阳贼之，心则使之也。

道通其分也，其成也毁也。所恶乎分者，其分也以备。所以恶乎备者？其有以备。故出而不反，见其鬼。出而得，是谓得死。灭而有实，鬼之一也。以有形者象无形者而定矣！出无本，入无窍，有实而无乎处，有长而无乎本剽，有所出而无窍者有实。有实而无乎处者，宇也；有长而无本剽者，宙也。有乎生，有乎死；有乎出，有乎入。入出而不见其形，是谓天门。天门者，无有也。万物出乎无有。有不能以有为有，必出乎无有，而无有一无有。圣人藏乎是。

古之人，其知有所至矣。恶乎至？有以为未始有物者，至矣，尽矣，弗可以加矣！其次以为有物矣，将以生为丧也，以死为反也，是以分已。其次曰始无有，既而有生，生俄而死。以无有为有，以生为体，以死为尻。孰知有无死生之一守者，吾与之为友。是三者虽异，公族也。昭景也，著戴也；甲氏也，著封也：非一也。

有生黑者，披然曰移是。尝言移是，非所言也。虽然，不可知者也。腊者之有篦眩，可散而不可散也；观室者周于寝庙，又适其偃焉！为是举移是。请尝言移是：是以生为本，以知为师，因以乘是非。果有名实，因以己为质，使人以为己节，因以死偿节。若然者，以用为知，以不用为愚；以彻为名，以穷为辱。移是，今之人也，是蜩与学鸠同于同也。

碾市人之足，则辞以放骜，兄则以妪，大亲则已矣。故曰：至礼有不人，至义不物，至知不谋，至仁无亲，至信辟金。

彻志之勃，解心之谬，去德之累，达道之塞。贵富显严名利六者，勃志也；容动色理气意六者，谬心也；恶欲喜怒哀乐六者，累德也；去就取与知能六者，塞道也。此四六者不荡胸中则正，正则静，静则明，明则虚，虚则无为而无不为也。

道者，德之钦也；生者，德之光也；性者，生之质也。性之动谓之为，为之伪谓之失。知者，接也；知者，谋也。知者之所不知，犹睨也。动以不得已之谓德，动无非我之谓治，名相反而实相顺也。

羿工乎中微而拙乎使人无己誉；圣人工乎天而拙乎人；夫工乎天而浪乎人者，唯全人能之。虽虫能虫，虽虫能天。全人恶天，恶人之天，而况吾天乎人乎！一雀适羿，羿必得之，威也。以天下为之笼，则雀无所逃。是故汤以庖人笼伊尹，秦穆公以五羊之皮笼百里奚。是故非以其所好笼之而可得者，无有也。

介者移画，外非誉也。胥靡登高而不惧，遗死生也。夫复习不愧而忘人，忘人，因以为天人矣！故敬之而不喜，侮之而不怒者，唯同乎天和者为然。出怒不怒，则怒出于不怒矣；出为无为，则为出于无为矣！欲静则平气，欲神则顺心。有为也欲当，则缘于不得已。不得已之类，圣人之道。

```

徐无鬼第二十四

```
徐无鬼因女商见魏武侯，武侯劳之曰：“先生病矣，苦于山林之劳，故乃肯见于寡人。”徐无鬼曰：“我则劳于君，君有何劳于我！君将盈嗜欲，长好恶，则性命之清病矣；君将黜嗜欲，挈好恶，则耳目病矣。我将劳君，君有何劳于我！”武侯超然不对。少焉，徐无鬼曰：“尝语君吾相狗也：下之质，执饱而止，是狸德也；中之质，若视日；上之质，若亡其一。吾相狗又不若吾相马也。吾相马：直者中绳，曲者中钩，方者中矩，圆者中规。是国马也，而未若天下马也。天下马有成材，若恤其失，若丧其一。若是者，超轶绝尘，不知其所。”武侯大悦而笑。

徐无鬼出，女商曰：“先生独何以说吾君乎？吾所以说吾君者，横说胡子则以《诗》、《书》、《礼》、《乐》，从说之则以《金板》、《六韬》，奉事而大有功者不可为数，而吾君未尝启齿。今先生何以说吾君？使吾君说若此乎？”徐无鬼曰：“吾直告之吾相狗马耳。”女商曰：“若是乎？”曰：“子不闻夫越之流人乎？去国数日，见其所知而喜；去国旬月，见所尝见于国中者喜；及期年也，见似人者而喜矣。不亦去人滋久、思人滋深乎？夫逃虚空者，藜藿柱乎猩鼬之径，踉位其空，闻人足音空然而喜矣，又况乎昆弟亲戚之声咳其侧者乎！久矣夫，莫以真人之言声咳吾君之侧乎！”

徐无鬼见武侯，武侯曰：“先生居山林，食芋栗，厌葱韭，以宾寡人，久矣夫！今老邪？其欲干酒肉之味邪？其寡人亦有社稷之福邪？”徐无鬼曰：“无鬼生于贫贱，未尝敢饮食君之酒肉，将来劳君也。”君曰：“何哉！奚劳寡人？”曰：“劳君之神与形。”武侯曰：“何谓邪？”徐无鬼曰：“天地之养也一，登高不可以为长，居下不可以为短。君独为万乘之主，以苦一国之民，以养耳目鼻口，夫神者不自许也。夫神者，好和而恶奸。夫奸，病也，故劳之。唯君所病之何也？”武侯曰：“欲见先生久矣！吾欲爱民而为义偃兵，可乎？”徐无鬼曰：“不可。爱民，害民之始也；为义寝兵，造兵之本也。君自此为之，则殆不成。凡成美，恶器也。君虽为仁义，几且伪哉！形固造形，成固有伐，变固外战。君亦必无盛鹤列于丽樵之间，无徒骥于缁坛之宫，无藏逆于得，无以巧胜人，无以谋胜人，无以战胜人。夫杀人之士民，兼人之土地，以养吾私与吾神者，其战不知孰善？胜之恶乎在？君若勿已矣！修胸中之诚以应土地之情而勿撄。夫民死已脱矣，君将恶乎用夫偃兵哉！”

黄帝将见大槐乎具茨之山，方明为御，昌寓骖乘，张若习朋前马，昆昏滑稽后车。至于襄城之野，七圣皆迷，无所问涂。适遇牧马童子，问涂焉，曰：“若知具茨之山乎？”曰：“然。”“若知大槐之所存乎？”曰：“然。”黄帝曰：“异哉小童！非徒知具茨之山，又知大槐之所存。请问为天下。”小童曰：“夫为天下者，亦若此而已矣，又奚事焉！予少而自游于六合之内，予适有瞀病，有长者教予曰：‘若乘日之车而游于襄城之野。’今予病少痊，予又且复游于六合之外。夫为天下亦若此而已，予又奚事焉！”黄帝曰：“夫为天下者，则诚非吾子之事，虽然，请问天下。”小童辞。皇帝又问。小童曰：“夫为天下者，亦奚以异乎牧马哉！亦去其害马者而已矣！”黄帝再拜稽首，称天师而退。

知士无思虑之变则不乐；辩士无谈说之序则不乐；察士无凌淬之事则不乐：皆囿于物者也。招世之士兴朝；中民之士荣官；筋力之士矜难；勇敢之士奋患；兵革之士乐战；枯槁之士宿名；法律之士广治；礼教之士敬容；仁义之士贵际。农夫无草莱之事则不比；商贾无市井之事则不比；庶人有旦暮之业则劝；百工有器械之巧则壮。钱财不积则贪者忧，权势不尤则夸者悲，势物之徒乐变。遭时有所用，不能无为也，此皆顺比于岁，不物于易者也。驰其形性，潜之万物，终身不反，悲夫！

庄子曰：“射者非前期而中谓之善射，天下皆羿也，可乎？”惠子曰：“可。”庄子曰：“天下非有公是也，而各是其所是，天下皆尧也，可乎？”惠子曰：“可。”庄子曰：“儒墨杨秉四，与夫子为五，果孰是邪？或者若鲁遽者邪？其弟子曰：‘我得夫子之道矣！吾能冬歆鼎而夏造冰矣！’鲁遽曰：‘是直以阳召阳，以阴召阴，非吾所谓道也。吾示子乎吾道。’于是为之调瑟，废一于堂，废一于室，鼓宫宫动，鼓角角动，音律同矣！夫或改调一弦，于五音无当也，鼓之，二十五弦皆动，未始异于声而音之君已！且若是者邪！”惠子曰：“今夫儒墨杨秉，且方与我以辩，相拂以辞，相镇以声，而未始吾非也，则奚若矣？”庄子曰：“齐人谪于宋者，其命昏也不以完；其求刑钟也以束缚；其求唐子也而未始出域；有遗类矣夫！楚人寄而谪昏者；夜半于无人之时而与舟人斗，未始离于岑而足以造于怨也。”

庄子送葬，过惠子之墓，顾谓从者曰：“郢人垩慢其鼻端若蝇翼，使匠石斫之。匠石运斤成风听而斫之，尽垩而鼻不伤，郢人立不失容。宋元君闻之，召匠石曰：‘尝试为寡人为之。’匠石曰：‘臣则尝能斫之。虽然，臣之质死久矣！’自夫子之死也，无无以为质矣，吾无与言之矣！”

管仲有病，桓公问之曰：“仲父之病病矣，可不谓云至于大病，则寡人恶乎属国而可？”管仲曰：“公谁欲与？”公曰：“鲍叔牙。”曰：“不可。其为人挈廉，善士也；其于不己若者，不比之又，一闻人之过，终身不忘。使之治国，上且钩乎君，下且逆乎民。其得罪于君也将弗久矣！”公曰：“然则孰可？”对曰：“勿已则隰朋可。其为人也，上忘而下畔，愧不若黄帝，而哀不己若者。以德分人谓之圣；以财分人谓之贤。以贤临人，末有得人者也；以贤下人，未有不得人者也。其于国有不闻也，其于家有不见也。勿已则隰朋可。”

吴王浮于江，登乎狙之山，众狙见之，恂然弃而走，逃于深蓁。有一狙焉，委蛇攫抓，见巧乎王。王射之，敏给搏捷矢。王命相者趋射之，狙执死。王顾谓其友颜不疑曰：“之狙也，伐其巧，恃其便，以敖予，以至此殛也。戒之哉！嗟乎！无以汝色骄人哉！”颜不疑归而师董梧，以锄其色，去乐辞显，三年而国人称之。

南伯子綦隐几而作，仰天而嘘。颜成子入见曰：“夫子，物之尤也。形固可使若槁骸，心固可使若死灰乎？”曰：“吾尝居山穴之口矣。当是时也，田禾一睹我而齐国之众三贺之。我必先之，彼故知之；我必卖之，彼故鬻之。若我而不有之，彼恶得而知之？若我而不卖之，彼恶得而鬻之？嗟乎！我悲人之自丧者；吾又悲夫悲人者；吾又悲夫悲人之悲者；其后日远矣！”

仲尼之楚，楚王觞之。孙叔敖执爵而立。市南宜僚受酒而祭，曰：“古之人乎！于此言已。”曰：“丘也闻不言之言矣，未之尝言，于此乎言之：市南宜僚弄丸而两家之难解；孙叔敖甘寝秉羽而郢人投兵；丘愿有喙三尺。”彼之谓不道之道，此之谓不言之辩。故德总乎道之所一，而言休乎知之所不知，至矣。道之所一者，德不能同也。知之所不能知者，辩不能举也。名若儒墨而凶矣。故海不辞东流，大之至也。圣人并包天地，泽及天下，而不知其谁氏。是故生无爵，死无谥，实不聚，名不立，此之谓大人。狗不以善吠为良，人不以善言为贤，而况为大乎！夫为大不足以为大，而况为德乎！夫大备矣莫若天地。然奚求焉，而大备矣！知大备者，无求，无失，无弃，不以物易己也。反己而不穷，循古而不摩，大人之诚！

子綦有八子，陈诸前，召九方湮曰：“为我相吾子，孰为祥。”九方湮曰：“困也为祥。”子綦瞿然喜曰：“奚若？”曰：“困也，将与国君同食以终其身。”子綦索然出涕曰：“吾子何为以至于是极也？”九方湮曰：“夫与国君同食，泽及三族，而况父母乎！今夫子闻之而泣，是御福也。子则祥矣，父则不祥。”子綦曰：“湮，汝何足以使之。而困祥邪？尽于酒肉，入于鼻口矣，而何足以知其所自来！吾未尝为牧而佯生于奥，未尝好田而鹑生于夭，若勿怪，何邪？吾所与吾子游者，游于天地，吾与之邀乐于天，吾与之邀食于地。吾不与之为事，不与之为谋，不与之为怪。吾与之乘天地之诚而不以物与之相撄，吾与之一委蛇而不与之为事所宜。今也然有世俗之偿焉？凡有怪征者必有怪行。殆乎！非我与吾子之罪，几天与之也！吾是以泣也。”无几何而使困之于燕，盗得之于道，全而鬻之则难，不若刖之则易。于是乎刖而鬻之于齐，适当渠公之街，然身食肉而终。

啮缺遇许由曰：“子将奚之？”曰：“将逃尧。”曰：“奚谓邪？”曰：“夫尧畜畜然仁，吾恐其为天下笑。后世其人与人相食与！夫民不难聚也，爱之则亲，利之则至，誉之则劝，致其以恶则散。爱利出乎仁义，捐仁义者寡，利仁义者众。夫仁义之行，唯且无诚，且假乎禽贪者器。是以一人断制天下，譬之犹一见也。夫尧知贤人之利天下也，而不知其贼天下也。夫唯外乎贤者知之矣。”

有暖姝者，有濡需者，有卷娄者。所谓暖姝者，学一先生之言，则暖暖姝姝而私自说也，自以为足矣，而未知未始有物也。是以谓暖姝者也。濡需者，豕虱是也，择疏鬣，自以为广宫大囿。奎蹄曲隈，乳间股脚，自以为安室利处。不知屠者之一旦鼓臂布草操烟火，而己与豕俱焦也。此以域进，此以域退，此其所谓濡需者也。卷娄者，舜也。羊肉不慕蚁，蚁慕羊肉，羊肉膻也。舜有膻行，百姓悦之，故三徙成都，至邓之墟而十有万家。尧闻舜之贤，举之童土之地，曰：“冀得其来之泽。”舜举童土之地，年齿长矣，聪明衰矣，而不得休归，所谓卷娄者也。是以神人恶众至，众至则不比，不比则不利也。故无所甚亲，无所甚疏，抱德炀和，以顺天下，此谓真人。于蚁弃知，于鱼得计，于羊弃意。于目视目，以耳听耳，以心复心。若然者，其平也绳，其变也循。古之真人！以天待之，不以人入天，古之真人！

得之也生，失之也死；得之也死，失之也生：药也。其实堇也，桔梗也，鸡臃也，豕零也，是时为帝者也，何可胜言！

句践也以甲盾三千栖于会稽，唯种也能知亡之所以存，唯种也不知其身之所以愁。故曰：鸱目有所适，鹤颈有所节，解之也悲。故曰：风之过，河也有损焉；日之过，河也有损焉；请只风与日相与守河，而河以为未始其撄也，恃源而往者也。故水之守土也审，影之守人也审，物之守物也审。故目之于明也殆，耳之于聪也殆，心之于殉也殆，凡能其于府也殆，殆之成也不给改。祸之长也兹萃，其反也缘功，其果也待久。而人以为己宝，不亦悲乎！故有亡国戮民无已，不知问是也。故足之于地也践，虽践，恃其所不碾而后善博也；人之于知也少，虽少，恃其所不知而后知天之所谓也。知大一，知大阴，知大目，知大均，知大方，知大信，知大定，至矣！大一通之，大阴解之，大目视之，大均缘之，大方体之，大信稽之，大定持之。

尽有天，循有照，冥有枢，始有彼。则其解之也似不解之者，其知之也似不知之也，不知而后知之。其问之也，不可以有崖，而不可以无崖。碣滑有实，古今不代，而不可以亏，则可不谓有大扬榷乎！阖不亦问是已，奚惑然为！以不惑解惑，复于不惑，是尚大不惑。

```

则阳第二十五

```
则阳游于楚，夷节言之于王，王未之见。夷节归。彭阳见王果曰：“夫子何不谭我于王？”王果曰：“我不若公阅休。”彭阳曰：“公阅休奚为者邪？”曰：“冬则捉鳖于江，夏则休乎山樊。有过而问者，曰：‘此予宅也。’夫夷节已不能，而况我乎！吾又不若夷节。夫夷节之为人也，无德而有知，不自许，以之神其交，固颠冥乎富贵之地。非相助以德，相助消也。夫冻者假衣于春，喝者反冬乎冷风。夫楚王之为人也，形尊而严。其于罪也，无赦如虎。非夫佞人正德，其孰能挠焉。故圣人其穷也，使家人忘其贫；其达也，使王公忘爵禄而化卑；其于物也，与之为娱矣；其于人也，乐物之通而保己焉。故或不言而饮人以和，与人并立而使人化，夫子之宜。彼其乎归居，而一闲其所施。其于人心者，若是其远也。故曰：‘待公阅休’。”

圣人达绸缪，周尽一体矣，而不知其然，性也。复命摇作而以天为师，人则从而命之也。忧乎知而所行恒无几时，其有止也若之何！生而美者，人与之鉴，不告则不知其美于人也。若知之，若不知之，若闻之，若不闻之，其可喜也终无已，人之好之亦无已，性也。圣人之爱人也，人与之名，不告则不知其爱人也。若知之，若不知之，若闻之，若不闻之，其爱人也终无已，人之安之亦无已，性也。

旧国旧都，望之畅然。虽使丘陵草木之缗入之者十九犹之畅然，况见见闻闻者也，以十仞之台县众间者也。冉相氏得其环中以随成，与物无终无始，无几无时。日与物化者，一不化者也。阖尝舍之！夫师天而不得师天。与物皆殉。其以为事也，若之何！夫圣人未始有天，未始有人，未始有始，未始有物，与世偕行而不替，所行之备而不恤，其合之也，若之何！汤得其司御门尹登恒为之傅之。从师而不囿，得其随成。为之司其名，之名嬴法，得其两见。仲尼之尽虑，为之傅之。容成氏曰：“除日无岁，无内无外。”

魏莹与田侯牟约，田侯牟背之，魏莹怒，将使人刺之。犀首闻而耻之，曰：“君为万乘之君也，而以匹夫从仇。衍请受甲二十万，为君攻之，虏其人民，系其牛马，使其君内热发于背，然后拔其国。忌也出走，然后佚其背，折其脊。”季子闻而耻之，曰：“筑十仞之城，城者既十仞矣，则又坏之，此胥靡之所苦也。今兵不起七年矣，此王之基也。衍，乱人也，不可听也。”华子闻而丑之，曰：“善言伐齐者，乱人也；善言勿伐者，亦乱人也；谓‘伐与不伐乱人也’者，又乱人也。”君曰：“然则若何？”曰：“君求其道而已矣。”

惠子闻之，而见戴晋人。戴晋人曰：“有所谓蜗者，君知之乎？”曰：“然。”“有国于蜗之左角者，曰触氏；有国有蜗之右角者，曰蛮氏。时相与争地而战，伏尸数万，逐北，旬有五日而后反。”君曰：“噫！其虚言与？”曰：“臣请为君实之。君以意在四方上下有穷乎？”君曰：“无穷。”曰：“知游心于无穷，而反在通达之国，若存若亡乎？”君曰：“然。”曰：“通达之中有魏，于魏中有梁，于梁中有王，王与蛮氏有辩乎？”君曰：“无辩。”客出而君傥然若有亡也。客出，惠子见。君曰：“客，大人也，圣人不足以当之。”惠子曰：“夫吹管也，犹有稿也；吹剑者，决而已矣。尧、舜，人之所誉也。道尧、舜于戴晋人之前，譬犹一决也。”

孔子之楚，舍于蚁丘之浆。其邻有夫妻臣妾登极者，子路曰：“是稷稷何为者邪？”仲尼曰：“是圣人仆也。是自埋于民，自藏于畔。其声销，其志无穷，其口虽言，其心未尝言。方且与世违，而心不屑与之俱。是陆沉者也，是其市南宜僚邪？”子路请往召之。孔子曰：“已矣！彼知丘之著于己也，知丘之适楚也，以丘为必使楚王之召己也。彼且以丘为佞人也。夫若然者，其于佞人也，羞闻其言，而况亲见其身乎！而何以为存！”子路往视之，其室虚矣。

长梧封人问子牢曰：“君为政焉勿卤莽，治民焉勿灭裂。昔予为禾，耕而卤莽之，则其实亦卤莽而报予；芸而灭裂之，其实亦灭裂而报予。予来年变齐，深耕而熟耨之，其禾繁以滋，予终年厌餐。”庄子闻之曰：“今人之治其形，理其心，多有似封人之所谓：遁其天，离其性，减其情，亡其神，以众伪。故卤莽其性者，欲恶之孽，为性蔺苇廉葭始萌，以扶吾形，寻擢吾性，并溃漏发，不择所出，漂疽疥臃，内热溲膏，是也。”

```

柏矩学于老聃，曰：“请之天下游。”老聃曰：“已矣！天下犹是也。”又请之，老聃曰：“汝将何始？”曰：“始于齐。”至齐，见辜人焉，推而强之，解朝服而幕之，号天而哭之，曰：“子乎！子乎！天下有大灾，子独先离之曰，莫为盗，莫为杀人。荣辱立然后睹所病，货财聚然后睹所争。今立人之所病，聚人之所争，穷困人之身，使无休时。欲无至此得乎？古之君人者，以得为在民，以失为在己；以正为在民，以枉为在己。故一形有失其形者，退而自责。今则不然，匿为物而愚不识，大为难而罪不敢，重为任而罚不胜，远其涂而诛不至。民知力竭，则以伪继之。日出多伪，士民安取不伪。夫力不足则伪，知不足则欺，财不足则盗。盗窃之行，于谁责而可乎？”

```
遽伯玉行年六十而六十化，未尝不始于是之，而卒绌之以非也。未知今之所谓是之非五十九非也。万物有乎生而莫见其根，有乎出而莫见其门。人皆尊其知之所知，而莫知恃其知之所不知而后知，可不谓大疑乎！已乎！已乎！且无所逃。此所谓然与然乎！

仲尼问于太史大滔、伯尝骞、烯韦曰：“卫灵公饮酒湛乐，不听国君之政；田猎毕弋，不应诸侯之际：其所以为灵公者何邪？”大滔曰：“是因是也。”伯常骞曰：“夫灵公有妻三人，同滥而浴。史鳅奉御而进，所搏币而扶翼。其慢若彼之甚也，见贤人若此其肃也，是其所以为灵公也。”烯韦曰：“夫灵公也，死卜葬于故墓，不吉；卜葬于沙丘而吉。掘之数仞，得石椁焉，洗而视之，有铭焉，曰：‘不冯其子，灵公夺而里之。’夫灵公之为灵也久矣！之二人何足以识之。”

少知问于大公调曰：“何谓丘里之言？”大公调曰：“丘里者，合十姓百名而以为风俗也，合异以为同，散同以为异。今指马之百体而不得马，而马系于前者，立其百体而谓之马也。是故丘山积卑而为高，江河合水而为大，大人合并而为公，是以自外入者，有主而不执；由中出者，有正而不距。四时殊气，天不赐，故岁成；五官殊职，君不私，故国治；文武大人不赐，故德备；万物殊理，道不私，故无名。无名故无为，无为而无不为。时有终始，世有变化，祸福溷溷，至有所拂者而有所宜，自殉殊面；有所正者有所差，比于大泽，百材皆度；观于大山，木石同坛。此之谓丘里之言。”少知曰：“然则谓之道足乎？”大公调曰：“不然，今计物之数，不止于万，而期曰万物者，以数之多者号而读之也。是故天地者，形之大者也；阴阳者，气之大者也；道者为之公。因其大而号以读之则可也，已有之矣，乃将得比哉！则若以斯辩，譬犹狗马，其不及远矣。”

少知曰：“四方之内，六合之里，万物之所生恶起？”大公调曰：“阴阳相照相盖相治，四时相代相生相杀。欲恶去就，于是桥起。雌雄片合，于是庸有。安危相易，祸福相生，缓急相摩，聚散以成。此名实之可纪，精微之可志也。随序之相理，桥运之相使，穷则反，终则始，此物之所有。言之所尽，知之所至，极物而已。睹道之人，不随其所废，不原其所起，此议之所止。”少知曰：“季真之莫为，接子之或使。二家之议，孰正于其情，孰偏于其理？”大公调曰：“鸡鸣狗吠，是人之所知。虽有大知，不能以言读其所自化，又不能以意其所将为。斯而析之，精至于无伦，大至于不可围。或之使，莫之为，未免于物而终以为过。或使则实，莫为则虚。有名有实，是物之居；无名无实，在物之虚。可言可意，言而愈疏。未生不可忌，已死不可阻。死生非远也，理不可睹。或之使，莫之为，疑之所假。吾观之本，其往无穷；吾求之末，其来无止。无穷无止，言之无也，与物同理。或使莫为，言之本也，与物终始。道不可有，有不可无。道之为名，所假而行。或使莫为，在物一曲，夫胡为于大方！言而足，则终日言而尽道；言而不足，则终日言而尽物。道，物之极，言默不足以载。非言非默，议有所极。”

```

外物第二十六

```
外物不可必，故龙逢诛，比干戮，箕子狂，恶来死，桀、纣亡。人主莫不欲其臣之忠，而忠未必信，故伍员流于江，苌弘死于蜀，藏其血三年而化为碧。人亲莫不欲其子之孝，而孝未必爱，故孝己忧而曾参悲。木与木相摩则然，金与火相守则流，阴阳错行，则天地大骇，于是乎有雷有霆，水中有火，乃焚大槐。有甚忧两陷而无所逃。混沌不得成，心若县于天地之间，慰愍沈屯，利害相摩，生火甚多，众人焚和，月固不胜火，于是乎有溃然而道尽。

庄周家贫，故往贷粟于监河侯。监河侯曰：“诺。我将得邑金，将贷子三百金，可乎？”庄周忿然作色曰：“周昨来，有中道而呼者，周顾视车辙，中有鲋鱼焉。周问之曰：‘鲋鱼来，子何为者耶？’对曰：‘我，东海之波臣也。君岂有斗升之水而活我哉！’周曰：‘诺，我且南游吴越之王，激西江之水而迎子，可乎？’鲋鱼忿然作色曰：‘吾失我常与，我无所处。吾得斗升之水然活耳。君乃言此，曾不如早索我于枯鱼之肆。’”

任公子为大钩巨缁，五十害以为饵，蹲乎会稽，投竿东海，旦旦而钓，期年而不得鱼。已而大鱼食之，牵巨钩，陷没而下，骛扬而奋髻，白波若山，海水震荡，声侔鬼神，惮赫千里。任公子得若鱼，离而腊之，自制河以东，苍梧以北，莫不厌若鱼者。已而后世诠才讽说之徒，皆惊而相告也。夫揭竿累，趋灌渎，守鲵鲋，其于得大鱼难矣！饰小说以干县令，其于大达亦远矣。是以未尝闻任氏之风俗，其不可与经于世亦远矣！

```

儒以《诗》《礼》发冢，大儒胪传曰：“东方作矣，事之若何？”小儒曰：“未解裙襦，口中有珠。”“《诗》固有之曰：‘青青之麦，生于陵陂。生不布施，死何含珠为？’接其鬓，压其喙，儒以金椎控其颐，徐别其颊，无伤口中珠。”

```
老莱子之弟子出薪，遇仲尼，反以告，曰：“有人于彼，修上而趋下，末偻而后耳，视若营四海，不知其谁氏之子。”老莱子曰：“是丘也，召而来。”仲尼至。曰：“丘，去汝躬矜与汝容知，斯为君子矣。”仲尼揖而退，蹙然改容而问曰：“业可得进乎？”老莱子曰：“夫不忍一世之伤，而骜万世之患。抑固娄邪？亡其略弗及下？惠以欢为骜，终始之丑，中民之行进焉耳！相引以名，相结以隐。与其誉尧而非桀，不知两忘而闭其所誉。反无非伤也，动无非邪也，圣人踌躇以兴事，以每成功。奈何哉，其载焉终矜尔！”

宋元君夜半而梦人被发窥阿门，曰：“予自宰路之渊，予为清江使河伯之所，渔者余且得予。”元君觉，使人占之，曰：“此神龟也。”君曰：“渔者有余且乎？”左右曰：“有。”君曰：“令余且会朝。”明日，余且朝。君曰：“渔何得？”对曰：“且之网得白龟焉，其圆五尺。”君曰：“献若之龟。”龟至，君再欲杀之，再欲活之。心疑，卜之。曰：“杀龟以卜吉。”乃刳龟，七十二钻而无遗荚。仲尼曰：“神龟能见梦于元君，而不能避余且之网；知能七十二钻而无遗荚，不能避刳肠之患。如是则知有所困，神有所不及也。虽有至知，万人谋之。鱼不畏网而畏鹈鹕。去小知而大知明，去善而自善矣。婴儿生，无石师而能言，与能言者处也。”

惠子谓庄子曰：“子言无用。”庄子曰：“知无用而始可与言用矣。天地非不广且大也，人之所用容足耳，然则侧足而垫之，致黄泉，人尚有用乎？”惠子曰：“无用。”庄子曰：“然则无用之为用也明矣。”

庄子曰：“人有能游，且得不游乎！人而不能游，且得游乎！夫流遁之志，决绝之行，噫，其非至知厚德之任与！覆坠而不反，火驰而不顾。虽相与为君臣，时也。易世而无以相贱。故曰：至人不留行焉。夫尊古而卑今，学者之流也。且以烯韦氏之流观今之世，夫孰能不波！唯至人乃能游于世而不僻，顺人而不失己。彼教不学，承意不彼。

目彻为明，耳彻为明，鼻彻为颤，口彻为甘，心彻为知，知彻为德。凡道不欲壅，壅则哽，哽而不止则畛，畛则众害生。物之有知者恃息。其不殷，非天之罪也。天之穿之，日夜无降，人则顾塞其窦。胞有重阆，心有天游。室无空虚，则妇姑勃溪；心无天游，则六凿相攘。大林丘山之善于人也，亦神者不胜。

德溢乎名，名溢乎暴，谋稽乎弦，知出乎争，柴生乎守，官事果乎众宜。春雨日时，草木怒生，钱缛于是乎始修，草木之倒植者过半，而不知其然。

静默可以补病，髭灭可以休老，宁可以止遽。虽然，若是劳者之务也，非佚者之所未尝过而问焉；圣人之所以戒夭下，神人未尝过而问焉；贤人所以戒世，圣人未尝过而问焉；君子所以戒国，贤人未尝过而问焉；小人所以合时，君子未尝过而问焉。”

```

演门有亲死者，以善毁爵为官师，其党人毁而死者半。尧与许由天下，许由逃之；汤与务光天下，务光怒之；纪他闻之，帅弟子而浚于款水，诸侯吊之。三年，申徒狄因以仆河。

```
筌者所以在鱼，得鱼而忘筌；蹄者所以在兔，得兔而忘蹄；言者所以在意，得意而忘言。吾安得夫忘言之人而与之言哉！

```

寓言第二十七

```
寓言十九，重言十七，卮言日出，和以天倪。寓言十九，藉外论之。亲父不为其子媒，亲父誉之，不若非其父者也。非吾罪也，人之罪也。与己同则应，不与己同则反。同于己为是之，异于己为非之。重言十七，所以已言也。是为耆艾，年先矣，而无经纬本末以期年耆者，是非先也。人而无以先人，无人道也。人而无人道，是之谓陈人。卮言日出，和以天倪，因以曼衍，所以穷年。不言则齐，齐与言不齐，言与齐不齐也。故曰无言。言无言：终始言，未尝言；终始不言，未尝不言。有自也而可，有自也而不可；有自也而然，有自也而不然。恶乎可？可于可；恶乎不可？不可于不可。物固有所然，物固有所可。无物不然，无物不可。非卮言日出，和以天倪，孰得其久！万物皆种也，以不同形相禅，始卒若环，莫得其伦，是谓天均。天均者，天倪也。

庄子谓惠子曰：“孔子行年六十而六十化。始时所是，卒而非之。未知今之所谓是之非五十九年非也。”惠子曰：“孔子勤志服知也。”庄子曰：“孔子谢之矣，而其未之尝言。孔子云：夫受才乎大本，复灵以生。鸣而当律，言而当法。利义陈乎前，而好恶是非直服人之口而已矣。使人乃以心服而不敢噩，立定天下之定。已乎，已乎！吾且不得及彼乎！”

曾子再仕而心再化，曰：“吾及亲仕，三釜而心乐；后仕，三千钟而不洎，吾心悲。”弟子问于仲尼曰：“若参者，可谓无所县其罪乎？”曰：“既已县矣！夫无所县者，可以有哀乎？彼视三釜、三千钟，如观雀蚁蚊虻相过乎前也。”

颜成子游谓东郭子綦曰：“自吾闻子之言，一年而野，二年而从，三年而通，四年而物，五年而来，六年而鬼入，七年而天成，八年而不知死、不知生，九年而大妙。

“生，有为，死也。劝公以其死也有自也，而生阳也，无自也。而果然乎？恶乎其所适，恶乎其所不适？天有历数，地有人据，吾恶乎求之？莫知其所终，若之何其无命也？莫知其所始，若之何其有命也？有以相应也，若之何其无鬼邪？无以相应也，若之何其有鬼邪？”

众罔两问于景曰：“若向也俯而今也仰，向也括而今也被发；向也坐而今也起；向也行而今也止：何也？”景曰：“叟叟也，奚稍问也！予有而不知所以。予，蜩甲也，蛇蜕也，似之而非也。火与日，吾屯也；阴与夜，吾代也。彼，吾所以有待邪，而况乎以有待者乎！彼来则我与之来，彼往则我与之往，彼强阳则我与之强阳。强阳者，又何以有问乎！”

阳子居南之沛，老聃西游于秦。邀于郊，至于梁而遇老子。老子中道仰天而叹曰：“始以汝为可教，今不可也。”阳子居不答。至舍，进盥漱巾栉，脱履户外，膝行而前，曰：“向者弟子欲请夫子，夫子行不闲，是以不敢；今闲矣，请问其过。”老子曰：“而雎雎盯盯，而谁与居！大白若辱，盛德若不足。”阳子居蹴然变容曰：“敬闻命矣！”其往也，舍者迎将，其家公执席，妻执巾栉，舍者避席，炀者避灶。其反也，舍者与之争席矣！

```

让王第二十八
------

尧以天下让许由，许由不受。又让子州支伯，子州支伯曰：“以我为天子，犹之可也。虽然，我适有幽忧之病，方且治之，未暇治天下也。”夫天下至重者也，而不以害其生，又况他物乎！唯无以天下为者可以托天下也。舜让天下于子州支伯，子州支伯曰：“予适有幽忧之病，方且治之，未暇治天下也。”故天下大器也，而不以易生。此有道者之所以异乎俗者也，舜以天下让善卷，善卷曰：“余立于宇宙之中，冬日衣皮毛，夏日衣葛希。春耕种，形足以劳动；秋收敛，身足以休食。日出而作，日入而息，逍遥于天地之间，而心意自得。吾何以天下为哉！悲夫，子之不知余也。”遂不受。于是去而入深山，莫知其处。舜以天下让其友石户之农。石户之农曰：“卷卷乎后之为人，葆力之士也。”以舜之德为未至也。于是夫负妻戴，携子以入于海，终身不反也。

大王檀父居豳，狄人攻之。事之以皮帛而不受，事之以犬马而不受，事之以珠玉而不受。狄人之所求者土地也。大王檀父曰：“与人之兄居而杀其弟，与人之父居而杀其子，吾不忍也。子皆勉居矣！为吾臣与为狄人臣奚以异。且吾闻之：不以所用养害所养。”因杖荚而去之。民相连而从之。遂成国于岐山之下。夫大王檀父可谓能尊生矣。能尊生者，虽贵富不以养伤身，虽贫贱不以利累形。今世之人居高官尊爵者，皆重失之。见利轻亡其身，岂不惑哉！

越人三世弑其君，王子搜患之，逃乎丹穴，而越国无君。求王子搜而不得，从之丹穴。王子搜不肯出，越人薰之以艾。乘以王舆。王予搜援绥登车，仰天而呼曰：“君乎，君乎，独不可以舍我乎！”王子搜非恶为君也，恶为君之患也。若王子搜者，可谓不以国伤生矣！此固越人之所欲得为君也。

韩魏相与争侵地，子华子见昭僖侯，昭僖侯有忧色。子华子曰：“今使天下书铭于君之前，书之言曰：‘左手攫之则右手废，右手攫之则左手废。然而攫之者必有天下。’君能攫之乎？”昭僖侯曰：“寡人不攫也。”子华子曰：“甚善！自是观之，两臂重于天下也。身亦重于两臂。韩之轻于天下亦远矣！今之所争者，其轻于韩又远。君固愁身伤生以忧戚不得也。”僖侯曰：“善哉！教寡人者众矣，未尝得闻此言也。”子华子可谓知轻重矣！

鲁君闻颜阖得道之人，使人以币先焉。颜阖守陋闾，苴布之衣，而自饭牛。鲁君之使者至，颜阖自对之。使者曰：“此颜阖之家与？”颜阖对曰：“此阖之家也。”使者致币。颜阖对曰：“恐听者谬而遗使者罪，不若审之。”使者还，反审之，复来求之，则不得已！故若颜阖者，真恶富贵也。

故曰：道之真以治身，其绪余以为国家，其土苴以治天下。由此观之，帝王之功，圣人之余事也，非所以完身养生也。今世俗之君子，多为身弃生以殉物，岂不悲哉！凡圣人之动作也，必察其所以之与其所以为。今且有人于此，以随侯之珠，弹千仞之雀，世必笑之。是何也？则其所用者重而所要者轻也。夫生者岂特随侯之重哉？

子列子穷，容貌有饥色。客有言之于郑子阳者，曰：“列御寇，盖有道之士也，居君之国而穷，君无乃为不好士乎？”郑子阳即令官遗之粟。子列子见使者，再拜而辞。使者去，子列子入，其妻望之而拊心曰：“妾闻为有道者之妻子，皆得佚乐。今有饥色，君过而遗先生食，先生不受，岂不命邪？”子列子笑，谓之曰：“君非知我也，以人之言而遗我粟；至其罪我也，又且以人之言，此吾所以不受也。”其卒，民果作难而杀子阳。

楚昭王失国，屠羊说走而从于昭王。昭王反国，将赏从者，及屠羊说。屠羊说曰：“大王失国，说失屠羊。大王反国，说已反屠羊。臣之爵禄已复矣，又何赏之言。”王曰：“强之。”屠羊说曰：“大王失国，非臣之罪，故不敢伏其诛；大王反国，非臣之功，故不敢当其赏。”王曰：“见之。”屠羊说曰：“楚国之法，必有重赏大功而后得见。今臣之知不足以存国，而勇不足以死寇。吴军入郢，说畏难而避寇，非故随大王也。今大王欲废法毁约而见说，此非臣之所以闻于天下也。”王谓司马子綦曰：“屠羊说居处卑贱而陈义甚高，子其为我延之以三旌之位。”屠羊说曰：“夫三旌之位，吾知其贵于屠羊之肆也；万钟之禄，吾知其富于屠羊之利也。然岂可以贪爵禄而使吾君有妄施之名乎？说不敢当，愿复反吾屠羊之肆。”遂不受也。

原宪居鲁，环堵之室，茨以生草，蓬户不完，桑以为枢而瓮牖，二室褐以为塞，上漏下湿，匡坐而弦。子贡乘大马，中绀而表素，轩车不容巷，往见原宪。原宪华冠蔽履，杖藜而应门。子贡曰：“嘻！先生何病？”原宪应之曰：“宪闻之，无财谓之贫，学而不能行谓之病。今宪贫也，非病也。”子贡逡巡而有愧色。原宪笑曰：“夫希世而行，比周而友，学以为人，教以为己，仁义之慝，舆马之饰，宪不忍为也。”

曾子居卫，蕴袍无表，颜色肿哙，手足胼骶，三日不举火，十年不制衣。正冠而缨绝，捉矜而肘见，纳履而踵决。曳履而歌《商颂》，声满天地，若出金石。天子不得臣，诸侯不得友。故养志者忘形，养形者忘利，致道者忘心矣。

孔子谓颜回曰：“回，来！家贫居卑，胡不仕乎？”颜回对曰：“不愿仕。回有郭外之田五十亩，足以给邗粥；郭内之田十亩，足以为丝麻；鼓琴足以自娱；所学夫子之道者足以自乐也。回不愿仕。”孔子湫然变容，曰：“善哉，回之意！丘闻之：‘知足者，不以利自累也；审自得者，失之而不惧；行修于内者，无位而不作。’丘诵之久矣，今于回而后见之，是丘之得也。”

中山公子牟谓瞻子曰：“身在江海之上，心居乎魏阙之下，奈何？”瞻子曰：“重生。重生则利轻。”中山公子牟曰：“虽知之，未能自胜也。”瞻子曰：“不能自胜则从，神无恶乎！不能自胜而强不从者，此之谓重伤。重伤之人，无寿类矣！”魏牟，万乘之公子也，其隐岩穴也，难为于布衣之士，虽未至乎道，可谓有其意矣！

孔子穷于陈蔡之间，七日不火食，藜羹不糁，颜色甚惫，而弦歌于室。颜回择菜，子路、子贡相与言曰：“夫子再逐于鲁，削迹于卫，伐树于宋，穷于商周，围于陈蔡。杀夫子者无罪，藉夫子者无禁。弦歌鼓琴，未尝绝音，君子之无耻也若此乎？”颜回无以应，入告孔子。孔子推琴，喟然而叹曰：“由与赐，细人也。召而来，吾语之。”子路、子贡入。子路曰：“如此者，可谓穷矣！”孔子曰：“是何言也！君子通于道之谓通，穷于道之谓穷。今丘抱仁义之道以遭乱世之患，其何穷之为？故内省而不穷于道，临难而不失其德。天寒既至，霜露既降，吾是以知松柏之茂也。陈蔡之隘，于丘其幸乎。”孔子削然反琴而弦歌，子路戚然执干而舞。子贡曰：“吾不知天之高也，地之下也。”古之得道者，穷亦乐，通亦乐，所乐非穷通也。道德于此，则穷通为寒暑风雨之序矣。故许由娱语颍阳，而共伯得乎求首。

舜以天下让其友北人无择，北人无择曰：“异哉，后之为人也，居于畎亩之中，而游尧之门。不若是而已，又欲以其辱行漫我。吾羞见之。”因自投清泠之渊。

汤将伐桀，因卞随而谋，卞随曰：“非吾事也。”汤曰：“孰可？”曰：“吾不知也。”汤又因瞀光而谋，瞀光曰：“非吾事也。”汤曰：“孰可？”曰：“吾不知也。”汤曰：“伊尹何如？”曰：“强力忍垢，吾不知其他也。”汤遂与伊尹谋伐桀，克之。以让卞随，卞随辞曰：“后之伐桀也谋乎我，必以我为贼也；胜桀而让我，必我为贪也。吾生乎乱世，而无道之人再来漫我以其辱行，吾不忍数闻也！”乃自投稠水而死。汤又让瞀光，曰：“知者谋之，武者遂之，仁者居之，古之道也。吾子胡不立乎？”瞀光辞曰：“废上，非义也；杀民，非仁也；人犯其难，我享其利，非廉也。吾闻之曰：‘非其义也，不受其禄；无道之世，不践其土。’况尊我乎！吾不忍久见也。”乃负石而自沈于庐水。

昔周之兴，有士二人处于孤竹，曰伯夷、叔齐。二人相谓曰：“吾闻西方有人，似有道者，试往观焉。”至于岐阳，武王闻之，使叔旦往见之。与盟曰：“加富二等，就官一列。”血牲而埋之。二人相视而笑，曰：“嘻，异哉！此非吾所谓道也。昔者神农之有天下也，时祀尽敬而不祈喜；其于人也，忠信尽治而无求焉。乐与政为政，乐与治为治。不以人之坏自成也，不以人之卑自高也，不以遭时自利也。今周见殷之乱而遽为政，上谋而下行货，阻兵而保威，割牲而盟以为信，扬行以悦众，杀伐以要利。是推乱以易暴也。吾闻古之士，遭治世不避其任，遇乱世不为苟存。今天下暗，周德衰，其并乎周以涂吾身也，不如避之，以挈吾行。”二子北至于首阳之山，遂饿而死焉，若伯夷、叔齐者，其于富贵也，苟可得已，则必不赖。高节戾行，独乐其志，不事于世。此二士之节也。

盗跖第二十九
------

孔子与柳下季为友，柳下季之弟名曰盗跖。盗跖从卒九千人，横行天下，侵暴诸侯。穴室枢户，驱人牛马，取人妇女。贪得忘亲，不顾父母兄弟，不祭先祖。所过之邑，大国守城，小国入保，万民苦之。孔子谓柳下季曰：“夫为人父者，必能诏其子；为人兄者，必能教其弟。若父不能诏其子，兄不能教其弟，则无贵父子兄弟之亲矣。今先生，世之才士也，弟为盗跖，为天下害，而弗能教也，丘窃为先生羞之。丘请为先生往说之。”柳下季曰：“先生言为人父者必能诏其子，为人兄者必能教其弟，若子不听父之诏，弟不受兄之教，虽今先生之辩，将奈之何哉？且跖之为人也，心如涌泉，意如飘风，劲足以距敌，辩足以饰非。顺其心则喜，逆其心则怒，易辱人以言。先生必无往。”孔子不听，颜回为御，子贡为右，往见盗跖。

盗跖乃方休卒徒太山之阳，脍人肝而哺之。孔子下车而前，见谒者曰：“鲁人孔丘，闻将军高义，敬再拜谒者。”谒者入通。盗跖闻之大怒，目如明星，发上指冠，曰：“此夫鲁国之巧伪人孔丘非邪？为我告之：尔作言造语，妄称文、武，冠枝木之冠，带死牛之胁，多辞缪说，不耕而食，不织而衣，摇唇鼓舌，擅生是非，以迷天下之主，使天下学士不反其本，妄作孝弟，而侥幸于封侯富贵者也。子之罪大极重，疾走归！不然，我将以子肝益昼哺之膳。”孔子复通曰：“丘得幸子季，愿望履幕下。”谒者复通。盗跖曰：“使来前！”孔子趋而进，避席反走，再拜盗跖。盗跖大怒，两展其足，案剑嗔目，声如乳虎，曰：“丘来前！若所言顺吾意则生，逆吾心则死。”

孔子曰：“丘闻之，凡天下有三德：生而长大，美好无双，少长贵贱见而皆说之，此上德也；知维天地，能辩诸物，此中德也；勇悍果敢，聚众率兵，此下德也。凡人有此一德者，足以南面称孤矣。及将军兼此三者，身长八尺二寸，面目有光，唇如激丹，齿如齐贝，音中黄钟，而名曰盗跖，丘窃为将军耻不取焉。将军有意听臣，臣请南使吴越，北使齐鲁，东使宋卫，西使晋楚，使为将军造大城数百里，立数十万户之邑，尊将军为诸侯，与天下更始，罢兵休卒，收养昆弟，共祭先祖。此圣人才士之行，而天下之愿也。”

盗跖大怒曰：“丘来前！夫可规以利而可谏以言者，皆愚陋恒民之谓耳。今长大美好，人见而悦之者，此吾父母之遗德也。丘虽不吾誉，吾独不自知邪？且吾闻之，好面誉人者，亦好背而毁之。今丘告我以大城众民，是欲规我以利而恒民畜我也，安可久长也！城之大者，莫大乎天下矣。尧、舜有天下，子孙无置锥之地；汤、武而天子，后世绝灭。非以其利大故邪？且吾闻之，古者禽兽多而人少，于是民皆巢居以避之。昼拾橡栗，暮栖木上，故命之曰‘有巢氏之民’。古者民不知衣服，夏多积薪，冬则炀之，故命之曰‘知生之民’。神农之世，卧则居居，起则于于。民知其母，不知其父，与麋鹿共处，耕而食，织而衣，无有相害之心。此至德之隆也。

“然而黄帝不能致德，与蚩尤战于涿鹿之野，流血百里。尧、舜作，立群臣，汤放其主，武王杀纣。自是以后，以强陵弱，以众暴寡。汤、武以来，皆乱人之徒也。今子修文、武之道，掌天下之辩，以教后世。缝衣浅带，矫言伪行，以迷惑天下之主，而欲求富贵焉。盗莫大于子，天下何故不谓子为盗丘，而乃谓我为盗跖？子以甘辞说子路而使从之。使子路去其危冠，解其长剑，而受教于子。天下皆曰‘孔丘能止暴禁非’，其卒之也，子路欲杀卫君而事不成，身沮于卫东门之上，是子教之不至也。子自谓才士圣人邪，则再逐于鲁，削迹于卫，穷于齐，围于陈蔡，不容身于天下。子教子路沮此患，上无以为身，下无以为人，子之道岂足贵邪？

世之所高，莫若黄帝。黄帝尚不能全德，而战涿鹿之野，流血百里。尧不慈，舜不孝，禹偏枯，汤放其主，武王伐纣，文王拘卣里。此六子者，世之所高也。孰论之，皆以利惑其真而强反其情性，其行乃甚可羞也。世之所谓贤士：伯夷、叔齐。伯夷、叔齐辞孤竹之君，而饿死首阳之山，骨肉不葬。鲍焦饰行非世抱木而死。申徒狄谏而不听，负石自投于河，为鱼鳖所食。介子推至忠也，自割其股以食文公。文公后背之，子推怒而去，抱木而播死。尾生与女子期于梁下，女子不来，水至不去，抱梁柱而死。此六子者，无异于桀犬流豕、操瓢而乞者，皆离名轻死，不念本养寿命也。

“士之所谓忠臣者，莫若王子比干、伍子胥。子胥沉江，比干剖心。此二子者，世谓忠臣也，然卒为天下笑。自上观之，至于子胥、比干，皆不足贵也。丘之所以说我者，若告我以鬼事，则我不能知也；若告我以人事者，不过此矣，皆吾所闻知也。今吾告子以人之情：目欲视色，耳欲听声，口欲察味，志气欲盈。人上寿百岁，中寿八十，下寿六十，除病瘦死丧忧患，其中开口而笑者，一月之中不过四五日而已矣。天与地无穷，人死者有时。操有时之具，而托于无穷之间，忽然无异骐骥之驰过隙也。不能说其志意、养其寿命者，皆非通道也。丘之所言，皆吾之所弃也。亟去走归，无复言之！子之道狂况汲汲，诈巧虚伪事也，非可以全真也，奚足论哉！”

孔子再拜趋走，出门上车，执辔三失，目芒然无见，色若死灰，据轼低头，不能出气。归到鲁东门外，适遇柳下季。柳下季曰：“今者阙然，数日不见，车马有行色，得微往见跖邪？”孔子仰天而叹曰：“然！”柳下季曰：“跖得无逆汝意若前乎？”孔子曰：“然。丘所谓无病而自灸也。疾走料虎头，编虎须，几不免虎口哉！”

子张问于满苟得曰：“盍不为行？无行则不信，不信则不任，不任则不利。故观之名，计之利，而义真是也。若弃名利，反之于心，则夫士之为行，不可一日不为乎！”满苟得曰：“无耻者富，多信者显。夫名利之大者，几在乎无耻而信。故观之名，计之利，而信真是也。若弃名利，反之于心，则夫士之为行，抱其天乎！”子张曰：“昔者桀、纣贵为天子，富有天下。今谓臧聚曰：‘汝行如桀、纣。’则有作色，有不服之心者，小人所贱也。仲尼、墨翟，穷为匹夫，今谓宰相曰：‘子行如仲尼、墨翟。’则变容易色，称不足者，士城贵也。故势为天子，未必贵也；穷为匹夫，未必贱也。贵贱之分，在行之美恶。”满苟得曰：“小盗者拘，大盗者为诸侯。诸侯之门，义士存焉。昔者桓公小白杀兄入嫂，而管仲为臣；田成子常杀君窃国，而孔子受币。论则贱之，行则下之，则是言行之情悖战于胸中也，不亦拂乎！故《书》曰：‘孰恶孰美，成者为首，不成者为尾。’”

子张曰：“子不为行，即将疏戚无伦，贵贱无义，长幼无序。五纪六位，将何以为别乎？”满苟得曰：“尧杀长子，舜流母弟，疏戚有伦乎？汤放桀，武王杀纣，贵贱有义乎？王季为适，周公杀兄，长幼有序乎？儒者伪辞，墨子兼爱，五纪六位，将有别乎？且子正为名，我正为利。名利之实，不顺于理，不监于道。吾日与子讼于无约，曰：‘小人殉财，君子殉名，其所以变其情、易其性则异矣：乃至于弃其所为而殉其所不为，则一也。’故曰：无为小人，反殉而天；无为君子，从天之理。若枉若直，相而天极。面观四方，与时消息。若是若非，执而圆机。独成而意，与道徘徊。无转而成，将弃而天。比干剖心，子胥抉眼，忠之祸也；直躬证父，尾生溺死，信之患也；鲍子立干，申子不自理，廉之害也；孔子不见母，匡子不见父，义之失也。此上世之所传、下世之所语以为士者，正其言，必其行，故服其殃、离其患也。”

无足问于知和曰：“人卒未有不兴名就利者。彼富则人归之，归则下之，下则贵之。夫见下贵者，所以长生安体乐意之道也。今子独无意焉，知不足邪？意知而力不能行邪？故推正不忘邪？”知和曰：“今夫此人，以为与己同时而生，同乡而处者，以为夫绝俗过世之士焉，是专无主正，所以览古今之时、是非之分也。与俗化世，去至重，弃至尊，以为其所为也。此其所以论长生安体乐意之道，不亦远乎！惨惮之疾，恬愉之安，不监于体；怵惕之恐，欣欢之喜，不监于心。知为为而不知所以为。是以贵为天子，富有天下，而不免于患也。”

无足曰：“夫富之于人，无所不利。穷美究执，至人之所不得逮，贤人之所不能及。侠人之勇力而以为威强，秉人之知谋以为明察，因人之德以为贤良，非享国而严若君父。且夫声色滋味权势之于人，心不待学而乐之，体不待象而安之。夫欲恶避就，固不待师，此人之性也。天下虽非我，孰能辞之！”知和曰：“知者之为，故动以百姓，不违其度，是以足而不争，无以为故不求。不足故求之，争四处而不自以为贪；有余故辞之，弃天下而不自以为廉。廉贪之实，非以迫外也，反监之度。势为天子，而不以贵骄人；富有天下，而不以财戏人。计其患，虑其反，以为害于性，故辞而不受也。非以要名誉也。尧、舜为帝而雍，非仁天下也，不以美害生；善尧、许由得帝而不受，非虚辞让也，不以事害己。此皆就其利、辞其害，而天下称贤焉，则可以有之，彼非以兴名誉也。”

无足曰：“必持其名，苦体绝甘，约养以持生，则亦久病长厄而不死者也。”知和曰：“平为福，有余为害者，物莫不然，而财其甚者也。今富人耳营钟鼓管龠之声，口慊于刍豢鹨醴之味，以感其意，遗忘其业，可谓乱矣；骇溺于冯气，若负重行而上也，可谓苦矣；贪财而取慰，贪权而取竭，静居则溺，体泽则冯，可谓疾矣；为欲富就利，故满若堵耳而不知避，且冯而不舍，可谓辱矣；财积而无用，服膺而不舍，满心戚醮，求益而不止，可谓忧矣；内则疑劫请之贼，外则畏寇盗之害，内周楼疏，外不敢独行，可谓畏矣。此六者，天下之至害也，皆遗忘而不知察。及其患至，求尽性竭财单以反一日之无故，而不可得也。故观之名则不见，求之利则不得。缭意体而争此，不亦惑乎！”

说剑第三十
-----

昔赵文王喜剑，剑士夹门而客三千余人，日夜相击于前，死伤者岁百余人。好之不厌。如是三年，国衰。诸侯谋之。太子悝患之，募左右曰：“孰能说王之意止剑士者，赐之千金。”左右曰：“庄子当能。”太子乃使人以千金奉庄子。庄子弗受，与使者俱往，见太子曰：“太子何以教周，赐周千金？”太子曰：“闻夫子明圣，谨奉千金，以币从者。夫子弗受，悝尚何敢言。”庄子曰：“闻太子所欲用周者，欲绝王之喜好也。使臣上说大王，而逆王意，下不当太子，则身刑而死，周尚安所事金乎？使臣上说大王，下当太子，赵国何求而不得也！”太子曰：“然。吾王所见，唯剑士也。”庄子曰：“喏。周善为剑。”太子曰：“然吾王所见剑士，皆蓬头，突鬓，垂冠，曼胡之缨，短后之衣，嗔目而语难，王乃悦之。今夫子必儒服而见王，事必大逆。”庄子曰：“请治剑服。”治剑服三日，乃见太子。太子见与见王。王脱白刃待之。庄子入殿门不趋，见王不拜。王曰：“子欲何以教寡人，使太子先。”曰：“臣闻大王喜剑，故以剑见王。”王曰：“子之剑何能禁制？”曰：“臣之剑十步一人，千里不留行。”王大悦之，曰：“天下无敌矣。”庄子曰：“夫为剑者，示之以虚，开之以利，后之以发，先之以至。愿得试之。”王曰：“夫子休，就舍待命，令设戏，请夫子。”

王乃校剑士七日，死伤者六十余人，得五六人，使奉剑于殿下，乃召庄子。王曰：“今日试使士敦剑。”庄子曰：“望之久矣！”王曰：“夫子所御杖，长短何如？”曰：“臣之奉皆可。然臣有三剑，唯王所用。请先言而后试。”王曰：“愿闻三剑。”曰：“有天子剑，有诸侯剑，有庶人剑。”王曰：“天子之剑何如？”曰：“天子之剑，以燕溪石城为锋，齐岱为锷，晋魏为脊，周宋为镡，韩魏为铗，包以四夷，裹以四时，绕以渤海，带以常山，制以五行，论以刑德，开以阴阳，持以春夏，行以秋冬。此剑直之无前，举之无上，案之无下，运之无旁。上决浮云，下绝地纪。此剑一用，匡诸侯，天下服矣。此天子之剑也。”文王芒然自失，曰：“诸侯之剑何如？”曰：“诸侯之剑，以知勇士为锋，以清廉士为锷，以贤良士为脊以忠圣士为镡，以豪杰士为夹。此剑直之亦无前，举之亦无上，案之亦无下，运之亦无旁。上法圆天，以顺三光；下法方地，以顺四时；中和民意，以安四乡。此剑一用，如雷霆之震也，四封之内，无不宾服而听从君命者矣。此诸侯之剑也。”王曰：“庶人之剑何如？”曰：“庶人之剑，蓬头突鬓，垂冠，曼胡之缨，短后之衣，嗔目而语难，相击于前，上斩颈领，下决肝肺。此庶人之剑，无异于斗鸡，一旦名已绝矣，无所用于国事。今大王有天子之位而好庶人之剑，臣窃为大王薄之。”王乃牵而上殿，宰人上食，王三环之。庄子曰：“大王安坐定气，剑事已毕奏矣！”于是文王不出宫三月，剑士皆服毙其处也。

渔父第三十一
------

孔子游乎缁帷之林，休坐乎杏坛之上。弟子读书，孔子弦歌鼓琴。奏曲未半，有渔父者，下船而来，鬓眉交白，被发揄袂，行原以上，距陆而止，左手据膝，右手持颐以听。曲终而招子贡、子路二人俱对。客指孔子曰：“彼何为者也？”子路对曰：“鲁之君子也。”客问其族。子路对曰：“族孔氏。”客曰：“孔氏者何治也？”子路未应，子贡对曰：“孔氏者，性服忠信，身行仁义，饰礼乐，选人伦。上以忠于世主，下以化于齐民，将以利天下。此孔氏之所以治也。”又问曰：“有土之君与？”子贡曰：“非也。”“侯王之佐与？”子贡曰：“非也。”客乃笑而还行，言曰：“仁则仁矣，恐不免其身。苦心劳形，以危其真。呜呼！远哉，其分于道也。”

子贡还，报孔子。孔子推琴而起，曰：“其圣人与？”乃下求之，至于泽畔，方将杖弩而引其船，顾见孔子，还乡而立。孔子反走，再拜而进。客曰：“子将何求？”孔子曰：“曩者先生有绪言而去，丘不肖，未知所谓，窃待于下风，幸闻咳唾之音，以卒相丘也。”客曰：“嘻！甚矣，子之好学也！”孔子再拜而起，曰：“丘少而修学，以至于今，六十九岁矣，无所得闻至教，敢不虚心！”

客曰：“同类相从，同声相应，固天之理也吾请释吾之所有而经子之所以。子之所以者，人事也。天子诸侯大夫庶人，此四者自正，治之美也：四者离位而乱莫大焉。官治其职，人忧其事，乃无所陵。故田荒室露，衣食不足，征赋不属，妻妾不和，长少无序，庶人之忧也；能不胜任，官事不治，行不清白，群下荒怠，功美不有，爵禄不恃，大夫之忧也；廷无忠臣，国家昏乱，工技不巧，贡职不美，春秋后伦，不顺天子，诸侯之忧也；阴阳不和，寒暑不时，以伤庶物，诸侯暴乱，擅相攘伐，以残民人，礼乐不节，财用穷匮，人伦不饬，百姓淫乱，天下有司之忧也。今子既上无君侯有司之势，而下无大臣职事之官，而擅饰礼乐，选人伦，以化齐民，不泰多事乎？且人以八疵，事有四患，不可不察也。非其事而事之，谓之偬；莫之顾而进之，谓之佞；希意道言，谓之谄；不择是非而言，谓之谀；好言人之恶，谓之谗；析交离亲，谓之贼；称誉诈伪以败恶人，谓之慝；不择善否，两容颜适，偷拔其所欲，谓之险。此八疵者，外以乱人，内以伤身，君子不友，明君不臣。所谓四患者：好经大事，变更易常，以挂功名，谓之叨；专知擅事，侵人自用，谓之贪；见过不更，闻谏愈甚，谓之很；人同于己则可，不同于己，虽善不善，谓之矜。此四患也。能去八疵，无行四患，而始可教已。”

孔子啾然而叹，再拜而起，曰：“丘再逐于鲁，削迹于卫，伐树于宋，围于陈蔡。丘不知所失，而离此四谤者，何也？”客凄然变容曰：“甚矣，子之难悟也！人有畏影恶迹而去之走者，举足愈数而迹愈多，走愈疾而影不离身，自以为尚迟，疾走不休，绝力而死。不知处阴以休影，处静以息迹，愚亦甚矣！子审仁义之间，察同异之际，观动静之变，适受与之度，理好恶之情，和喜怒之节，而几于不免矣。谨修而身，慎守其真，还以物与人，则无所累矣。今不修之身而求之人，不亦外乎！”

孔子啾然曰：“请问何谓真？”客曰：“真者，精诚之至也。不精不诚，不能动人。故强哭者，虽悲不哀；强怒者，虽严不威；强亲者，虽笑不和。真悲无声而哀，真怒未发而威，真亲未笑而和。真在内者，神动于外，是所以贵真也。其用于人理也，事亲则慈孝，事君则忠贞，饮酒则欢乐，处丧则悲哀。忠贞以功为主，饮酒以乐为主，处丧以哀为主，事亲以适为主。功成之美，无一其迹矣；事亲以适，不论所以矣；饮酒以乐，不选其具矣；处丧以哀，无问其礼矣。礼者，世俗之所为也；真者，所以受于天也，自然不可易也。故圣人法天贵真，不拘于俗。愚者反此。不能法天而恤于人，不知贵真，禄禄而受变于俗，故不足。惜哉，子之早湛于人伪而晚闻大道也！”孔子又再拜而起曰：“今者丘得遇也，若天幸然。先生不羞而比之服役而身教之。敢问舍所在也，请因受业而卒学大道。”客曰：“吾闻之，可与往者，与之至于妙道；不可与往者，不知其道。慎勿与之，身乃无咎。子勉之，吾去子矣，吾去子矣！”乃刺船而去，延缘苇间。

颜渊还车，子路授绥，孔子不顾，待水波定，不闻弩声而后敢乘。子路旁车而问曰：“由得为役久矣，未尝见夫子遇人如此其威也。万乘之主，千乘之君，见夫子万乘不分庭抗礼，夫子犹有倨傲之容。今渔父杖弩逆立，而夫子曲要磬折，言拜而应，得无太甚乎！门人皆怪夫子矣，渔人何以得此乎！”孔子伏轼而叹，曰：“甚矣，由之难化也！湛于礼仪有间矣，而朴鄙之心至今未去。进，吾语汝：夫遇长不敬，失礼也；见贤不尊，不仁也。彼非至人，不能下人。下人不精，不得其真，故长伤身。惜哉！不仁之于人也，祸莫大焉，而由独擅之。且道者，万物之所由也。庶物失之者死，得之者生。为事逆之则败，顺之则成。故道之所在，圣人尊之。今渔父之道，可谓有矣，吾敢不敬乎！”

列御寇第三十二
-------

列御寇之齐，中道而反，遇伯昏瞀人。伯昏瞀人曰：“奚方而反？”曰：“吾惊焉。”曰：“恶乎惊？”曰：“吾尝食于十浆而五浆先馈。”伯昏瞀人曰：“若是则汝何为惊已？”曰：“夫内诚不解，形喋成光，以外镇人心，使人轻乎贵老，而赍其所患。夫浆人特为食羹之货，多于之赢，其为利也薄，其为权也轻，而犹若是，而况于万乘之主乎！身劳于国而知尽于事。彼将任我以事，而效我以功。吾是以惊。”伯昏瞀人曰：“善哉观乎！汝处己，人将保汝矣！”无几何而往，则户外之履满矣。伯昏瞀人北面而立，敦杖，蹙之乎颐。离有间，不言而出。宾者以告列子，列子提履，跣而走，暨乎门，曰：“先生既来，曾不发药乎？”曰：“已矣，吾固告汝曰：人将保汝。果保汝矣！非汝能使人保汝，而汝不能使人无保汝也，而焉用之感豫出异也。必且有感，摇而本性，又无谓也。与汝游者，又莫汝告也。彼所小言，尽人毒也。莫觉莫悟，何相孰也，巧者劳而知者忧，无能者无所求，饱食而敖游，泛若不系之舟，虚而敖游者也！”

郑人缓也，呻吟裘氏之地。只三年而缓为儒。河润九里，泽及三族，使其弟墨。儒墨相与辩，其父助翟。十年而缓自杀。其父梦之曰：“使而子为墨者，予也，阖胡尝视其良？既为秋柏之实矣。”夫造物者之报人也，不报其人而报其人之天，彼故使彼。夫人以已为有以异于人，以贱其亲。齐人之井饮者相啐也。故曰：今之世皆缓也。自是有德者以不知也，而况有道者乎！古者谓之遁天之刑。圣人安其所安，不安其所不安；众人安其所不安，不安其所安。

庄子曰：“知道易，勿言难。知而不言，所以之天也。知而言之，所以之人也。古之人，天而不人。朱坪慢学屠龙于支离益，单千金之家，三年技成而无所用其巧。圣人以必不必，故无兵；众人以不必必之，故多兵。顺于兵，故行有求。兵，恃之则亡。小夫之知，不离苞苴竿牍，敝精神乎蹇浅，而欲兼济导物，太一形虚。若是者，迷惑于宇宙形累，不知太初。彼至人者，归精神乎无始，而甘瞑乎无何有之乡。水流乎无形，发泄乎太清。悲哉乎！汝为知在毫毛，而不知大宁。”

宋人有曹商者，为宋王使秦。其往也，得车数乘。王说之，益车百乘。反于宋，见庄子，曰：“夫处穷间厄巷，困窘织履，槁项黄首者，商之所短也；一悟万乘之主，而从车百乘者，商之所长也。”庄子曰：“秦王有病召医。破痈溃痤者得车一乘，舐痔者得车五乘，所治愈下，得车愈多。子岂治其痔邪？何得车之多也？子行矣！”

鲁哀公问于颜阖曰：“吾以仲尼为贞干，国其有瘳乎？”曰：“殆哉圾乎！仲尼方且饰羽而画，从事华辞。以支为旨，忍性以视民，而不知不信。受乎心，宰乎神，夫何足以上民！彼宜女与予颐与？误而可矣！今使民离实学伪，非所以视民也。为后世虑，不若休之。难治也！”施于人而不忘，非天布也，商贾不齿。虽以事齿之，神者勿齿。为外刑者，金与木也；为内刑者，动与过也。宵人之离外刑者，金木讯之；离内刑者，阴阳食之。夫免乎外内之刑者，唯真人能之。

孔子曰：“凡人心险于山川，难于知无。天犹有春秋冬夏旦暮之期，人者厚貌深情。故有貌愿而益，有长若不肖，有顺怀而达，有坚而缦，有缓而干。故其就义若渴者，其去义若热。故君子远使之而观其忠，近使之而观其敬，烦使之而观其能，卒然问焉而观其知，急与之期而观其信，委之以财而观其仁，告之以危而观其节，醉之以酒而观其则，杂之以处而观其色。九征至，不肖人得矣。”

正考父一命而佝，再命而偻，三命而俯，循墙而走，孰敢不轨！如而夫者，一命而吕巨，再命而于车上舞，三命而名诸父。孰协唐许？贼莫大乎德有心而心又睫，及其有睫也而内视，内视而败矣！凶德有五，中德为首。何谓中德？中德也者，有以自好也，而呲其所不为者。穷有八极，达有三必，形有六府。美、髯、长、大、壮、丽、勇、敢，八者俱过人也，因以是穷；缘循、偃侠、困畏，不若人，三者俱通达；知慧外通，勇动多怨，仁义多责。达生之情者鬼，达于知者肖，达大命者随，达小命者遭。

人有见宋王者，锡车十乘。以其十乘犀庄子。庄子曰：“河上有家贫，恃苇萧而食者，其子投于渊，得千金之珠。其父谓其子曰：‘取石来锻之！夫千金之珠，必在九重之渊而骊龙颔下。子能得珠者，必遭其睡也。使骊龙而寤，子尚奚微之有哉！’今宋国之深，非直九重之渊也；宋王之猛，非直骊龙也。子能得车者，必遭其睡也；使宋王而寤，子为齑粉夫。”

或聘于庄子，庄子应其使曰：“子见夫牺牛乎？衣以文绣，食以刍叔。及其牵而入于太庙，虽欲为孤犊，其可得乎！”庄子将死，弟子欲厚葬之，庄子曰：“吾以天地为棺椁，以日月为连璧，星辰为珠玑，万物为赍送。吾葬具岂不备邪？何以加此！”弟子曰：“吾恐乌鸢之食夫子也。”庄子曰：“在上为乌鸢食，在下为蝼蚁食，夺彼与此，何其偏也。”以不平平，其平也不平；以不征征，其征也不征。明者唯为之使，神者征之。夫明之不胜神也久矣，而愚者恃其所见入于人，其功外也，不亦悲乎！

天下第三十三
------

天下之治方术者多矣，皆以其有为不可加矣！古之所谓道术者，果恶乎在？曰：“无乎不在。”曰：“神何由降？明何由出？”“圣有所生，王有所成，皆原于一。”不离于宗，谓之天人；不离于精，谓之神人；不离于真，谓之至人。以天为宗，以德为本，以道为门，兆于变化，谓之圣人；以仁为恩，以义为理，以礼为行，以乐为和，薰然慈仁，谓之君子；以法为分，以名为表，以操为验，以稽为决，其数一二三四是也，百官以此相齿；以事为常，以衣食为主，蕃息畜藏，老弱孤寡为意，皆有以养，民之理也。古之人其备乎！配神明，醇天地，育万物，和天下，泽及百姓，明于本数，系于末度，六通四辟，小大精粗，其运无乎不在。其明而在数度者，旧法、世传之史尚多有之；其在于《诗》、《书》、《礼》、《乐》者，邹鲁之士、缙绅先生，多能明之。《诗》以道志，《书》以道事、《礼》以道行，《乐》以道和，《易》以道阴阳，《春秋》以道名分。其数散于天下而设于中国者，百家之学时或称道之。

天下大乱，贤圣不明，道德不一。天下多得一察焉以自好。譬如耳目鼻口，皆有所明，不能相通。犹百家众技也，皆有所长，时有所用。虽然不该不遍，一曲之士也。判天地之美，析万物之理，察古人之全。寡能备于天地之美，称神明之容。是故内圣外王之道，黯而不明，郁而不发，天下之人各为其所欲焉以自为方。悲夫！百家往而不反，必不合矣！后世之学者，不幸不见天地之纯，古人之大体。道术将为天下裂。

不侈于后世，不靡于万物，不晖于数度，以绳墨自矫，而备世之急。古之道术有在于是者，墨翟、禽滑离，闻其风而说之。为之太过，已之大循。作为《非乐》，命之曰《节用》。生不歌，死无服。墨子泛爱兼利而非斗，其道不怒。又好学而博，不异，不与先王同，毁古之礼乐。黄帝有《咸池》，尧有《大章》，舜有《大韶》，禹有《大夏》，汤有《大镬》，文王有辟雍之乐，武王、周公作《武》。古之丧礼，贵贱有仪，上下有等。天子棺椁七重，诸侯五重，大夫三重，士再重。今墨子独生不歌，死无服，桐棺三寸而无椁，以为法式。以此教人，恐不爱人；以此自行，固不爱己。未败墨子道。虽然歌而非歌，哭而非哭，乐而非乐，是果类乎？其生也勤，其死也薄，其道大觳。使人忧，使人悲，其行难为也。恐其不可以为圣人之道，反天下之心。天下不堪。墨子虽能独任，奈天下何！离于天下，其去王也远矣！

墨子称道曰：“昔禹之湮洪水，决江河而通四夷九州也。名川三百，支川三千，小者无数。禹亲自操橐耜，而九杂天下之川。腓无跋，胫无毛，沐甚雨，栉疾风，置万国。禹，大圣也。而形劳天下也如此。”使后世之墨者，多以裘褐为衣，以岐峤为服，日夜不休，以自苦为极，曰：“不能如此，非禹之道也，不足谓墨。”相里勤之弟子，五侯之徒，南方之墨者苦获、已齿、邓陵子之属，俱诵《墨经》，而倍谲不同，相谓别墨。以坚白同异之辩相訾，以奇偶不仵之辞相应，以巨子为圣人。皆愿为之尸，冀得为其后世，至今不决。墨翟、禽滑离之意则是，其行则非也。将使后世之墨者，必自苦以腓无跋，胫无毛相进而已矣。乱之上也，治之下也。虽然，墨子真天下之好也，将求之不得也，虽枯槁不舍也，才士也夫！

不累于俗，不饰于物，不苟于人，不歧于众，愿天下之安宁以活民命，人我之养，毕足而止，以此白心。古之道术有在于是者，宋平、尹文闻其风而悦之。作为华山之冠以自表，接万物以别宥为始。语心之容，命之曰：“心之行。”以耳合獾，以调海内。请欲置之以为主。见侮不辱，救民之斗，禁攻也寝兵，救世之战。以此周行天下，上说下教。虽天下不取，强聒而不舍者也。故曰：上下见厌而强见也。虽然，其为人太多，其自为太少，曰：“请欲固置五升之饭足矣。”先生恐不得饱，弟子虽饥，不忘天下，日夜不休。曰：“我必得活哉！”图傲乎救世之士哉！曰：“君子不为苟察，不以身假物。”以为无益于天下者，明之不如已也。以禁攻寝兵为外，以情欲寡浅为内。其小大精粗，其行适至是而止。

公而不当，易而无私，决然无主，趣物而不两，不顾于虑，不谋于知，于物无择，与之俱往。古之道术有在于是者，彭蒙、田骈、慎到，闻其风而悦之。齐万物以为首，曰：“天能覆之而不能载之，地能载之而不能覆之，大道能包之而不能辩之。”知万物皆有所可，有所不可。故曰：“选则不遍，教则不至，道则无遗矣。”是故慎到弃知去己，而缘不得已。泠汰于物，以为道理。曰：“知不知，将薄知而后邻伤之者也。”溪裸无任，而笑天下之尚贤也；纵脱无行，而非天下之大圣；椎拍剜断，与物婉转；舍是与非，苟可以免。不师知虑，不知前后，魏然而已矣。推而后行，曳而后往。若飘风之还，若羽之旋，若磨石之隧，全而无非，动静无过，未尝有罪。是何故？夫无知之物，无建己之患，无用知之累，动静不离于理，是以终身无誉。故曰：“至于若无知之物而已，无用圣贤，夫块不失道。”豪杰相与笑之曰：“慎到之道，非生人之行，而至死人之理，适得怪焉。”田骈亦然，学于彭蒙，得不教焉。彭蒙之师曰：“古之道人，至于莫之是、莫之非而已矣。其风域然，恶可而言。”常反人，不见观，而不免于腕断。其所谓道非道，而所言之韪不免于非。彭蒙、田骈、慎到不知道。虽然，概乎皆尝有闻者也。

以本为精，以物为粗，以有积为不足，澹然独与神明居。古之道术有在于是者，关尹、老聃闻其风而悦之。建之以常、无、有，主之以太一。以濡弱谦下为表，以空虚不毁万物为实。关尹曰：“在己无居，形物自著。其动若水，其静若镜，其应若响。惚乎若亡，寂乎若清。同焉者和，得焉者失。未尝先人而常随人。”老聃曰：“知其雄，守其雌，为天下溪；知其白，守其辱，为天下谷。”人皆取先，己独取后。曰：“受天下之垢。”人皆取实，己独去虚。“无藏也故有余。”岿然而有余。其行身也，徐而不费。无为也而笑巧。人皆求福，己独曲全。曰：“苟免于咎。”以深为根，以约为纪。曰：“坚则毁矣，锐则挫矣。”常宽容于物，不削于人。可谓至极，关尹、老聃乎，古之博大真人哉！

惚漠无形，变化无常，死与？生与？天地并与？神明往与？芒乎何之？忽乎何适？万物毕罗，莫足以归。古之道术有在于是者，庄周闻其风而悦之。以谬悠之说，荒唐之言，无端崖之辞，时恣纵而不傥，不以绮见之也。于天下为沈浊，不可与庄语。以卮言为曼衍，以重言为真，以寓言为广。独与天地精神往来，而不敖倪于万物。不谴是非，以与世俗处。其数虽环玮，而连卞无伤也。其辞虽参差，而叔诡可观。彼其充实，不可以已。上与造物者游，而下与外死生、无终始者为友。其于本也，宏大而辟，深闳而肆；其于宗也，可谓调适而上遂矣。虽然，其应于化而解于物也，其理不竭，其来不蜕，芒乎昧乎，未之尽者。

惠施多方，其书五车，其道桀驳，其言也不中。历物之意，曰：“至大无外，谓之大一；至小无内，谓之小一。无厚不可积也，其大千里。天与地卑，山与泽平。日方中方倪，物方生方死。大同而与小同异，此之谓‘小同异’；万物毕同毕异，此之谓‘大同异’。南方无穷而有穷。今日适越而昔来。连环可解也。我知天之中央，燕之北、越之南是也。泛爱万物，天地一体也。”

惠施以此为大观于天下而晓辩者，天下之辩者相与乐之。卵有毛。鸡三足。郢有天下。犬可以为羊。马有卵。丁子有尾。火不热。山出口。轮不辗地。目不见。指不至，至不绝。龟长于蛇。矩不方，规不可以为圆。凿不围呐。飞鸟之景未尝动也。镞矢之疾，而有不行不止之时。狗非犬。黄马骊牛三。白狗黑。孤驹未尝有母。一尺之捶，日取其半，万世不竭。辩者以此与惠施相应，终始无穷。

桓团、公孙龙辩者之徒，饰人之心，易人之意，能胜人之口，不能服人之心，辩者之囿也。惠施日以其知与人之辩，特与天下之辩者为怪，此其柢也。然惠施之口谈，自以为最贤，曰：“天地其壮乎！”惠施雄而无术。南方有倚人焉，曰黄缭，问天地所以不坠不陷，风雨雷霆之故。惠施不辞而应，不虑而对，遍为万物说。说而不休，多而无已，犹以为寡，益之以怪，以反人为实，而欲以胜人为名，是以与众不适也。弱于德，强于物，其涂澳矣。由天地之道观惠施之能，其犹一蚊一虻之劳者也，其于物也何庸！夫充一尚可曰愈，贵道几矣！惠施不能以此自宁，散于万物而不厌，卒以善辩为名。惜乎，惠施之才！骀荡而不得，逐万物而不反，是穷响以声，形与影竞走也，悲夫！



---


`@bintou`
`2015-10-10 19:48:00`
`字数 1915`
`阅读 2246`


论如何进行高质量吐槽
==========

`吐槽`

---

著名教育家马克吐温曾经说过：如果吐槽有利于身心健康，那么中国人就是世界上最健康的人群；如果吐槽可以兴帮，那么中国就是世界最伟大的国度。就连拿破轮子也说了：中国这个东方雄狮啊，千万别让他们吐槽吐起来......话虽这么说，以我浅见，真正有益于身心健康且有助于“修身、齐家、治国、平天下”的是高质量的吐槽。

什么是高质量的吐槽？试举一例，话说宋朝有一清官叫陈世美，他为官清廉、刚正不阿。有一次他严辞拒绝了一位老乡的走后门。他这位老乡啊心中万马奔腾啊，恼火啊，要吐槽！按理他应该在微信朋友圈发个贴把这辈子学过的各种成语喷出去，噼里啪啦。但是，他不，这家伙有文化！他是一个写戏曲的，于是他就编了个故事说啊，有一个状元郎叫陈世美，招了驸马就抛妻弃子，罪恶涛天，最后给包黑子给斩..... 这故事编得好，百姓喜欢不说还深得圣意，结果到处巡回演出，陈世美就出名了，而且这罪名传了上千年，到现在还没平反呢，啥时候需要反贪腐就拿出来演。所以，所谓高质量的吐槽就是编高质量的故事，这样才有益于身心健康，利于国家安全。

说到这，大家该都明白了，为何经历了几千年文明熏陶的中国依然是发展中国家了。“修齐治平”（高质量吐槽）这活儿真不是谁都能干的，要够冷静、要会编故事。我今天就给大家介绍一位吐槽的旷世奇才，他就是大家都听过但是都不怎么了解的庄子。庄子的言论都记录在《庄子》这部书里，满纸荒唐言，到处是槽点啊！以下我们通过《庄子》里面的一些故事来了解一下吐槽的具体操作手法。

首先，我们要知道，庄子此人最痛恨的几大历史人物分别是：尧、舜、禹和孔子！与孔子不同，在《论语》中，每次讲到道家人物的时候孔子都是异常地恭敬、不敢多言。然而，庄子每每讲到尧、舜、禹和孔子的时候多半都是不屑与嘲笑。只是他使用的方式不同，那就是编故事。因此，在《庄子》这本书里面有很多关于孔子的故事，孔子在其中扮演了各种痴呆楞傻邪恶偶尔也有一两次是聪明善良的角色。比如以下这个：

有天，孔子最器重的大弟子颜回屁颠屁颠地跑到孔子面前说，师父师父，我又进步了！哈哈，真够傻的。孔子一脸严肃地问，你进步啥了啊？颜回就答，师父啊，我忘记了仁义道德了！这个世界上最讲仁义道德的大宗师该怒了吧？没有，孔子回答说，哎哟不错嘛，不过还有进步空间。又过两天，颜回又跑来了说，老师老师，我又进步了！孔子问，你又怎么了？颜回说，我忘记礼乐了！反了你，难道这弟子不知道“礼乐”是师父修订过最重要的专著，还等着靠它评院士呢？孔子答，嗯，哎哟不错嘛，不过还有进步空间。第三次，颜回又来说自己进步了，好烦啊～孔子又问你咋了，颜回说，我**坐忘**了！孔子一听傻了，啥玩意儿叫坐忘，我怎么没听过，你赶紧说来听听。颜回就说：“堕肢体，黜聪明，离形去知，同于大通。此谓坐忘。”这分明是老庄的言论嘛！最后孔子泪流满面地说，哇噻，酷啊，坐忘这家伙好，颜回你小子就是牛就是大圣人啊，不如你做我师父，我跟着你混好了。(注：故事出自《庄子》内篇，大宗师。)

说白了，老庄就是鄙视孔子的仁义道德和诗书礼乐，要“忘记仁义、忘记礼乐以达坐忘之境”，分明就是吐槽孔子的理论嘛。但是他不这么说，他非要讲个故事，让最讲仁义的人来说，我要忘记仁义忘记礼乐，我要跟这你老庄混。反正，任何老庄不爽的言论都是孔子说的--无论孔子说了还是没说，这跟马克吐温的名言是如出一辙的。

不过，这个故事编得有点太浅白了，连我都读得懂，这绝对不能代表老庄的独特风格。高质量吐槽要包括一个特性就是隐蔽性，是个人都懂的吐槽很容易中枪的。大家想想，这么多年只听闻有批孔的，没怎么听说批庄的，为何？主要是听故事的人听不懂，讲故事的人故意讲得让人云山雾罩不好理解。比如，下面这个说白了是冷笑话的故事：

有个人叫疏，有个人叫忽，他们是好朋友，疏和忽混得都不怎么好，但是有一哥们总是照着他俩，这人叫混沌。疏忽在混沌当中舒舒服服地生活了好多年.....有天突然疏忽不知道为何就很感恩，说啊，这个混沌是个好人，我们是不是该为他做点什么作为回报呢？他们就商量起来，然后就发现，咦，混沌原来没开窍啊！这不废话吗，开窍了还叫混沌？我们不如就给他开开窍吧，于是疏忽这俩小子就每天给混沌开一窍。看到这大家伙就想了，混沌开了窍包准会把这疏忽两臭小子给踹了。老庄不是这样编的，他说啊，第七天混沌被开了第七窍之后就挂了。故事结束，你听明白了吗？

长文不利流传，吐槽不宜过头，文章就到此结束，希望以后与大家继续分享老庄吐槽的故事。下次可以继续吐槽孔子，或者讲讲被誉为大圣人的尧舜禹在《庄子》中各种不堪的故事。太有意思了，哈哈，没想到啊，2015年我最喜欢的书竟然是这本《莊子今註今譯》（中華書局，陳鼓應)



---


`@bintou`
`2016-02-15 23:34:52`
`字数 2452`
`阅读 2732`


神谕、计算与哲学
========

`计算机教育` `哲学` `计算机理论`

---

神谕（Oracle）、计算（Computation）和哲学这个标题显然过于庞大与复杂，其实我的本意只是直白地讨论一个数学问题，得到一个关于计算理论的结论，结果却在人生、宗教和哲学等问题中陷入漩涡。

一般而言，在绝望无助的时候，通常大家就会祈祷，希望得到神的帮助。“如有神助”，定能排除万难，能力无限。无神论者自然是不信神，但这并不足以将神排除在他们的思维框架之中，只不过，他们采用了另一种方式。比如，如果一位数学家碰上了一个函数f：x --> y（x映射到y）无法求解，他也许会假设：如果有一个神存在，把这个问题交给她，就会得到这个函数的一个解（当然，也可以让神做一些我们想她做的事情，看情况而定），也许因此我会得到帮助。把这个愿意帮忙的神称为Oracle。如果这个神愿意帮助，f当然可解。问题是，我们通常假设这些个神（想一想那个只满足他人三个愿望的灯神）只帮忙比较有限的次数（比如，多项式次），而X的值域又比较大（指数规模）。问题：在这个能力无比强大但又比较小气（只计算有限次的f(x)）的神帮助下，数学家能不能自己计算这个函数呢？

比如大整数分解问题：给定一个很大的整数（例如1024比特长），要把它分解成若干小整数的乘积。假设有一个神可以解大整数分解问题，你给他许多的大整数，他都可以帮忙分解。等你听够了神的唠叨（在你得到神足够多的帮助）之后，再给你一个新选取的大整数，你能分解它吗？我想，这个神帮不上什么忙。但是，我并不确定.....

**Oracle对计算是否有帮助**这是一个非常严肃的难题，我没办法回答，但我可以告诉你们一些线索。首先，大部份数学家都相信，Oracle是没有帮助的，也就是说在上面的例子中，有神的帮助，数学家还是无法自己真正地解决难题。其次，非常矛盾地，数学家们在不同的场合也会认为Oracle会有一定的帮助，利用Oracle来区分不同的计算能力，注意，他们并不能证明Oracle有或者没有帮助。换句话说，数学家们想用神的时候就信神，想不信神的时候就否定神（和那些声称信耶稣基督并且每年都到教堂过圣诞节的教友有异曲同工之妙）。数学家这种矛盾也是值得理解的，毕竟他们碰到的难题特别多。

计算理论中有一大类问题被定义为“NP难题”，数学家们似乎还没有驯服这类问题，他们试图对这类问题进行分类，其做法就是**借助Oracle，形成难题类的等级**。比如，某类问题（记为A类问题），在P时间下解不了，那就看看给一个Oracle是不是有帮助，就定义出了一个新的类A^Oracle。显然，如果A^Oracle类问题还是无法在P时间下解，我再给一个Oracle，定义新的难题类为A^Oracle^Oracle。这些所谓不同的类其实很有可能是相同的玩意儿，但目前谁都不清楚。（以上内容可参考M. Sipser的ITOC第9.2章。）哲学上似乎也有类似的做法。

**Oracle的一种重要用途是用于证明某种问题不能被求解。**比如，在密码学的领域，通常借助Oracle来证明某种密码体制不能被破解。思路如下：首先假设某个问题不能在多项式时间内被求解，比如大整数分解问题（factoring问题）。接着，假设某种密码体制可以被Adv破解。然后借助Adv的求解过程构造某个Oracle，借助Oracle则可多项式时间求解factoring问题。结论：因为factoring问题不能多项式求解，所以声称可破解密码体制的Adv不存在，所以，此密码体制是安全的。这种证明思路我们称为：**归约**。

作为普通人，我们有没有相信神谕呢，或者思考一下，神谕对我们有实质性帮助吗？这似乎非常废话，如果你找到灯神，说，给我来一瓶二锅头，立即就有二锅头，这难道不是非常实质性的帮助吗？情况似乎并不是这样，因为神是不可揣摩与测度的，「因为他打破，又缠裹；他击伤，用手医治。」（圣经：约五18）。因此，只要神的帮助是有限次的，那么神是否有实质性帮助就需要重新考量了。想一想你喝了二锅头之后召回的那个法国人就知道了，神也曾善待于他，可是他只能回来陪你喝二锅头了（读者要是不理解这个笑话可以自行Google一下，关键词：二锅头、神灯、笑话）。

我也如先知一般给了学生们很多的神谕，但我相信，我的神谕并不能实质性地帮助到很多人。我最喜欢挂在嘴边的一句就是，你要跟别人竞争跟别人比，比什么？就比学习能力比阅读能力吧。有一个管理学的名人说过：要保持竞争实力，你要做的就是要保持强劲的学习能力。我不是名人，所以没有名言，不被相信也是正常的。然而，许多大名鼎鼎的名言传播遍及世界的每一个文化角落，知道那些道理的人多如牛毛，但是就我肤浅的目力所见，知道道理的人很多，理解道理的人却少，而践行道理的人更少了！神谕谁听啊......值得注意的是，我并不是说神谕没有帮助，我只是说，这种帮助的实质性值得考量。

好吧，其实，我什么都没讲，结论一个都没有，只是很多玩意儿值得重新考量了。充满矛盾的理论，正如神也自相矛盾一样。考虑到，为了高兴，你每天都必须做几件自己不喜欢的事情，以上这些混乱的文字也就好理解了。

Appendix. (Proposed by Zhijie Li)

* Oracle是什么？能回答某种神奇问题的外部设备。
* Oracle Machine是什么？是一种变种的Turing Machine，它可以访问某种Oracle。
* 谁提出Oracle Machine？图灵在他的Phd论文中提出。
* 为什么提出Oracle Machine？用于定义“规约”，把某种问题的求解规约到某种Oracle的访问。比如我们想知道，假如存在一台可回答图灵停机问题的Oracle，那么是不是某种图灵不可判定问题会变得可判定。结果表明，答案是否定的。

目前，除了经典计算领域，在量子计算、密码学、机器学习等领域都常用到Oracle Machine的概念。可以笼统地认为，Oracle Machine是出于研究需要而假设存在的，具备某种计算能力的计算模型。

--2011年12月写；2016年2月整理.



---


`@bintou`
`2016-01-18 00:11:49`
`字数 2942`
`阅读 1976`


治國學雜話--梁啟超
==========

`国学` `治学`
---------

***转发此文，因为对文章中的观点非常认同，而且这些观点关乎治学做人而不仅仅适用于国学之学习，窃以为对当代学子依然具有深厚的现实意义，不要忘记这可是近百年前的文章啊！***

學生做課外學問是最必要的。若只求講堂上功課及格，便算完事，那么，你進學校，只是求文憑，并不是求學問。你的人格，先已不可問了。再者，此類人一定沒有“自發”的能力，不特不能成為一個學者，亦斷不能成為社會上治事領袖人才。課外學問，自然不專指讀書。如試驗，如觀察自然界……，都是極好的。但讀課外書，最少要算課外學問的主要部分。

一個人，總要養成讀書的趣味。打算做專門學者，固然要如此。打算做事業家，也要如此，因為我們在工廠里、在公司里、在議院里、在……里做完一天的工作出來之後，隨時立刻可以得著愉快的伴侶，莫過于書籍，莫便于書籍。

但是將來這種愉快得著得不著，大概是在學校時代已經決定。因為必須養成讀書習慣，才能嘗著讀書趣味。人生一世的習慣，出了學校門限，已經鐵鑄成了。所以在學校中不讀課外書以養成自己自動的讀書習慣，這個人簡直是自己剝奪自己終身的幸福。

讀書自然不限于讀中國書，但中國人對于中國書，最少也該和外國書作平等待遇。你這樣待遇他，他給回你的愉快報酬，最少也和讀外國書所得的有同等分量。

中國書沒有整理過，十分難讀，這是人人公認的。但會做學問的人，覺得趣味就在這一點。吃現在，是最沒意思的事，是最沒有出息的人才喜歡的。一種問題，被別人做完了，四平八正的編成教科書樣子給我讀，讀去自然是毫不費力。但從這不費力上頭，結果便令我的心思不細致不刻入。專門喜歡讀這類書的人，久而久之，會把自己創作的才能汩沒哩。在紐約、芝加哥筆直的馬路、嶄新的洋房里舒舒服服混一世，這個人一定是過的毫無意味的平庸生活；若要過有意味的生活，須是哥倫布初到美洲時。

中國學問界，是千年未開的礦穴，礦苗異常豐富。但非我們親自絞腦筋絞汗水，卻開不出來。翻過來看，只要你絞一分腦筋一分汗水，當然還你一分成績，所以有趣。

中國學問界的礦苗，當然不專指書籍。自然界和社會實況，都是極重要的。但書籍為保存過去原料之一種寶庫，且可以為現在實測各方面之引線。就這點看來，我們對于書籍之浩瀚，應該歡喜感謝它，不應該厭惡它。因為我們的事業比方要開工廠，原料的供給，自然是越豐富越好。

讀中國書，自然像披沙撿金，沙多金少。但我們若把他作原料看待，有時尋常人認為極無用的書籍和語句，也許有大功用。須知工廠種類多著呢。一個廠里頭還有許多副產物哩。何止金有用，沙也有用。

若問讀書方法，我想向諸君上一個條陳。這方法是極陳舊極笨極麻煩的，然而實在是極必要的。什么方法呢？是抄錄或筆記。

我們讀一部名著，看見他征引那么繁博，分析那么細密，動輒伸著舌頭說道：“這人不知有多大記憶力，記得許多東西，這是他的特別天才，我們不能學步了。”其實那里有這回事。好記性的人不見得便有智慧，有智慧的人比較的倒是記性不甚好。你所看見者是他發表出來的成果，不知他這成果原是從銖積寸累困知勉行得來。大抵凡一個大學者平日用功，總是有無數小冊子或單紙片，讀書看見一段資料覺其有用者，即刻抄下。（短的抄全文，長的摘要記書名卷數頁數。）資料漸漸積得豐富，再用眼光來整理分析它，便成一篇名著。想看這種痕跡，讀趙北甌的《二十二史札記》、陳蘭甫的《東塾讀書記》，最容易看出來。

這種工作，笨是笨極了，苦是苦極了，但真正做學問的人，總離不了這條路。做動植物的人，懶得采集標本，說他會有新發明，天下怕沒有這種便宜事。

發明的最初動機在注意。抄書便是促醒注意及繼續保存注意的最好方法。當讀一書時，忽然感覺這一段資料可注意，把他抄下。這件資料，自然有一微微的印象印入腦中，和滑眼看過不同。經過這一番后，過些時碰著第二個資料和這個有關系的，又把他抄下，那注意便加濃一度。經過幾次之后，每翻一書，遇有這項資料，便活跳在紙上，不必勞神費力去找了。這是我多年經驗得來的實況。諸君拿一年功夫去試試，當知我不說慌。

先輩每教人不可輕言著述。因為未成熟的見解公布出來，會自誤誤人，這原是不錯的。但青年學生“斐然有述作之譽”，也是實際上鞭策學問的一種妙用。譬如同是讀《文獻通考》的《錢幣考》、各史《食貨志》中錢幣項下各文，泛泛讀去，沒有什么所得。倘若你一面讀，一面打主意做一篇《中國貨幣沿革考》，這篇考做的好不好另一問題，你所讀的自然加幾倍受用。

譬如同讀一部《荀子》，某甲泛泛讀去，某乙一面讀一面打主意做部《荀子學案》，讀過之后，兩個人的印象深淺，自然不同。所以我很獎勵青年好著書的習慣。至于所著的書，拿不拿給人看，什么時候才認成功，這還不是你的自由嗎？

每日所讀之書，最好分兩類：一類是精讀的，一類是涉覽的。因為我們一面要養成讀書心細的習慣，一面要養成讀書眼快的習慣。心不細則毫無所得，等于白讀；眼不快則時候不夠用，不能博搜資料。諸經、諸子、“四史”、《通鑒》等書，宜入精讀之部，每日指定某時刻讀他，讀時一字不放過，讀完一部才讀別部。想抄錄的隨讀隨抄。另外指出一時刻，隨意涉覽。覺得有趣，注意細看；覺得無趣，便翻次頁。遇有想抄錄的，也俟讀完再抄，當時勿窒其機。

諸君勿因初讀中國書勤勞大而結果少，便生退悔。因為我們讀書，并不是想專向現時所讀這一本書里頭現錢現貨的得多少報酬，最要緊的是涵養成好讀書的習慣和磨練出善讀書的腦力。青年期所讀各書，不外借來做達這兩個目的的梯子。我所說的前提倘若不錯，則讀外國書和讀中國書當然都各有益處。外國名著，組織得好，易引起趣味；他的研究方法，整整齊齊擺出來，可以做我們的模范，這是好處。我們滑眼讀去，容易變成享現成福的少年們，不知甘苦來歷，這是壞處。中國書未經整理，一讀便是一個悶頭棍，每每打斷趣味，這是壞處，（只要走路，斷無冤枉；走錯了回頭，便是絕好教訓。）從甘苦閱歷中磨練出智慧，得苦盡甘來的趣味，那智慧和趣味卻最真切，這是好處。

還有一件，我在前項書目表中，有好幾處寫“希望熟讀成誦”字樣。我想諸君或者以為甚難，也許反對，說我頑舊。但我有我的意思，我并不是獎勵人勉強記憶。我所希望熟讀成誦的有兩種類。一種類是最有價值的文學作品；一種類是有益身心的格言。好文學是涵養情趣的工具，作一個民族的分子，總須對于本民族的好文學十分領略。能熟讀成誦，才在我們的“下意識”里頭，得著根柢，不知不覺會“發酵”。有益身心的圣哲格言，一部分久已在我們全社會上形成共同意識，我既做這社會的分子，總要徹底了解它，才不至和共同意識生隔閡。一方面我們應事接物時候，常常仗它給我們的光明。要平日摩得熟，臨時才用得著。我所以有些書希望熟讀成誦者在此。但亦不過一種格外希望而已，并不謂非如此不可。

最后還專向清華同學諸君說幾句話：我希望諸君對于國學的修養比旁的學校學生格外加功。諸君受社會恩惠，是比別人獨優的。諸君將來在全社會上一定占勢力，是眼看得見的。諸君回國之后對于中國文化有無貢獻，便是諸君功罪的標準。

任你學成一位天字第一號形神畢肖的美國學者，只怕于中國文化沒有多少影響。若這樣便有影響，我們把美國藍眼睛的大博士抬一百幾十位來便夠了，又何必諸君呢？諸君須要牢牢記著：你不是美國學生，是中國留學生。如何才配叫做中國留學生，請你自己打主意吧。



---


`@bintou`
`2020-10-25 05:18:51`
`字数 3602`
`阅读 2120`


2020级图灵班工作手记
============

`图灵班` `教学手记`

---

### 什么是图灵班？

一个学生自发组织的学习小组。

### 图灵班的目的是什么？

* 阅读（教材）
* 讨论（问题）
* 目标：[五核心](https://www.jianshu.com/p/96e7142fb41a)   
  
  如果讲一点虚的，也许寻找学习乐趣也是其中之一。
* [FAQ](https://www.jianshu.com/p/1f307bbd2b9f)

### 目前的任务是什么？

阅读ThinkC（[这是指南](https://www.jianshu.com/p/5332307389c7)），学习编程。请到[课堂派](https://ketangpai.com)上提交代码（加课码：ZCQP23）。请让我看到你的**信心、决心与执行力**。

### 怎样才能进图灵班

首先同学们需要自愿提交一份申请，然后根据课堂派或者平时的表现，加一个简单的面试来决定。国庆后就开展此项工作。

### 大学计算机新生求生技能（2020年10月2日）

现在要求大家具备以下技能：   

- 翻墙，使用Google（远离Baidu）；   

- 懂得使用GitHub分享、阅读代码；   

- 懂得双系统安装，linux系统使用；   

- 使用MarkDown写作、分享代码（推荐[这个](https://paste.ubuntu.com/)）、分享知识；   

- 坚定阅读英文教材的决心（[为什么要看英文教材？](https://www.jianshu.com/p/d6c29f714e9d)）。

### 学习编程的第一天（2020年10月3日）

今天17级某师兄义务为新生讲了一次课（[这是讲义](https://www.notion.so/iwktd/2020-152af5e8348f4790881f7a190af2d56f)），其中讲到了函数。关于函数，我补充如下。

可能到了课堂上，一个月都不会讲到函数，但是今天第一节课就讲了，是不是冒进？首先，学编程不仅仅是学语法，是学处理问题的方法。其次，函数就是思考问题的第一步。比如，写个程序目的一定是要解决问题，什么是问题？立即就想到输入什么，输出结果是什么。这就是函数定义了。注意，具体怎么实现是下一步，请大家写程序的开始就考虑输入输出。接下来才考虑输入输出的数据类型或数据结构。再才是处理问题的算法。所以，回应第一天给大家说的，什么是程序？数据结构加算法。如果现在入门的时候不强调，就很有可能出现高年级同学写程序只有main函数的坏习惯。main函数只是一个控制函数，主要用于与用户的交互，请区分处理问题与人机交互的不同。这是我非常想补充的一点，具体的一些想法大家可以看[这一份关于算法思维训练的讲义](https://www.jianshu.com/p/fc258c7b341d)。

### C语言到底香不香（2020年10月4日）

关于用什么语言教编程，这个很有些故事的。很早大家就发现了C语言不适合入门，某些欧美高校就用函数式语言进行教学，有一本很著名的教材How to design programs(HTDP)。而SICP更是其中佼佼者，使用Lisp和Scheme教程序。SICP是我看过最牛的教程序设计的教材。

但是，似乎全世界都没有往这更合理更高级的方向发展。最早使用SICP的MIT也是对函数式语言发起攻击的最早的一波高校之一，然后提出SICP-Python版本。结果当然是也没有很流行，就我个人来看，SICP-Python是失败的。

人类的发展怎么会倒退着走呢？其实，倒退着走基本是必然的。打个比方，你说开兰博基尼、保时捷不比开奥拓好吗？但是，如果你的大环境就是脏乱差，奥拓还是挺适合的。现在的计算机系统环境有多好？估计还是属于脏乱差之列吧。C语言香还是Go香？当然，Go香。但是计算机系统的母语是C语言啊，就好比你问象形文字好还是拉丁文字好？就算象形文字再不科学，作为你的母语还是得学的，对吧？如果明白到这个道理，那就要学C的。只是，不要太认真太努力学，应该把它视为一种入门工具、一种描述问题的朴素语言。（类似的，学了中文还是要学英语的。）以此为基础，尽快走向更高级的语言，则进可攻、退可守。没人让你一辈子抱着C不学新语言不是吗？所以，C语言还是挺香的！

### 关于斐波那契数列那不值得观摩的代码的评论

可能大部分同学没有理解为什么要提交代码，当然是接受批评了。否则怎么进步呢？也许我批评的这句“fibo函数输入什么、输出什么？大家理解这里的输入是不是一定要键盘输入scanf？输出就一定是屏幕输出printf？面向问题去思考。”大家也没有明白。因为也没人问啊。我再继续啰嗦几句。请问，你写了这个Fibo函数给谁用？怎么用？比如，我把问题扩展一下，请尝试不同的整数n，求第n项斐波那契数与第n+1项斐波那契数的比值，并问当n趋向很大的时候，这个比值是否会接近某个数值？好，你开始做这题，于是就发现，咦，之前写的Fibo竟然帮不上忙，需要重新修改。所以，小结一下，如果某同学写的Fibo函数能继续在新问题下使用，恭喜你，你有非常好的思维习惯。

我点评的那段代码大概长这样。

```


1. int Fibo()
2. {
3. scanf()
4. ......
5. printf()
6. }

```

看上去这个问题似乎无伤大雅。让我想起在大二作业当中看到的，当我要求大家写函数求，有同学在函数中`scanf`这个n，让人啼笑皆非。为什么出现这样的问题？无非入门的时候从来没有人提醒罢了。希望这些唠叨能起一点作用。

### 关于作业

有几位同学反映最近一直在看书，没写代码，就没交作业。是这样的，学程序设计，看书的同时一定要动手，一定要动手，一定要动手！这是专业性决定的。动手写代码是必须的。建议大家就是看书1小时，就赶紧实践1小时。然后，另外课后的习题做起来，课堂派的题也很简单，可以考虑考虑。

### 关于加入图灵班的提醒

各位20级的同学，最近感谢大家的积极关注。我一直说，大家不要期待图灵班能给予大家太多的东西，希望大家要降低期望值。图灵班一直都做得非常不够，师资有问题是肯定的，以后各种安排，包括时间、场地，能给大家的真的真的非常有限。一直我都感觉非常抱歉。图灵班的意义在于大家为了一个共同的理念、目标，一起学习。图灵班的老师就是你们自己，其他人都只是辅助作用的，甚至可能是起到负面作用。希望大家能多了解这个读书小组，慎重考虑。

### 第一次面谈

10月11日下午4点，131实验室。新生25人。

### 第一周学习任务

* 数组、排序、查找；
* 阅读GSLA、看视频（三周至四大基本子空间）；
* LeetCode自选两题提交；
* C语言参考书：Points on C
* 算法与数据结构参考书：Algorithms in C（Sedgewick 1998）；Algorithms unplugged；算法导论
* C语言最经典的是KR啊！虽然我没给大家推荐，也要告诉你们，Q群里有。

### 第一周的一个额外作业

```


1. #include <stdio.h>
2. int main()
3. {
4. unsigned char a = 255;
5. printf("a + 2 == %d \n", a + 2);
6. printf("a^5 == %d \n", a * a * a * a * a);
7. a += 2;
8. printf("a + 2 == %d \n", a);
9. a = 255;
10. a = a * a * a * a * a;
11. printf("a^5 == %d \n", a);
12. a = 255;
13. a = a * a * a * a * a * a;
14. printf("a^6 == %d \n", a);
15. return 0;
17. }

```

请问以上程序的输出是什么？可以使用计算器，但是在给出答案前先不要编译执行该程序。

### 图灵班本学期的学习内容框架

#### 程序设计与数据结构

其实，整个脉络都是非常清晰的。现在只是具体化而已。如果你不清晰的话只需要理解到：程序 = 数据结构 + 算法。

目前语法已经不会成为重点去讲解了。那么剩下就是数据结构入门：数组、链接表、BST。算法：排序、搜索、树相关的算法。再稍微深入就是：堆、栈这样的结构。然后算法再深入一点就是广度优先、深度优先。最后，如果可以希望再有一点点DP。大概就是这样。其中穿插讲解一点点数论小知识。希望大家了解这个框架。

我大致把它表达为[这样的一份指南](https://www.jianshu.com/p/fc258c7b341d)，很标准化的内容了。没什么新鲜的东西。

#### 线性代数

[GSLA](https://www.jianshu.com/p/d651f23aa1e3)

### 第二周学习任务

* 链接表初步
* 线性代数三个视频

### 第二周作业点评

各位同学，就我刚才改了几份作业来说，我看到一个问题，这个问题不知道什么课本会教。但是，你们肯定没想。我一直提示过很多次，估计也没怎么看，或者看了也不理解。什么问题？函数的定义问题。为什么一个函数要这样定义，不能那样定义。注意，这绝对不是语法问题。下面举个例子，第二周作业3，写一个素数筛法。理解错题意的我都不说了。就说说，你们认为这个函数应该怎么定义？下面是大家的代码：1、void ans(int n,int l,int r) 2、int\* create\_prime(int range); 3、int find(int n) 4、int is\_primer(int b,int arr[]); 你认为哪一个是自己想要的呢？还有一个问题，到底是在这个函数外动态申请一个数组，还是在函数内形成一个数组传到函数外？

我很想提醒新生两点：第一，真的不必然会有老师教你；第二，你们的思考真的太少。仅有的时间都在忙碌，没有思考，这是可悲的。

今天有同学对我说，学了线性代数不知道怎么用。虽然我今天也讲了一个应用，而且我还可以讲很多的应用，但是估计也满足不了大家迫切“不起来”的需求。所以，我的意见是，大家不要太迫切要“用”，把数学作为一种语言去看待更好。打个比方，我在课堂派出的Fibonacci数的习题。矩阵只是一种描述工具。同样，在量子计算中，矩阵也是一种描述工具，没有这种工具，估计也就没有量子计算了。

### 第三周学习任务

* 增加线性代数相关作业
* 基本数据结构：栈与队列
* 本周周末讨论线性代数相关内容，请预习到四大基本子空间

---


`@bintou`
`2018-09-04 19:31:39`
`字数 607`
`阅读 2021`


图灵班工作计划--2018年
==============

`图灵班`

---

> 作者：斌头老师   
> 
> 单位：华南师范大学计算机学院   
> 
> 时间：2018年9月   
> 
> 版本：0.1

---

引言
--

2018年秋季，斌头老师的图灵班将会迎来其第四批学员。如果你还不知道什么是图灵班，请看[这里](https://www.jianshu.com/p/0b98e702db6b)或[更久远的帖子](https://zybuluo.com/bintou/note/130481)。或者找15、16级的同学打听。

计划
--

因为时间精力有限，打算对18级图灵班进行比较大的改变。主要思路：大幅度减少入班人数，主要招收有一定基础、有潜力有志向的同学进来学习。增加斌头老师亲自出马上课面授的时间。

* 面试时间：从今天开始到军训结束，接受预约。面试官有可能是我本人，也可能是往届的师兄。
* 时间：军训后开始高强度学习训练。
* 人数：3-5人。
* 本学期内容：算法、数论、线性代数、C编程。
* 要求：必须通过面试；心态开放，愿意交流、分享。其他的说不清......

FAQ
---

* 谁应该参加图灵班学习？图灵班的思路是对的，大部分同学都应该跟这个学习思路。
* 为什么限制人数？作为一个学习小组，资源有限，必须做人数控制。而且人数少了，管理与教学的效率更高。也算是一次改革吧。
* 谁不应该报名参加图灵班面试？   
  
  1.零专业基础   
  
  2.没有强烈的专业意识   
  
  3.缺乏学习信心、没有远大的理想   
  
  4.参加很多社团，总是很忙   
  
  5.英语恐惧症

愿景
--

在过去的四、五年，我一致致力于图灵班的建设。不敢说取得了什么成绩，但是在图灵班的学员中我看到了潜在的发展可能性，也感觉到很多同学不同程度的进步，从而坚信这个学习小组存在的必要性。为此，......惨淡经营，苦苦支撑。



---


`@bintou`
`2016-10-10 05:23:51`
`字数 324`
`阅读 2366`


2016图灵班授课手记
===========

`手记` `教学` `图灵班`

---

### 2016年10月9日

于10月7日至8日进行面试，得2016图灵班学员20名。确定授课时间、地点。建立畅顺的沟通渠道。希望每一位学员都是班级的主人。

#### 2016－2017年度第一学期教学计划

1、C/C++程序设计；教材：ThinkC和ThinkC++。

2、数据结构与算法基础；教材：《程序设计竞赛入门经典》或其他。

3、线性代数；教材：MIT的GSLA；请务必要看视频、做习题。

4、计算机科学思维方式，内容包括但不限于数论、代数、概率等；教材：无，无有时也意味很多。

#### “数据结构与算法基础”教学内容

1、基础数论

2、递归

3、排序、查找

4、数组、队列、堆栈

5、树

6、DP初步

7、贪心法初步－－哈夫曼编码

8、图论

#### 线性代数教学内容



---


`@bintou`
`2016-11-23 06:32:42`
`字数 2182`
`阅读 2323`


大学生的提问智慧
========

`导论` `大学教育`

---

“没有问题是最大的问题！”，这是我常对大学生们说的一句话。事实显示，无法提出有效问题往往意味你的学习深度不够，也意味缺乏阅读、缺乏思考。不提问的学习是难以进步的。如何提问，如何高效地提问，如何提出有意义的问题是本文所关注的要点。没有人天生会提问，提问需要智慧，更加需要锻炼。

首先，我们需要设定一下提问所必须依据的原则。大致有三：

1、问题的目的是为了寻求帮助。提问前请把自己置于一个求助者的状态。

2、既然自己求助，那么就要设定回答者是一个“懒惰的”或者“不情愿的”帮助者。

3、因此，提问者在提问时所要做的就是尽可能地让回答者给出回答。

有以上原则为前提，就不难得出以下提问的注意事项。

#### 1、问题描述含糊。

错误的问题永远不会有正确的答案。含糊的问题往往也不会得到什么帮助。

比如，“老师，为何我的程序明明是对的，但是执行不了？”。这个问题在实际工作中经常出现，但是在不同的学生身上的表现又各不相同。有一点是比较普遍地相同，就是提问者强调自己没错，为何机器（系统）会错？这很危险！实际上，这个问题，有可能是编译没过，也可能是进入了死循环，甚至程序正常执行并结束......而这些都被提问者归结为“执行不了”。可见，能清醒地明白自己的处境，清晰地描述自己的问题是多么的重要。不要怕啰嗦，被提问者不是神仙，他们需要更多的信息了解你的处境。

比如：“老师，行列式我不懂......” 不懂不是问题！行列式不懂，是定义出了问题？是证明出了问题？还是你认为书本没讲清楚？类似这样的问题，最好是“老师，课本xx页的证明中，有一步的逻辑关系我理解不了，请问......”

#### 2、问题描述过于“个性化”

所谓个性化，指没有使用大家公用的术语，添加了过多的个人口语化或者情绪化的内容。导致与接受提问者无法有共同的语境，也就无法正常交流。

#### 3、提问的场合方式不对

请参照原则二。说一种我最怕接到的提问，手机短信或者微信发来，“老师，你什么时候有空？” 实话实说，我回答不了这个问题。这只是一个例子，拿到学术提问上来说，你不能指望手机短信、微信能有多详细的解答。

#### 4、多提小问题，少探讨大问题。

如果你总是提很“庞大”的问题，或者”很高深“的问题，那通常得到的帮助也非常有限。因为你的问题往往不能引起回答者的兴趣，或者问题过于庞大之后，让回答者望而却步，懒得回答了。

因此，大问题要化成小问题，通过小问题来得到帮助。多个小问题往往就能帮助解决大问题了。

#### 5、有意义的问题通常会得到更多的响应

作为老师，其实在上一门课的时候已经在心目中准备回答学生们潜在的问题，如果你不提出，说明你没有学到点子上。

#### 6、作为提问者，需要勇气

不但需要勇气，还需要忍受他人的不响应，参考原则二。当他人不回答，多反省自己，也许是自己提问出了问题。既然有心理准备，就不要害羞、害怕。如果害怕自己被鄙视而不提问题，那永远都提不出问题

以下介绍一些特定的提问技巧。

在学习中，有两个通用的问题可以供大学生们使用，甚至一辈子使用。**“这个概念（问题、定理、算法）的动机（motivation）是什么？”**。一般而言，在新的知识点中包括问题的描述（概念）、解题的方法、定理的描述与证明、结论的推广与应用。在学习这样的知识点时都适合提出以上问题。比如，在程序设计学习中，指针这个概念，你就可以问，为何要使用指针，指针应该用于什么场景。甚至，如果指针是在这样那样的条件下提出的，我们还可以问，现在这些条件还适用吗？又比如，对象与类，为何要提出这样的概念，提出的意义（动机）何在，在什么场合下应该使用（或者不应该使用），有什么优势和缺陷？

第二个问题，**“这里的逻辑关联是什么？（为何从已知条件会得到这样的结论）”** 。我们很容易会通过自己的直觉接受或者否认一个结论，然后在数学证明中，除了有非常符合人类直觉的结论也有反直觉的结论，无论是哪一种，在接收一个结论前，我们最好的做法是完全掌握这个结论从条件到最后得以证明的整个过程，意思是，每一个逻辑关联都必须严格验证。否则，我们往往就只是知其然而不知其所以然，人云亦云，错过了许多有意义的细节。甚至导致整个知识体系的把握存在严重的缺陷。提这个问题还迫使我们紧扣关键概念、逻辑推导，这是非常有益的学习过程。考察课程中，回答“为何定长计算非常重要”时，大家普遍存在关键概念不清，逻辑关联不明的问题。

对于某些复杂的数学定理或者公式，我还喜欢问的一个问题是：**这里有没有直观的含义？**因为大部分的理论家不会平白无故地去造很多的公式、定理，很多的理论是源自于实践的发现。《高等数学》、《线性代数》中的概念、公式有不少属于这个类型，比如：行列式的概念、导数的概念等等。在自己的学习与阅读中，如果没有发现或者悟出某些特定概念的直观，而这些概念恰恰又比较复杂时可以尝试做这种提问。

还有一个问题，老师讲课越讲越迷，你听不懂怎么办？我有一个建议，就是给他提问！首先当然还是要明确自己的问题。其次，组织同学们在课间向老师请教。请教的范围包括：教学计划、具体的问题、证明的理解等等。我相信，同学们围着老师进行提问这种在大学已经失传的“神技”必定可以起到巨大的作用。关键还是要交流！下课有事没事跑到老师那里问他问题，探讨他上课时候到思路，探讨他的想法等等都是值得提倡的好方法。提问、提问、提问，要具体落到实处。用提问来促进交流促进学习。



---


`@bintou`
`2017-01-12 06:40:52`
`字数 1341`
`阅读 1686`


欲精深功夫须熟练起式
==========

`太极` `笔记`

---

作者：四川 林墨根

余自从跟杨式太极宗师李雅轩习拳以来，至今近五十年。时刻谨记先师教诲，刻苦练功，不敢有丝毫倦怠。常忆先师练拳，尤重起式，我时时揣之却未能深思其中奥秘。直到2002年，83岁的我因胃溃疡大出血住进了医院，历经三次大手术，骨瘦如柴，大肉若脱，医学专家断言活不过三个月。躺在病床上，我又想起恩师的教诲，开始专门修练太极拳的起式。躺着，坐着……时时勤练之。不想，如此半年，不仅身体渐渐康复了，而且功夫也精进不少，如今发劲、化劲均得心应手，至此方才领悟我杨式太极拳起式之妙，妙不可言。

首先，起式作为杨式太极拳的第一式是无极生太极的关键所在，能使人身心放松，有助于经络的畅通，促进内气的充盈与运行，调和气血，平衡阴阳，从而促进人体健康。此式既是静功，又是内功，还是气功、养生功。再者，从练拳的放松与稳静，使整趟拳更有拳意，更有气势。尤其重要的是，在太极拳推手时，欲要做到浸人于不知，发人于不觉，此实乃熟练起式而后身、手至轻、至柔之故。

总而言之，欲要精深功夫，必先熟练起式。现将先师所授杨式太极拳起式之练法公诸于世，惟愿太极拳能为人类的健康事业再做贡献。

预备式：两脚跟并拢外八字站立，两臂自然下垂，中指贴裤缝，顶头拔背，两眼平视前方。右脚脚跟提起，以右脚尖点地，向右侧横开半步，随之脚跟着地，左脚尖内扣，两脚平行，与肩同宽。随后在意念的带领下，缓慢从上到下依次松头顶、松面部、松颈部、松双肩、松胸部、松背部、松腹部、松胯部、松大腿、松双膝、松小腿、松踝关节、松脚背、松脚趾，松至脚底涌泉穴（备注1： 松时，意念犹如水流，水流至哪里，就松在哪里，身势立稳，头顶虚灵，尾闾中正。只有全身松开，心意松开，才能达到形态上的松。）如此稍待片刻，让身心稳静下来之后才能开动。开动时要大松大软，仍要保持此稳静（备注2： 此为无极式站桩功）。

起式：由以下四个连贯动作完成：

一． 两臂徐徐向前提起，似有细绳将其拉起，两后胛缓缓打开，两手掌自然伸直，成舒松自然掌型，掌心向下，掌指朝前，两掌之间的距离略宽于肩。随起随吸气，同时两脚脚趾微微抓地、提肛，收腹（备注3：两臂提起与吸气、两脚抓地、提肛、收腹为同时动作。）

二． 当两臂升至与肩同高时，松肩，两臂略向内收，即环状收回，至两指尖的距离与头部同宽（备注4：松肩，两肘自然左右稍开，就使两臂环状收回；环状收回的同时，再次两脚趾抓地，提肛，收腹）。

三． 随后，将手肩忘掉，两臂缓缓垂直下落（备注5：两掌掌心向下，似降落伞兜风样缓缓下落。）与此同时松胸部、松背部、松腹部、松胯部、松大腿、松双膝。

四． 当两手落至与腰部同高时（这时意念松至双膝），坠肘，两小臂及前胛自然打开，两掌指尖向前，掌心依然向下。直至两臂垂落至身体两侧，松手腕，指尖朝下，中指自然贴至裤缝。这时感觉两臂犹如钟摆，自然悬垂，手指有麻胀感。在这一过程中，松双膝、松小腿、松踝关节、松脚背、松脚趾、松至脚底涌泉穴。

至此，一个完整的起式即告完成。练习者可依以上动作要领，用心体会，反复练习，日积月累，当可收到奇效。余亲身体会，每日练此起式半小时，相当于打一趟太极拳，周身舒适，精力充沛，个中之妙只有常练习者才可领悟。

太极第一式不可轻视。太极第一式不可一日不练。 2005年10月



---


`@bintou`
`2016-01-29 00:23:14`
`字数 1466`
`阅读 5533`


《计算理论导引》学习笔记
============

`计算理论` `学习笔记`

---

ITOC（Introduction to Theory Of Computation)主讲三大内容：什么是计算；什么可计算；如何度量计算问题的效率。大致上来说，首先我们需要一种准确的表达法来说明到底计算本质上是什么，不同的科学家抽象出不同的计算模型，于是我们就要考查这些模型的表达能力(第一部分)。其次，我们发现计算是有局限的，不是什么问题都能计算，那到底什么是可计算的问题呢？有什么问题是不可计算的呢（不存在算法）？（第二部分）如果某些问题是可解的，存在某种算法可以解决这个问题，那么这种算法的效率如何度量呢？我们需要一种通用的标准度量，並建立相關理論。（第三部分）

*2016年元月 by Bintou*

第0章 引論
------

### 0.1 自动机、可计算性、复杂性

### 0.2 數學表示與術語

### 0.3 定義、定理與證明

### 0.4 证明的类型

*學習時間安排：一天或者半天；應該無難點。*

第1章 正則語言
--------

Language（语言），对计算问题的高度抽象表达。整本书的重点是“计算“，如果能体会出在描述计算理论时语言的定义所产生的巨大作用，则理解就上了一个台阶。只是，第一章并不能产生这么大的效用，需持续关注。

### 1.1 有限自动机

概念：FA、語言、正則語言、正則操作   

定理：正則語言類在正則操作（並、交、串聯）下封閉；

### 1.2 非确定性

重點：體會計算的**非確定性**   

難點：DFA與NFA的等價

对非确定性的两种解读：1、并行执行；2、总是猜对执行路径。哪一种更好？   

问题：为什么我们需要“不确定性“？

### 1.3 正则表达

### 1.4 非正则语言

要點：自動機的計算侷限   

難點：Pumping Lemma及其應用

*2016年元月22日上午，自己重新複習了一遍第1章，感覺很容易，然而依然感覺有意思。*

第2章 上下文无关语言
-----------

### 2.1 上下文无关文法

重点：歧义性

问题1：为什么把能以不同方式生成的字符串称为歧义？   

问题2：为什么需要“最左派生“这个定义？

### 2.2 下推自動機

下退自动机（PDA）比有限自动机的能力更强，主要体现在哪里？为什么PDA能力会更强呢？

问题1：在Lemma 2.21的证明中，如何确保可被匹配的串w一定会被匹配？   

回答：构造算法是非确定性算法。重点体会非确定性选择的含义。

问题2：在Lemma 2.27的证明中，如果p不可达q，那么的构造是否还合法（会出现不合法的情况）？   

回答：暂无

### 2.3 非上下文無關語言

### 2.4 （忽略）

第3章 丘奇-圖靈命題
-----------

這一章的主要內容介紹圖靈機及其相關概念。其主旨是進一步刻畫計算的本質。重點要區分兩個概念：圖靈可判定與圖靈可識別。從算法的角度看，前者要求計算這有限步之後停機，而後者沒有。明白了這個區別，就對計算機的有限計算有了更深入的理解。

### 3.1 圖靈機

一種計算模型

### 3.2 圖靈機的各種變形

### 3.3 算法的定義

### 第4章 判定性

### 4.1 可判定语言

### 4.2 停机问题

重点：对角线法、停机问题不可判定的证明

5 可归约性
------

这一章的重点是理解归约的本质、过程与应用。

### 5.1 语言理论中的不可判定问题

针对RL与CFL的若干语言形成的判定性问题进行证明。

### 5.2 一个简单的不可判定问题：PCP问题

只是一个证明！PCP问题的描述很简单，其不可判定性倒是颇令人感到意外。这里除了一个结论，一个冗长的证明外，内容不多。

### 5.3 不可判定问题的形式化定义：映射可归约性

重点：Mapping Reducibility的定义

第6章 计算理论的高级专题
-------------

### 61. 递归定理

递归定理展示“程序自我复制是可能的“这样一个简单而令人吃惊的结论。

[The Quine Page](http://www.nyx.net/~gthompso/quine.htm)，里面收集了大量不同语言写成的Quine程序：自己输出自己源代码的程序。



---


`@bintou`
`2017-07-09 02:19:38`
`字数 12638`
`阅读 5189`


CLRS学习指南
========

`学习笔记` `算法`

---

*以下内容源自2015年寒假的教学笔记，适用于2016年的学习，持续更新，请保持关注。有问题请发Email联系bintou2010@qq.com.*

第一部分 基础
-------

### 第一章 算法

1、什么是算法？（An algorithm is thus a suquence of computational steps that transform the input into the output.）   

大家还需要去找答案，注意要进一步归纳总结。

**术语：**

* computational problem（计算性问题）
* decisional problem（判定性问题）
* 计算领域三大问题：什么是计算机？什么问题可计算（可解）？解某个问题需要多长时间、消耗多少资源？

2、算法能解决什么问题？   

书本给出了很多实例，说明算法能解决很多很多问题，似乎要显示说算法无所不能。其实我们必须关心，什么问题算法不能解决。

**扩展**：停机问题（什么是停机问题，有什么重大意义？）

3、什么是数据结构？   

需要慢慢填空......

4、难解问题   

**概念：** P、NP、NPC，不理解可跳过，记住P是多项式时间内可解的问题集合即可。   

**思考：** 难题为什么是难？有什么已知的难题？   

**换一个角度思考：** 什么是容易解的问题？   

**术语：** reduction（规约），这不容易的。主要用于对NPC的描述。

5、算法的效率   

用实际的运算给出直观的感受，读者必须去感受。   

比较：，，，， ，

6、算法以及其他技术的讨论   

讨论内容，有很多很多“？”，不是难点，但需要思考，对初学者，这种思考往往是提高水平的正确路径。

7、扩展思考与检索   

为什么说算法是计算机科学的核心内容？算法的研究起源在哪里？什么时候开始人们认为：算法奠定了计算机科学的基础？

### 第二章 算法起步

#### 2.1、插入排序（以实例带动讲解）

术语：Loop invariants（循环不变量？）   

这是CLRS分析算法的一种重要技巧，要认真理解为何引入这个概念，以后如何运用这个概念。

伪代码的表示法，简单工作！

#### 2.2、算法分析模型

##### 2.2.1 重点：RAM

注意：本书讲解RAM以牺牲准确性为代价获得更通俗易懂的表达，原始的RAM模型可没这么简单。但是我喜欢这种讲解。   

扩展思考：除了RAM模型还有什么分析算法的模型？

*Additional Comments about RAM:* 由于不少同学纷纷表示对RAM的不理解，我多说几句。首先声明，不理解RAM模型并不会严重影响后续阅读，所以你可以非常放心目前的“不理解”。但我依然建议大家看看多两遍课本这并不冗长的两页说明讲解。以下是一些要点：

1. RAM模型是用于分析算法的一种计算模型；并非真实的计算机。
2. 一种计算模型通常会包括：指令、内存、数据类型、指令调度等内容。然而，书本并不讲解这些，反而是强调，不要滥用RAM模型。言外之意是，这些我就不多说了，只要不按常规来，不乱出牌，基本就ok...... （体会，2.2 第三段的这种含义）。说白了，这里给出RAM模型但是并没有具体解释RAM模型！
3. 数据类型，只强调一点，大小为n的整数可以表达为c lg n比特。言外之意还是，不要乱来即可。（2.2 第四段）
4. 指令、内存层次结构、单cpu、指令的串行执行等等要求都非常常规。（2.2 第五、六段）
5. 指出分析是困难的，但难点是在数学：组合数学、概率论、代数等，跟RAM没多大关系。（2.2 第七段）
6. 最后展望未来，我们还有很多可以选择的计算模型。

总而言之，准确定义计算模型是复杂的，在保证计算模型不被滥用的情况下，我们可以牺牲准确性而得到相应的简洁性与清晰性。对于初入门的CSers，刚学完C语言的同学，刚好你们不懂什么内存层次、并发计算等（即所谓“滥用”之处），所以，把RAM下的程序理解为一般的C语言程序则刚刚好。毕竟你们想滥用模型也往往不知道如何滥用（这样说真的不好吗？）。

##### 2.2.2 插入排序的效率分析

一个实例。   

扩展思考：冒泡排序的效率如何分析？是什么？与插入排序相比，哪个算法更好？或者，各有什么优势劣势？

##### 2.2.3 Worst-case and average-case analysis（难点！）

为何要区分两种不同的效率分析？如何理解这两个概念？我们更需要的是那种效率？

例子：对整数x、y，求x^y需要多少时间？也许我们没有准确答案，大概我们知道计算x的y次方要比计算x+y要耗更多的时间。然而，如果x = 2，算2^y只需要进行y次左移，并不比x + y慢。也就是说，在特定的情况下我们也许会有非常高效的算法，然而在一般情况下，算法需要执行更多的时间。因此我们需要平均复杂性来衡量这样的一般情况。有时候我们对特定情形下的最短时间并不感兴趣，因为我们比较保守，此时我们会问，最多需要多少时间（上界）来完成这项工作。此时，我们考虑最怀情况下的复杂性。

#### 2.3、算法设计

重点：分治法   

实例：归并排序，相信大家可以愉快地阅读下去，请注意Loop invariants的使用。   

提示：递归树是非常好的工具，用起来！

#### 2.4、习题（提示：该做题了！）

#### 2.5、编程题

此题源自于某位同学的提问，课本建议“将插入排序与归并排序结合使用，当一组数的个数足够小时，使用插入排序进行处理，再进行合并”。从而提高排序的效率。问题是如何判断数组个数是多少才足够小呢？我的建议是，编程测试。   

1、设计实现插入排序与归并排序结合使用的排序程序；   

2、设置一个变量控制何时进行插入排序；   

3、对1000k的随机数组进行排序，测试显示在不同的控制下排序的效率。

### 第三章 函数的增长

#### 3.1、Asymptotic notation（渐进表示法）：Big O，Omiga，Theta

术语：上界、下界、紧致界   

简单而言：最多做多少步？最少做多少步？最多做那么多步且最少也需要这么多步！   

难点1：相关计算，多做题！

难点2：恼人的常数c   

同学提问，常数c到底是多少？怎么理解BigO等等表达中需要乘一个常数？

回答：要理解这个恼人的c，首先要明白渐进式表达是一种松散的界，c可以理解为松散度系数。其次我们要理解这个c往往不影响我们的结论，尽管我们不知道它的真实大小。例子：考虑快速排序与归并排序，都是O(n lg n)的复杂度。那么我们可以说它们分别低于c\_1 n lg n   

（记为f）和c\_2 n lg n（记为g），其中c\_1和c\_2是两个不同的常数，我们并不知道具体数值。现在我们想比较这两种排序的大小，因为我们很担心不同的常数项会对我们造成影响，f/g = c\_1/c\_2，得到一个常数！尽管我们还是不知道f/g的大小，但是我们知道这两个数值相比只差一个常数，当n增加得很大的时候，常数不变，往往就显得无关紧要了。值得注意的是，这里只是说，通常情况下c不影响，并不是说常数永远不对算法复杂性有影响。

#### 3.2、标准表达及常用函数

提示：有很多比较难的函数，不一定要死记（能记住也是鼓励的！），先知道，用到了再查。或者在以后以专题的形式重点攻克。比如：Stirling公式。

Side Comments：曾经与某同学讨论算法的学习，他说自己学得很慢，碰到每一个难题都想去解决（不解决就不舒服斯基），不解决就没办法看其他内容。我不很同意这种做法，不懂应该成为常态！要先建立一种全局观，并有整体的思路，允许存在以后解决的技术和理论难点。拿这里来说，两页书的公式包含了很多的数学内容，就单单是一个Stirling公式，我就没有把握需要多少时间去把握它。如果纠结一个Stirling公式而不去看以下的内容，有意义吗？当然，相信这位同学也不是在纠结Stirling公式，只是举一个例子。

提示：除了理解和做题还有什么办法？

#### 3.3、测试

以下测试是在CLRS的作者Cormen的主页上找到的，建议做一做：

* [quiz--comparing-function-growth](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/e/quiz--comparing-function-growth)
* [asymptotic-notation/e/quiz--asymptotic-notation](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/e/quiz--asymptotic-notation)

### 第四章 Recurrences（递归式）

本章讲解三种计算渐进复杂性界的方法：替换法、递归树法以及Master Theorem（主定理？？）

#### 4.1 最大子数组问题

暂略～

#### 4.2 矩阵乘法

暂略～

#### 4.3、替换法：猜一个结果、证明结论（归纳法证明）

技巧1：猜测结果减去一个低阶子项使得证明得证；注意边界条件，可令n 大于某个 n\_0项，使得边界条件成立。

技巧2：换元法，例如，令 m = lg n 。适用于处理递归式中有sqr(n)的情形。

#### 4.4、递归树法

本质上是通过构造递归树，得到一个正确的猜测。还是要通过替换法进行结论证明！

#### 4.5、主定理：菜谱式定理，证明可以先跳过。

目标：给定 T(n) = aT(n/b) + f(n)，a,b > 1，f(n)为正函数。求递归式的界。

直观上（忽略某些细节而言），是通过比较 与 f(n)的大小进行判断:如果前者大，则是；如果是后者大，答案则是；如果一样大，则要乘上一个对数函数子项得到 = 。

思考：为何是比较 与 f(n)的大小呢？   

提示： 是不是等于  ？ 在递归式中代表什么含义？

Comment1：这种方法并不是万能的，有很大的局限。其次，在运用中不能忽略某些细节，比如，大小的比较，在这里要求的是多项式大或者多项式小。

Comment2：第一次阅读不要求证明并不能说明这里的证明就非常难。绝非如此，这个证明没有使用到复杂的技巧，只要把握住“递归树”的思路，理解并不困难。不畏难的同学，在进度跟得上的前提下，可先行阅读。特别是在假设下的证明，不难理解。

Comment3：有意思的是，在应用替换法、递归树法、主定理方法做题的时候，同学们都会很自觉地根据自己的喜好进行选用。实际上，他们应该是对这三种方法有自己的评判和选择（能说是偏见吗？），但是又不自觉地归纳总结出来。比如，有同学认为替换法很随意，也难以猜对，所以不使用。又比如：有同学认为Master Theorem只是套公式，是死记硬背，没什么意思，也不选用。然后，认为递归树法比较靠谱。其实，我认为这样的理解都颇为片面。

首先，我提倡大家猜！要知道能建立一种直观是非常重要的，不要忘记，“猜”就是一种能力，在科研起步的早期，使用“猜”的方法去培养直观可又大收获。其次，使用递归树法不要忘记证明！递归树只不过是帮助猜测的的一种方法，结论必须得到证明。第三，有菜谱为何不用？没错，是死记硬背，不要忘记，“记忆力”就是智商的一种！而且，这套方法是前人经过整理证明出来的有效方法，可直接使用，因为担心自己不理解而不去使用算不算“因噎废食”？

因此，在此我提倡，做题的时候三种方法都使用起来。首先猜，猜对猜不对都要去猜一下。其次，画递归树，能画不能画都去尝试一下。如果递归树或者替换法能得到答案，最后用Master Theorem验证一下自己的答案。

当然，这并非万能方法。也许我们可以不断积累技巧，其中，“换元法”我还是建议大家多多练习。

*2016年3月注记：最近，15图灵班对“主定理“的证明进行了讨论，也是本学期的第一次讨论。效果不错，讨论热烈。讨论过程表示，同学们基本上理解了该定理，也掌握了其中基本的证明技巧。相信，继续下去，这个讨论班会有较大的收获。*

#### 4.6、做习题检验这三种方法。本章强调练习！

### 第五章 概率分析与随机算法

建议在没有概率论基础时忽略。当然，这里要求的概率基础也比较少。建议掌握一些相关概念，比如，什么是概率分析，什么是随机算法。

**期望大家走到这里的时候不要超过一周时间！**

**补录：**   

在实际的学习过程中，我还是坚持要求学生们进行了概率分析的学习，困難是他们没有上过概率课。因此，简单地补了几个概念：示性随机变量、期望值、期望的线性性。结果，此章的内容可以顺利完成。

这说明：在需要的时候对某些知识点进行补充并非不可能完成的任务。反过来证明了那些在此却步的同学并非能力不足，而是信心不足。

第二部分 排序与序性统计
------------

这一部分出了讲排序等算法之外，实际上也讲了一种简单数据结构--数组和堆。

### 第六章 堆排序

#### 6.1 堆

堆可以视为一种完全二叉树，也可视为数组。理解堆的关键不在堆本身，我宁愿大家先理解完全二叉树。估计，作者此处假设读者已经掌握了一定的树的知识。如果你在第一次阅读碰到困难，不妨停下来看看树的概念，并画一棵树，然后体会、理解、证明几个关于树的结论。

**树的概念**：根、节点、叶子、左儿子、右儿子、父节点、树的高度

**关于树的结论**：n个元素的完全二叉树的高度是floor(lg n)；高度为h的完全二叉树的元素个数最多（最少）是多少？n个元素的完全二叉树，叶子的数目最多是多少？这些结论通常可以自己总结，然后用归纳法进行证明。

#### 6.2、堆的操作与堆排序

有了树的概念之后，堆的操作与堆排序都是容易理解的。

#### 6.5 优先队列

### 第七章 快速排序

这一章可说的东西暂时不多。相信大部分同学已经知道并学习过这个算法。与之前学习稍有区别的是，这里是讲两个版本的快排算法：确定性算法与随机化算法。后者与前者只有微妙的区别，就是在选择主元的时候是均匀随机地选择。

对随机快排的**思考**：为什么需要这样做？何时需要这样做？这样做得到什么好处？

这一章的难点在QSort的效率分析。由于是概率分析，在没有概率基础的情况下，暂时跳过。

排序算法的两种**重要属性**：in-place 和 stable。

QSort中的Partition方法比较，这篇[Blog](http://cs.stackexchange.com/questions/11458/quicksort-partitioning-hoare-vs-lomuto)的回答真是太专业了。为什么Hoare的Partition算法更有优势反而不写在正文，留做思考题呢？

**经验教训**：简单的概率知识作为CLRS的先验知识还是非常有必要。实际上，所需要的概率知识也不是很多，应该在第一学期就适当地让同学们掌握。比如，使用Pass等人的[Discrete Mathematics](https://www.cs.cornell.edu/~rafael/discmath.pdf)的Lecture作为基础就不错。

### 第八章 线性时间排序算法

1、排序算法的下界   

利用判定树模型证明所有使用元素对比的排序算法的复杂度下界是。基本思路：判定树是一棵二叉树，中间节点是元素之间的对比，叶子是排好序后数组下标的全排列（有点绕口）。如果有n个元素，则数组下标的全排列有n!种可能，即判定树的叶子个数（记为l）至少有n!个。二叉树的树高为h，它有多少叶子？把以上推理记为：n! <= l <= 2^h 。简单计算得出结论。

难点在于判定树模型，为何可以把HeapSort、QSort、MergeSort等等使用对比的排序算法的行为抽象为判断树？我暂时也没有非常合理简单的讲解可以提供，需要大家自己体会。其实我看书本也没能解释得很清楚。总而言之，结论非常重要。

扩展思考、练习： 如何比较HeapSort、QSort、MergeSort的优劣？它们都有相同的复杂性，而且已经达到最优，说明它们的性能相同？最好用实践来检验，任何已知结论都不可靠，需要验证。

2、计数排序   

这是一种具有线性复杂性的排序算法，当然，有优势必然要付出一定的代价。   

思考：这里的代价是什么呢？

基本思路：所有待排序的元素（或用于排序的关键字）都是某个范围之内的整数值。首先，输入待排序的数组A，统计其中某个数值出现的次数，存于C数组；从而得出小于或等于某个数值的数值的个数，还是存于C数组；最后，根据C数组的统计，将A数组中的元素放入数组B合适的位置中，B即为输出。这三个步骤都是线性时间的复杂度，加起来依然是线性复杂度。

3、基数排序   

基本思路：首先，把待排序元素的键值分成d个数位，每个digit有k个可能值。然后使用具有stability属性（比如，使用计数排序）的排序算法，分别针对d个数位进行排序。复杂性：Theta(d\*(n+k))。基数排序的快速依赖于它调用的计数排序。

思考：线性时间的基数排序是不是击败了其他所有的排序算法？为何？

4、桶排序   

基本思路：对n个元素进行排序，均匀随机地将这n个元素丢入n个桶之中。每个桶都有一个编号n\_i，编号越小的桶里面的元素就越小。使用插入排序对桶中元素进行排序。按桶编号顺序输出桶中元素。

复杂性分析：里面用到了随机变量、随机变量的期望等概率论中内容。抛开这些不谈，能不能从直观上看到某些东西呢？把n个元素丢入桶中需要的时间是Theta(n)，然后对n个桶中的元素排序。每一个桶假设有n\_i个元素，那么就需要O(n\_i^2)的时间（插入排序！）。拍脑瓜的时候来了，均匀随机地在n个桶中放n个元素，平均（所谓期望无非就是平均）每个桶里面有多少个元素？如果你算对了，书上的那一堆吓人的公式大概都是浮云了~

提示：桶排序使用了特定的数据结构，可在后续数据结构的内容学完之后再对桶排序进行编程练习。

### 第九章 中值及序位统计

本章最难懂不是其算法，而是其标题（吐槽！）。中文版直接将Statistics翻译为统计学（“中位数和顺序统计学”）让人摸不着头脑。实际上，本章只是考虑对n个元素求其最小值、最大值和中间值；一般化地，求n个元素的第i小的那个元素，称为Selection算法。

1、最大值与最小值   

简单思路： 按顺序从第一个元素开始，逐个元素对比，并保存下当前最大（最小）的元素位置。Theta(n)的复杂性。

疑问：这样做是不是最好的做法（常用词：optimal）呢？答案，yes！继续提问：why？

稍微难一点的问题：如何同时求最大值与最小值。

2、平均复杂性为线性时间的Selection算法   

思路：使用QSort算法对数组进行划分的思路，是一种分治法，使用了递归。   

提示：放心跳过大量的概率复杂性分析。

3、最坏情况为线性时间的Selection算法   

思路：   

复杂性分析：

第二部分结束。个人认为，第二部分的内容比第一部分稍容易，除了概率分析（刚好大家也可以跳过）之外，没有什么理论难点。所以，期望大家走到这里只是第二周学习的结束。无论你认为是快还是慢，都可以反思一下，为什么？也可以进行讨论。

第三部分 数据结构
---------

相信CLRS的作者会假定自己的学生或者读者懂一点点数据结构，但是要求掌握的并不多（也许这种要求之低可以低到以至于可以忽略）。因此，在引入数据结构的时候，作者强调了“动态集合”的操作：检索、插入、删除、最小值、最大值、前驱成员、后继成员等，完全是高度的抽象。字典是本章主要考察的实现对象。

反思：在学习CLRS之前是否需要集合论及简单的数据结构知识？尽管不知道大家如何想，实际上，如果CLRS是第一学期之后学习，要满足这两种前驱知识的需求也并不难达到。

注意：本章强调实践，使用C++及OO编程的技术做完本章习题，基本就覆盖了普通Data Structures with C++ 的内容（我对比了William Ford的《Data Structures with C++》的目录得出此结论）。如果我的学生可以完成这些内容的学习，就必须问一句：数据结构还必须那样教吗？

### 第十章 基础数据结构

1、栈与队列   

应该没有什么难度，大家可以自学并实现相关算法。自觉利用OO编程，设计相关的Object。

2、链接表   

唯一的难点在于：指针！所以，还是认为第一学期的课程必须包括指针编程的训练。

3、实现指针与对象   

这一节讲解如何在不提供指针与对象的程序语言中实现指针与对象。很奇怪的目的，是吗？因为我们现在大部分的语言都已经实现了指针与对象。所以，看完这一章感觉不奇怪的话，那么任务就完成了。不要忘记，C/C++是使用其他程序语言实现的程序语言。我们往往对C语言中的指针运算感到困惑，比如指针的++、--运算，指针的指针，指针的指针的指针等等，扫除这些困惑的一种方法就是了解这种变量的实现方法！（注，问正确的问题，是你走出正确理解的重要一步。）

4、表达有根树   

这一节有两个重要内容：二叉树与带根树的实现方法。需要讲解的内容不多，重点在于通过指针结构实现树及其各种遍历、查询。有根树与二叉树的区别仅仅在于前者的节点会有任意多个后代节点，每一个节点都有一个指针指向自己的父亲节点，也有一个指针指向自己的右边兄弟节点。编程！

第11章 Hash表   

Hash表是实现字典的有效数据结构。Hash表也许会被翻译为”哈希表“或者“散列表”，只是这种翻译也许并不需要。直观而言，字典，即通过关键词检索相对应的数据项。

1、直接寻址   

使用关键词（key）作为存储的检索号（对应一个存储位置：slot）。高效简单，前提是key的范围足够小。

2、Hash表   

与直接寻址相比，这里使用Hash函数将Key映射到一个存储位置K。使用Hash函数的原因是Key的范围很大，但是真正使用到的Key只是一小部分。比如，中国有13亿人口，要存储所有人的个人信息。如果以姓名为Key，这也许是一个无穷大的范围，我们没必要为每一个可能存在的姓名准备一个存储位置。

因此，这里的关键是设计合理的Hash函数。我们要求Hash函数可高效实现，并且尽可能避免碰撞（Collision）。所谓碰撞，即存在两个不同的key，k1和k2，使得h(k1) == h(k2)。首先，我们看Hash函数h的定义，一定要明确，碰撞存在！为什么？

当碰撞发生之后，如何处理存在的冲突呢？ Chaining！

3、Hash函数   

解决上一节遗留问题，如何设计“好”的Hash函数。

a. 什么是好的Hash函数？

b. 使用除法

c. 使用乘法

*\** Universal Hashing 第一次阅读跳过，然而开学后的学习中Universal Hashing依然是可以进行的内容。目前看效果一般，主要是更深入的学习与研究没办法开展。另外就是此内容在表述上不同的教材有一定的区别，也带来一定的困难。不过，依然令人满意。以后可以以专题的形式再次学习。

4.开放寻址   

不使用列表，在数组的基础上直接实现碰撞发生的处理。算法简单，分析有点困难，还是要卡在随机变量及期望！放过定理证明先。

\*5、完全Hash (暂时跳过)

第12章 二叉搜索树   

1、 什么是二叉搜索树 ？   

二叉搜索树是满足以下特性的二叉树：x是树的节点，x的左子树的所有非空节点的key都比x的key要小，x的右子树的所有非空节点的key都比x的key要大。   

三种遍历方式：前序、中序与后序。简单而言，从根出发，有三种选择：先访问根节点再访问子树；先访问左子树，访问根节点，再访问右子树；先访问子树，最后访问根节点。

2、二叉搜索树的查询、遍历   

容易！理解思路：树是一种递归结构，即树的子孙节点都是一棵树。因此，首先通过递归的思路去理解是最合适的。比如：简单的中序遍历来说，输入：一棵树的树根。遍历：递归遍历树根的左子树，访问树根节点，递归遍历树根的右子树。

3、二叉搜索树的插入与删除   

插入算法容易。删除算法稍微复杂。这里要注意，第三版在此处有非常大的改进。我看的是第二版，情况分析是清晰的，但是伪代码经过了整合优化，可读性较差。第三版的Delete算法描述清晰BigO(n)倍。所以，无论多么著名的书，都可以质疑。

一个简单的证明题，用于帮助理解删除操作过程：删除z节点，当其左子树与又子树都不为Nil，找其successor y节点（Case 3） 。请证明，y的左子树必为nil。

若干课外资料：   

a、一份纯C的BST教程，作者声称非常不喜欢理论:-D。   

b、一份Python的BST教程，适当的时候可以学习一下Python。

\*4、二叉搜索树的随机生成   

给定一系列元素，以随机的顺序将它们插入二叉树中。目的，得到一棵“较矮”的树。重点在概率分析。

第13章 红黑树   

本章的主要任务还是与树的高度作斗争，要得到矮的树，关键是要树平衡发展。红黑树是一种特殊的二叉搜索树，每一个节点增加一个颜色属性（红节点或者黑节点），目的是建立平衡二叉树，这是重点也是难点。   

1、什么是红黑树   

红黑树有五点属性需要把握：每个节点不是红就是黑；根节点是黑节点；所有的叶子都是黑；每一个红节点的孩子都是黑节点；每一节点走到叶子的不同路径包含相同个数的黑节点（保证黑高相同，也就保证了树高的平均）。

2、树的旋转   

一种插入、删除的辅助操作，用于保证红黑树的属性。容易～

3、插入、删除   

与二叉树的插入删除主要有一点不同，即插入、删除会导致红黑树属性变化，因此必须修补，使得原有属性得以保持。这里应该算是一个难点，也许是除了数学概率分析之外，数据结构当中的第一个难点。要克服这里的困难应该如何做？建议在阅读了基本内容（先忽略大部分的算法）之后，多用笔纸画图，对不同实例进行分析，比如，在何种情况下插入节点会（或者不会）导致属性改变？首先要通过这种简单的运算得到直观，再详细阅读课本印证自己的观点。简而言之，作图将会给你带来理解上的帮助。

当困难到来的时候、考验到来的时候，离进步就不远了。你只需要深呼吸、沉一口气，把它攻克下来！ 当然也需要讲一点学习技巧。1、手头有笔纸，把5种RBT的属性记下来作参考。2、根据不同的实例不断画图。3、跟着作者的思路，doubly-black node是一个关键。4、对RBT不要着急编程，不要让程序成为你理解的绊脚石。先理解，让程序成为你加深理解的工具。

问题：为何在RBTree中使用T.nil取代原来BSTree中的NIL？   

回答：首先要注意到T.nil是object，具备各种attributes；不同的是，NIL只是一个标记。其次，T.nil的作用很大，书本用了一个高度概况的字眼来描述：处理RBTree处理中的边界条件。实际上，在详细分析算法的时候，对RBTree进行处理的几种操作包括对叶子的操作，比如，旋转。这个时候叶子就不能仅仅是一个标记，而是一个完整的对象。这种情况很多，你如果没有发现，说明你对算法的分析没有覆盖算法执行的许多情形。为什么要统一用一个T.nil？答案就简单了，节省空间。这是一个好问题。如果你没有理解到这个问题的价值，说明你没有真正理解T.nil的作用与意义。

第14章 数据结构的扩展   

本节内容试图在“教科书式”数据结构与“工程实践中”的数据结构之间搭建桥梁，通过实例展示在工程实践中如果扩展教科书数据结构来完成特定的功能、满足相关的要求。大部分的情况下，我们只需要“扩展”教科书数据结构，而无需重新定义全新的数据结构。那些张口就说“学校授课内容很重要，但是......”“老师授课只注重理论，缺乏实践......”的人请闭嘴吧，至少你要明白什么是“工程实践”再说话，明白教科书、老师怎么理解“工程实践”再瞎说吧。

这一部分的内容主要还是关于红黑树。

1、动态序性统计   

红黑树的一种应用，在节点中增加某些信息，用于讲O(n)复杂度的序性统计下降到O(lg n)。可作为第二节的引入。

2、如何扩展数据结构   

四个步骤，一个定理。

3、区间树   

这一节是对第2节所提出方法的具体实例。

本部分难度不大，但考虑到本部分需要大量的编程，10天时间完成吧！搞完了就安心过春节了。

---

第四部分 高级算法设计与分析   

高级，到底高级在哪里？Advanced，我宁愿理解为“更进一步”的。在此之前的算法设计与分析只有分治法，到了这一章我们并不是抛弃分治法另起炉灶，而是，进一步，进一步......，一步一步地使得算法具有更好的效率。如果这么想，整个思路就很清晰了：动态规划这一章就是讲当大问题分解成子问题，如果重复的子问题不断出现该如何解决。贪心算法更进一步，如果子问题的分割在特定问题的时候具有某种可利用的属性，那么我们可以如何优化算法。因此，不要被“高级”吓倒，也不要被“高级”误导：这里的内容不存在更高级别的抽象，而且思路与之前的内容联系紧密，并非逻辑关联性不强的飞跃。因此，第一个问题必须改成：Where do you advance from？

第15章 动态规划   

动态规划只是一个名词，完全无法体现其应有的内涵。

第16章 贪心算法

第17章 平摊分析法   

平摊分析的目的？   

平摊分析的三种方法：累加平均、记账法、势能分析法。   

理解的难度不大。最大的收获在讲解习题、看视频（竞争分析）。   

如何灵活使用？

---

以上内容，从阅读的角度，一个星期也许够了，但是从做题的角度看，我无法估计！建议尽可能快地完成本部分阅读。然后进入一个反馈循环，再阅读再讨论，加强习题。

---

第五部分 高级数据结构
-----------

第18章、B树   

平衡的搜索树，主要用于磁盘检索。每个节点有多个键值，有多个孩子节点。我认为需要提醒的两点：插入只在叶子进行；删除可在任意节点进行。叶子的定义与BST树有重大区别。

第19章、Fibonacci堆   

1、之前有Binary Heap的内容，为何要提出Fibonacci Heap？有何优势？有何劣势？具体操作怎么做？复杂性是多少？解决这些基本问题。   

2、这种Heap与Fibonacci数列有什么关系？这是难点。

第20章、van Emde Boas树   

发明者Peter van Emde Boas，荷兰科学家。简记为vEB树。

第21章、用于不相交集合的数据结构

---

高级数据结构之所有“高级”的原因是什么？ “进一步”，到底是如何进一步的？思考！

---

第六部分 图算法
--------

第七部分 高级专题
---------

---

---

Appendix A. 本文助记符（统一借助LaTex的记号）   

1、"^" 代表“帽子”，N^2表示N的平方。   

2、“\_"代表下标，比如n\_2表示n带下标2。   

3、"\in" 表示集合的包含关系，比如，A \in B表示A集合是B集合的子集。   

4、BigO，Theta，Omiga，一个英国朋友，两个希腊朋友:-D   

5、floor、ceiling，分别代表下取整与上取整的那两个符号。

---

Appendix B. 相关网络资源   

0、[CLRS的主页](http://mitpress.mit.edu/books/introduction-algorithms)   

1、[《算法导论》网易公开课](http://open.163.com/special/opencourse/algorithms.html)   

2、作者之一[Cormen的主页](http://www.cs.dartmouth.edu/~thc/)   

3、作者之一[Rivest的主页](http://people.csail.mit.edu/rivest/)（大名鼎鼎的图灵奖得主啊！）   

4、Khan Academy‘s [algorithms tutorials](https://www.khanacademy.org/computing/computer-science/algorithms)   

5、进阶阅读：[Readings in Algorithms](http://cs.stanford.edu/~rishig/courses/s14.html)，Stanford的一门课程，里面有比较前沿的papers列表，还有我希望大家可以学习的FFT。留给我自己看看。   

6、[Algorithm Unlocked](http://mitpress.mit.edu/books/algorithms-unlocked)，CLRS作者之一的Cormen的新作，据说比CLRS更浅显易懂。我看过目录和部分章节，易懂也许是的，但是内容就少了很多，而且论述的顺序与风格充满了作者的个人趣味。按作者的本意来说，Algorithm Unlocked只是一盘开胃菜，可以作为学习CLRS的辅助阅读。我看确实如此！然而我看不出有任何理由推荐我的学生去看这本书，因为对大部分的人而言这真是很大一盘餐前小点，你很容易就找出很多很多理由拒绝进行这样的学习：哇啊是英语；哇啊真是太理论；哇啊我又不做科学家.....如果你真的下决心去吃它，还不如立即开始CLRS。如果你不下决心，去浅尝则止，收获也不会很多，那还不如不看。（2015年2月5日补记.）   

7、[Algorithms](http://highered.mheducation.com/sites/0073523402/index.html)，Papadimitriou等人2006年出版的一本算法书，我经常翻看，还不错，篇幅小，简洁。有中文注释版名为《算法概论》，推荐购买。这是[一篇网络评论](http://book.douban.com/review/1566749/)。   

8、[Algorithm Design](http://item.jd.com/10155597.html#detail-root-6)，Jon Kleinberg 等人2005年的著作，非常著名。不适合入门，有些高级且较新的内容。这里有[Lecture Slides](http://www.cs.princeton.edu/~wayne/kleinberg-tardos/).（当年大一就抱着它啃的哪位同学估计已经放弃算法学习了吧......）   

9、<http://codeforces.com/>，竞赛网站？据说有很多好的代码。



---


`@bintou`
`2014-06-04 20:15:03`
`字数 1762`
`阅读 2677`


Simple Git
==========

`学习笔记`

---

本文旨在成为最简单的Git入门。贡献归于[Pro Git](http://iissnan.com/progit/index.html "Pro Git")。

什么是版本控制？
--------

控制、管理软件开发中程序版本变化的软件。方便团队协同工作。

* 本地化版本控制
* 集中式版本控制
* 分布式版本控制

目前我们最需要使用的是分布式版本控制。

什么是Git
------

Git是Linux社区在2005年开发的一套开源的分布式版权控制软件，具有简单、高效、功能齐全等特性。可应付各种复杂的项目开发需求。

基本的 Git 工作流程
------------

1. 在工作目录中**保存修改**某些文件。
2. 对修改后的文件进行**快照**，然后保存到**暂存区域**。
3. **提交更新**，将保存在暂存区域的文件快照永久**转储**到 Git 目录中。   
   
   以下将解释这一工作过程。

安装 Git
------

在 Ubuntu 这类 Debian 体系的系统上，可以用 apt-get 安装：

```
  $ apt-get install git

```

估计这里要在命令前加`sudo`。其他系统也相当容易。

初次运行 Git 前的配置
-------------

### 用户信息设置

配置的是你个人的用户名称和电子邮件地址。这两条配置很重要，每次 Git 提交时都会引用这两条信息，说明是谁提交了更新:

 `$ git config --global user.name "Alice Bob"   

$ git config --global user.email alice@example.com`   

也许只有用户信息设置是最致命的，其他的，慢慢学习了之后再配置吧。可用`git config --list`命令查看配置信息。

Git 基础
------

将介绍几个最基本的，也是最常用的 `Git` 命令，以后绝大多数时间里用到的也就是这几个命令。

### 创建Git仓库

有两种方式：创建与克隆。

#### 新建

1. 为项目建立目录，进入目录，执行以下命令： `$ git init`

如果当前目录下有几个文件想要纳入版本控制，需要先用`git add` 命令告诉 Git 开始对这些文件进行跟踪，然后提交：

 `$ git add *.c   

$ git add README   

$ git commit -m 'initial project version'`   

2.克隆   

所谓克隆，即把某项目的 Git 仓库复制一份出来。比如，要克隆 Gnu PG的 Git 代码仓库 gnupg，可以用下面的命令：

 `$ git clone git://git.gnupg.org/gnupg.git`   

这会在当前目录下创建一个名为gnupg的目录，其中包含一个 .git 的目录，用于保存下载下来的所有版本记录，然后从中取出最新版本的文件拷贝。

### 记录更新

工作目录下面的所有文件都不外乎这两种状态：已跟踪或未跟踪。未跟踪文件即不纳入版本管理的文件。已跟踪文件是被纳入版本控制管理的文件，它们的状态初始是*未更新*，经过修改之后变成*已修改*，然后被放入暂存区（状态是*已暂存*），最后提交所有暂存文件到Git仓库，文件状态又变成*未更新*。如此不断反复：

> *未更新*--->*已修改*--->*已暂存*--->*未更新*

#### 检查当前文件状态

用`git status`命令可查看出文件当前状态，比如：

 `$ git status   

On branch master   

nothing to commit, working directory clean`   

如果创建一个新文件 README，保存退出后运行`git status` 会看到该文件出现在未跟踪文件列表中。

#### 跟踪新文件

使用命令 `git add` 开始跟踪一个新文件。所以，要跟踪 README 文件，运行：

 `$ git add README`

#### 暂存已修改文件

要暂存更新过的文件，需要运行`git add` 命令（功能还挺复杂的）。比如，你修改了一个文件叫something.c，运行`git add something.c`就可以把这个文件转为暂存状态。然后你还可以继续修改。此时如果你需要再次运行`git add something.c`命令把文件重新暂存起来。

#### 提交更新

把暂存的文件提交更新，运行命令：

 `$ git commit`   

在此之前，请一定要确认还有什么修改过的或新建的文件还没有`git add`过。

只要在提交的时候，给`git commit` 加上 `-a` 选项，Git 就会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过`git add` 步骤。（提问：哪为何还要`git add`命令？）

### 查看提交历史

想回顾下提交历史，可以使用 `git log`命令查看。

自此你已经学习了最最基本的Git功能，知道如何创建、克隆文件仓库，知道如何暂存、更新。还有很多复杂的功能需要进一步学习，我不会告诉你我还不懂的，不过，我还是要用以下命令撤销我说的这句话：`$ git commit --amend`



---


`@bintou`
`2017-02-07 16:44:44`
`字数 877`
`阅读 4158`


简介Generic Group Model
=====================

`密码学`

---

直观上看，所谓generic group model（通用群模型）就是在考虑群计算的时候不考虑群本身的特定结构，而是通过一种理想化的（类似RO的访问方法）Query来进行群元素的操作。Generic group model首先是Shoup在EuroCrypt97提出的，用于证明DLG问题的下界是q^(1/2)，其中q是所求DLG问题的群的最大素阶子群的阶（order）。

简单而言，通用群的操作（Query）只有两种（给定安全参数与生成元g）：

1、给定，Oracle返回，实际上Oracle并不做群计算，只是返回一个随机数串，然后记录一张查询列表，如果查询过的，直接返回表中的值。

2、给定群上的元和（记住，这两个值可通过上面的查询获得，比如，对应序号，对应序号），和两个小于的值，，返回一个群上的元  。   

Oracle是这样做的，首先根据和得到相应的序号和，查表可得！然后算。再查表，如果表里面有相应的元，则返回表中的值，否则选一个随机值，然后保存列表。

在定义了以上操作之后，解离散对数问题在Generic group model下等于做什么呢？其实就是通过Oracel查询，找到两组不同的数值，使得 。一旦得到这两对值，通过线性方程组可解出，。攻击者当然是ppt的TM，假设做了t此查询，那么在t次查询下，最多t取2的组合个的值会相同，且与q的阶相同，即t^2 = q，即t =q^(1/2)。

Koblitz等人对Generic group model进行了详细的分析，指出这个模型也许比RO还要“强”（糟糕！），详情见[another look at generic group model](https://eprint.iacr.org/2006/230.pdf)。

需要指出的是，在KE与id scheme中，安全证明常常严重依赖generic group model，请在阅读与以后的工作中注意。



---


`@bintou`
`2017-12-01 21:37:08`
`字数 1103`
`阅读 2958`


理解Goodstein定理
=============

`科普` `意识`

---

> 这篇短文的内容主要源自《皇帝的新脑》(Oxford university press, 1999, Roger Penrose)的前言。提出一个问题，给出一个惊人的结论。本文的目的是为另一篇书评收集素材，同时供读者玩赏。

问题1
---

1、给定一个正整数，把它写成以2为基数(base)的表达。

> 比如：给定整数581，可以首先表达为   
> 
> ，   
> 
> 进一步，把指数上的数也表达为以2为基数，得到：   
> 
> ，不断做，最后得到：   
> 
>    
> 
> 显然，如果数字比较大，指数上会不断递增，形成一个塔状，但这不是重点。

2、接下来对所得的数进行如下两步操作：   

- 将数的基数增加1,   

- 对所得数减1.

> 比如：的base增1，得到：   
> 
> .   
> 
> 然后减1，得到：   
> 
> .

解释一下，为何最后的1没有变化呢？因为是，所以不是基数没有变，是变了，但是值不发生变化。**请注意，这是一个关键点！**

3、不断重复第二步的操作：base增1，得数减1。

> 比如：对上面的结果继续操作得到：   
> 
> - base增一： .   
> 
> - 得数减一： .

4、重复以上的操作，似乎可以无限次地做下去，得数不断递增，而且增幅很大。对吗？

### 答案1

Goodstein定理告诉我们：不对！无论我们取什么正整数开始，重复进行这种操作，最终都会停止，得到一个0！

> 例子： 比如，取，读者自己验收一下，收获直观印象，确实会停止。

关于这个内容可以讲很多很多，暂时到此打住，敬请期待完整书评的出现。

问题2
---

一个稍微简化的问题，源自网络。

1、给定任一有限长度字符串，只考虑英文小写字母（a - z）组成的字符串）。

> 例：str = "abc"。

2、定义以下操作

* 删除该字符串的头字母；

> 例： str = "bc"

* 然后对字符串中剩余的每一个字母进行操作：将该字母的后一个字母插入到该字母的右边。‘z’字母后面没有字母，所以不进行任何操作。

> 例： str = "bc"变成 str = "bccd"

请问，对于任何一个有限的字符串，重复以上操作，操作是否会停止，还是会无限次进行？

### 答案2

同样是令人吃惊的答案：对任意给定的有限字符串，重复操作多次之后，操作一定会停止，最后得到一个空串。   

2017.11.30



---


`@bintou`
`2015-09-27 06:49:24`
`字数 2460`
`阅读 2961`


大白话解释中医的“滋补”与“阴阳”
=================

`扯淡`

---

就本人经验而言：国人知道“补肾”这个名词的人多，常挂在嘴边，但是真正理解“补肾”的人少；偶尔有几个知道“滋阴”，但是懂得“滋阴”的更少；能理解“滋阴”与“补肾”两者关系的，更少。反而，我看得更多的是对这种所谓“中医理论”的误解。其实，无论是赞成中医还是反对中医的民众，他们多半对中医毫无了解--实在懒得用“一知半解”这个字眼。那么我就要问，我们是否能用大众都理解的方式来解释一下这些概念呢？本文就此作出尝试，给出概念、公理，让有一定逻辑思维的人自行判断选择在日常生活中所谓的“滋补”行为。如有一定的帮助，善莫大焉。

首先，我们必须给出这样一个概念：**人体由物质与精神（能量）两部分组成，物质是可见部分，而能量（或者精神）是不可见部分。**不妨把物质记为“阴”，把能量记为“阳”。物质是能量的载体，能量控制物质的运作，此为“阴阳相合”。有了这个概念，大家就明白了，所谓“滋阴”其实很简单就是要补充营养，养好你物质上的身体；所谓“补肾”或者“补气”其实是补阳气，是增强你的能量。因为中医认为肾是藏阳的关键部位，所以往往把“补”都归结为“补肾”，其实除了肾需要补阳气，其他脏腑同样需要补，只是大多数人不知道而已。

其次，我们要承认一个公理：**身体(物质）机能良好，则精神（能量）就会凝结为固态（记为“精”）藏于身体之中；如果身体机能发生病变或者遭受损伤，则能量将会由固态转为气态从身体中流失。**最理想的状态当然是身体与能量相辅相成达成一种稳定状态，此谓“阴阳调和”是也。举个例子，比如，人感冒了没有精神。说的是：人遭受了外部病毒的入侵，身体遭受了损伤，然后能量丧失，导致精神不足，仅此而已。那么，那种“神不守舍”、精神无法集中的人呢？当然也是身体出了问题，而不是精神出了问题啊。所以啊，那些失恋导致精神不佳的年青人一定要记得，其实不是精神受到打击，而是自己的身体遭受了打击，才导致了精神的损伤。

或者有聪明的人就会问，我身体好了那么精神就好了，所以，滋阴就等同于补肾？这句话对了一半，“身体好精神就好”是没错，但是“滋阴”并不等于“补肾”。这么想：精神与物质相辅相成，总是某一部分出了问题而导致另一部分也出问题，那就要区分，到底是精神的问题还是物质的问题。也就是，要选择进行“滋阴”还是“补肾”。比如，一个人说自己精神不好，那么要进行的是滋阴还是补肾呢？很简单，如果你看到他面黄肌瘦，那么就要养身体，没身体你怎么补啊？所谓“虚不受补”说的无非就是身体机能太差而已。

话说到此，更聪明的人就会想到，既然身体好了那么精神就好，为何还要补呢？这个问题就确实很关键。以中国目前的状况看，一般人的营养都可以得到保证，身体就应该是健康的，精神也应该是好的。可是，目前国人没有察觉到的是，环境的变化、饮食习惯的变化、作息时间的变化在暗中不断对身体造成伤害，而这种伤害导致了阳气的流失，又因为大家不断地补充营养，比如大量喝牛奶，所以身体的伤害体现不在瘦而是胖。这个“胖”似乎又在提示说，哎，这个人营养好身体好，其实不然，它是提示说，摄入营养过剩，身体无法将其转换为能量，导致营养以一种“坏”的方式存储在体内。

以脂肪肝为例，通常的认识是说这个人摄入了过多营养。如果从另一个方面看，为何你不能理解为这个人消化不好？实际情况往往就是如此。很多得脂肪肝的人都有喝啤酒的习惯，然后西医不认为说啤酒会有什么害，而认为是啤酒的下酒菜过多而导致的脂肪肝。果真如此？如果你能意识到冷冻啤酒将会影响你的脾胃，导致消化出问题，那么你就不大会这样下结论了。请问什么医生敢宣布冷冻啤酒是脂肪肝的元凶之一？

以上这些事例其实只是想提醒说，人是一个系统，各个脏腑间有者错综复杂的关系，如果你不能认识其中关系，只是一味要“补”，通常都会补错，而且效果适得其反。大部分人都需要补，因为现在的环境等实在太差了，然而大部分人都不会补，既然如此，你还补什么呢？现在微信朋友圈关于“补肾”的食品介绍很多，然而作用真的不大，因为阳气并不只存于肾，**补的真谛在于你要发现为何自己的阳（精）会流失**。还有电视、媒体里面各种“男科”广告所宣传的“补肾”其实都是扯，每个人都有每个人不同的情况，何况性功能多半只是植物神经的问题，他们根本不知道肾阳其实是命门火，是管你条命，不是管你床笫之欢的啊！

接下来，我用一个补肾的方子来解释，在中医所谓补肾的大致方略，以提醒大家真的不要乱补。这个方子出自《金匮要略》，如下：

*肾气汤：生地黄 8、山药4、山茱萸4、泽泻 3（盐炒）、茯苓 3、丹皮 3、桂枝 3-5、附子 3（炮）。单位是钱，一钱等于3克。*

这个方子的做法是进行“三泻三补”：首先泻肝、泻脾胃、泻肾，即把这三个部位的不好的物质排出。其次补肝、补肾、补脾胃，即给这三部分更多的阳气。当然，是泻少补多。最后，把阳气压到三阴经里面去生精。好了，也许大家读这些不会懂得什么药物补什么药物泻，不知道什么是三阴经。没关系，这里只是告诉你，补是一个系统工程，不是简单拿个什么大补的药物吃下去就行的。实际上，这味肾气汤可以治疗糖尿病、脂肪肝，也可以用于中年发福的人减肥。只是，如果没有中医的概念，大家不会知道这个方子补肾。

总之，真正需要滋阴补肾的人都是病人，普通人没有这种必要，他们更需要的是规律且合理的作息与饮食，这才是阴阳调和的王道。也许，冬天多吃几斤羊肉就是很好的滋阴，多睡几个懒觉就是补阳，很简单。只是这种简单在现在又显得如此宝贵：加班、熬夜、酗酒等恶习还在损害我们的健康，大量的疾病疫苗、大量的抗生素、莫名其妙的转基因食品等等又使得我们防不胜防。为此，我们必须根据以上给出的原则和公理进行思考，并作出选择。

比如，如果一个民族的阅读量低、做智力题的兴趣不高，意味什么？答：意味阳气流失严重！因为阳主精神。如何给这个民族补肾，是一个庞大的系统工程啊！

为了大白话的效果，本文尽量避免对古典文献的引用，也不试图解释所有的概念，错漏似乎难免。有一点启发就好，不要试图在一篇文章中得到太多的东西。谢谢大家的阅读。



---


`@bintou`
`2022-07-15 19:45:54`
`字数 2168`
`阅读 702`


指数函数与欧拉公式
=========

`教学` `高等数学`

---

指数函数是指。到底这个函数是怎么想出来的？为什么会等于那么一大堆无穷的级数和？是偶然还是必然？是发明还是发现？

以下内容你只需要懂一阶导数，也就是说即使高数挂科者也可轻松阅读。

在没有这个函数之前，也许，数学家是想找一个函数，它的一阶导数刚好是函数本身。如果把一阶导数看为函数所表示曲线的加速度，那么就是说这条曲线的加速度函数就是自己本身。我尚不知道数学家们出于何种动机非要找这样的函数。我猜，欧拉等人很早就发现了这样的函数，比如：

 (公式1）

稍微做一下求导，就发现，。对求导，没了，变成,  变成...... 所以，这个就是我们想要的那个函数，给一个名字，就叫。并且我们知道。

似乎之前的表达是说，我们想要一个函数，刚好，很容易我们就发现了这个函数，happy ending。如果数学家们满足于这个状况，也许就不会出现下面这些内容了。

如果我们不仅仅满足于找到这么样一个函数，通过这个公式进一步问：是不是所有的曲线（函数）都可以表示成的累加()？即，是否所有的函数都会有这样的形状？   

（公式2）

如果是，我们如何求出这些系数，？注意，此时我们可能知道这个函数的另一种表达方式（不是公式2那种），记为。

现在我需要一点高阶导数的内容，其实就是一阶导数不断做下去。如果，在这个点上，，而且, ， ...，即的阶导数等于的阶导数，直到无穷，我们能说与相同吗？似乎我们没有拒绝的理由。考虑一下函数，记住，的导数就是自己本身。

在的情况下，无论多少次求导，都等于！

在的情况下，对（公式2）不断求导得到的是：

， (序列1）

现在要使得这一个数列都等于(因为此时都等于)，且当时，，也就是说：   

，

把它们代入公式2，刚好得到公式1。

到底是那种情况下找到的？我猜是第一种比较直接的方式，后面是一种发现。而且后面这种发现只是欧拉公式的一个阶段性产品。当然，都是猜。因为，是欧拉等人熟知的，所以，有意思的是能否找到其他函数能表示成的累加。比如，、这样的函数跟有什么关系吗？

同样的方法，我们知道如何对函数求导，求得它在的数值，就得到这样的序列：   

 （序列2）   

要求序列1与序列2相等，所以，   



很高兴地发现，偶数项全归了，而奇数项一正一负地摇摆，其实就得到了大家都很怕的那个所谓的"太乐"展式：   

（公式3）

同理，可以同样推理求得函数的表达为：   

 （公式4）

讲到这里，故事的高潮才逐步出现，以上内容其实都还比较简单。只是在这个神奇的数字引入之后，整个世界就开始奔放起来了。所谓，无非是说 。很崇拜提出这个的人！我们如果只是把理解为一个数，实在没有道理不能把它带入到这个函数当中，是吗？现在，我们考虑！

的展开式我们是知道的，不能照葫芦画瓢吗？   



其实我没干太多事情，只是把代入到公式1当中，然后我们再把展开，因为我们知道，然后我们得到一系列数字，有正有负。

关键还有一点，有些没有消掉，我们把不带的归一类，带（只能有一个i哟！）的归一类看看：   

（公式5）   

刚好它等于： ，与公式3和公式4对比一下即得。

这就是著名的欧拉公式！Perfect！

本文的内容归功于MIT的“微积分重点”公开课，我只是简单复述而已。

2022.07.15

---

P.S. 我花这些时间写这个主要是为了说明，这里写的比小强同学说的“欧拉公式可以这样解释： 把它看成沿时间轴（设描述时间）在复平面中做圆周运动呈螺旋向上的图形，投影在时间轴与实轴构成的平面上的图像为余弦波，投影在时间轴与虚轴构成的平面上的图像为正弦波。”要有趣很多。他只写了几行字，大家都看不懂，我写这么多，大家都懂了，相信还能背下来。哈哈，......开心！

P.P.S 这是好多年前写的博客（2014年QQ空间的也许都不是第一个版本），2022年再次编辑发出，其实娱乐的了我自己。也希望大家喜欢。



---


`@bintou`
`2015-09-12 18:17:53`
`字数 4209`
`阅读 5629`


打造华南师范大学的计算机科学铁军--图灵班
=====================

`教学改革`   

作者：王立斌   

单位：华南师范大学计算机学院   

时间：2015年9月   

版本：0.5

---

引言
--

本文简要分析指出近年华南师范大学计算机学院本科教学中的若干核心问题，提出一种新的且有望实现的教学模式，描述相应的目标与策略，并给出初始的教学计划。希望本文可抛砖引玉，引起各方重视，从而可群策群力，最终可实现打造华南师范大学计算机学院的学术精英学生团队的目标。

策划动机
----

计算机学院是华南师范大学为数不多的工科学院之一，在当今信息技术工程人员需求激增的年代，每年为社会输送三百多名IT人才。可以自豪地说，计算机学院同学的就业率与薪酬都居于学校前列。在创新创业、科技创新、学科竞赛等方面，计算机学子也是冲锋在前的骨干力量，取得了不少骄人的成绩。

成绩与危机并存，回顾近年来在本科教学当中的问题，主要可归纳为几点：   

- 科技创新、学科竞赛难以取得高水平的突破，甚至有水平滑坡的趋势；   

- 难以培育出高水平科技论文，与本校兄弟院系相比，我们也处于下游水平，体现出学科教育中重工程、轻理论的倾向，学生们明显缺乏相应的学术科研训练；   

- 学生中蔓延着比较浓重的畏难情绪，没有明确的长远目标，缺乏学习的激情。又因为环境、制度的影响和约束，学生的这种情绪得到了某种程度上的迎合；

每次进行教学改革讨论，我们都能发现很多的问题，但是各种解决方案又往往流于“头痛医头，脚痛医脚”，无法从根本解决问题。同时，老师们也都明白，之所以无法有效解决问题，往往是因为束缚过多。估计不经过“刮骨疗伤”的痛苦难以有大的改进。

比如，在2012年，学院针对相关问题提出了建设“实验班”的举措，至今已经已经招收了三届“实验班”学员。“实验班”的目标就是要培养学术精英，小班授课（30多人），让老师讲更难更多的内容。每位同学都配置一位专业导师，为其解决学术疑难，引导其走人学术前沿。然而三年下来，效果并不显著。“实验班”的建设困难重重：难以建立独立的行政班，没有独立的教学计划，没有行之有效的遴选与淘汰机制，过于短暂（3个学期）的教学过程，难以激发老师的教学热情，等等。使得“实验班”的同学没有得到更强有力的培养，没有发挥应有的力量，没有达到预期的目标。归根到底，束缚过多！

千言万语，解决以上问题无非一句话：让教育回归教育--老师喜欢教，学生喜欢学。“大学之大”也许不仅仅在于“大师之大”，而是在于学问之大。因此，我们需要：老师喜欢教“大学问”，学生努力学习“大学问”。于是我们问，在目前各种体制的束缚之下，回归教育的本源是否可以成为可能？以下我们试图给出一个初始的回应，如果还不能算是答案的话。

目标与策略
-----

我们的目标是：建设“**图灵班**”，让“图灵班”的学员成为计算机学院科学技术的铁军，让他们成为科技创新、学术研究的先锋队。

为了排除之前实验班建设遭遇的困难，我们设想“带着脚镣跳舞”的策略，所有的师生都身于体制之内，然而让图灵班的建设摆脱尽可能多的束缚。归纳为以下几点思路：

1. 学生必须有远大的理想，志于**科研**。
2. 建立独立且相对完善的图灵班教学计划，该计划不从属于本科教学计划；
3. 图灵班学制四年，而非实验班原有三学期的限制；
4. 所有课程使用著名英文教材，小班学习，灵活的授课机制，课程不纳入本科教学计划管理（负面地看，即你不会得到任何的学分）；
5. 建立完善的遴选淘汰制度，吸引优秀的学生，淘汰落后的学生，宁缺勿滥。初步计划10人左右；
6. 必须挣脱“成规”与“利益”的束缚。

以上策略假定学生学有余力，能利用“课余时间”进行更多的课程学习、学术攻关。同时，为了让教学真正回归教学，我们有意识地让图灵班的建设与各种“利益”脱勾：我们不会用学院的支持给予图灵班学员加分政策，也不会给予“保研”的政策倾斜。换而言之，进入图灵班只是因为你愿意学，有能力学。为了保证教学场所与教学资源等得到保障，学院会提供相应的保障措施。

不为图灵班学员配学业导师，换而为学员配科研导师。与学业导师不同的是，还会制定相应措施约定科研导师的指导时间与导师的遴选。

课程计划
----

教学计划主要分为：先修课程、初级课程、进阶课程及科研课程等若干阶段，有些部分可并行展开，比如：进阶课程与科研课程的学习就可以并行开展。

### 先修课程

设定图灵班先修班的目标旨在选拔优秀学员，避免使用以往的一般课程考核的方式，提高学生的区分度。同时，通过先修班也让学员知道图灵班教学的模式及体会相应的学习强度、压力。让进入图灵班的同学是真正喜欢学习愿意学习的同学。

作为敲门砖，特选两门与正常教学计划相对应的课程。

* [How to Think Like a Computer Scientist: C version](http://prof.beuth-hochschule.de/fileadmin/user/scheffler/Lehre/Think-C_v1.08.pdf)或者[How to Think Like a Computer Scientist: C++ Version](http://www.greenteapress.com/thinkcpp/thinkCScpp.pdf)（简记为HTCS）。
* [MIT：Linear Algebra](http://web.mit.edu/18.06/www/index.shtml), [网易公开课上对应的视频](http://v.163.com/special/opencourse/daishu.html)。

HTCS这门课对应大一的“程序设计语言”，所以，不会进行过多的授课，学生以自学为主，老师组织若干讨论和练习。

《线性代数》也是大一主干课程之一，但是，这里使用了完全不同的教材，讲解内容也大相径庭，特别是，针对这一门入门数学课，要求学生完成若干程序项目，不让数学课脱离工程实践。

### 遴选考核

先修课程中学员的表现作为学员遴选的重要指标。到第一学期期末，以这两门课内容为主进行一次选拔考核。最终遴选出优秀学员成为图灵班学员，进入下一阶段的教学。

### 初级课程

初级课程在大一寒假开始进行，主要有两门课：

* 算法导论([CLRS](http://mitpress.mit.edu/books/introduction-algorithms))，[网易公开课视频](http://v.163.com/special/opencourse/algorithms.html).
* 深入理解计算机系统（CSAPP）（第二版），机械工业出版社，R.E. Bryant

虽然是初级课程，但是，我们将这两门课程视为图灵班的核心课程，是重要的“敲门砖”也是课程建设的重点。

首先，安排学生在寒假期间进行自学，老师给出相应的学习指导。其次，在新的学期开始之后，再安排具体的学习计划。需要强调，图灵班的授课一定不会是目前的老师满堂灌的形式。

学期末，再次考核，决定学员是否继续图灵班的学习。

### 进阶课程

进阶课程学习安排在大一结束之后的暑假开始。主要包括以下几门课程：

1. 计算机程序的构造与解释(SICP)
2. 概率与计算，Michael Mitzenmacher
3. 数论概论 (FINT)，J.H. Silverman
4. 计算理论导引，ITOC，M. Sipser
5. Logic in Computer Science：modelling and reasoning about systems，Michael Huth and Mark Ryan
6. 代数，Michael Artin

进阶课程分为几个阶段，而且也不仅限以上书目。根据实际情况再做调整。为配合学术研究及科研项目的申报，图灵班还开设以下课程：

* 科技论文阅读写作

### 科研学术课程

科研导师的指导时间大致在第四学期开始，科研课程由科研导师根据自己的学术兴趣进行安排，包括一到两门专业课，引领学生进入学科前沿。

首先，科研导师提交完善的培养计划，包括课程计划与研究课题计划。其次，学生选择导师。经过双方的双向选择最终学生进入科研团队。

我们强调，科研导师的培养计划必须包括一到两门专业课程的学习，计划中必须指明相应的教材以及授课计划。换而言之，我们不希望图灵班学员进入科研团队只是一个开发人员，而得不到更多的学术培养。

同时在第四学期，根据科研导师拟定的课题计划，学生可撰写研究计划，申报各级各类科技创新、创新创业计划。

### 实践教学计划

图灵班的课程已经包括了许多的实践内容，暂不作列举。学员还会在老师的指导下，针对自己关注的学科问题，撰写一份研究计划或者项目计划。除此以外，图灵班还会倡导开源软件的应用与开发，我们会鼓励学生完全工作在开源操作系统之下，学习各种开源的开发工具，开发更多的开源工具。让学生们得到开源文化的熏陶，从而具备更广阔的国际文化视野。

同时，实践教学内容可以根据实际情况安排不同的讲座，可以是老师，也可以是同学，甚至可以邀请校友回来进行讲演。

结束语
---

本文为图灵班的建设进行各种设想，设计了建设策略，制订了初步的教学计划。坦率而言，这种教学模式并没有什么创新之处：让大学成为大学；让教育回归本源。然而，目前的环境与制度下，也许这些“正常行为”就会稍显另类，任何一小步的改进也许都会遭遇极大的困难与束缚。任重道远！在此呼吁，希望更多的老师、更多的学子可以参与这种正常的教学工作，为打造华南师范大学计算机的学术精英团队贡献力量。

---

### 结束语之外的话

也许有老师会怀疑，以上制订的计划是否过于“高难”，不适合我们华南师范大学这样的小学校。对此，笔者想回应两点：

1. 本文作者尝试过在2014级的同学中进行《程序设计》、《线性代数》、《算法导论》等课程的教学，效果不错，完全可以跟上。这是当时的[授课手记](http://user.qzone.qq.com/1626344361/blog/1422327955)。
2. 本文作者有两位学生，他们都是在本科时候进入老师的科研团队学习工作，然后保研、读研，他们学习过这里推荐的大部分课程。目前这两位都在国外读博士，一位是在波鸿大学的[Jiaxin Pan](http://www.foc.rub.de/people/pan.html.en)，一位是在里昂高师的[Weiqiang Wen](http://perso.ens-lyon.fr/weiqiang.wen/)。

因此，相信这个计划具有比较高的可执行度。而且，如果一个学校不坚持严标准高要求，那不正是教学没有回归教学本身的体现吗？

附录A. 初级核心课程书目
-------------

1. 微积分，James Stewart
2. How to Think like a Computer Scientist[5](http://mitpress.mit.edu/books/introduction-algorithms)
3. [线性代数导论[MIT]](http://web.mit.edu/18.06/www/index.shtml)，G. Strang，
4. 算法导论(CLRS)
5. 深入理解计算机系统(CSAPP) 或 A practical introduction to computer architecture，Daniel Page
6. 计算机程序的构造与解释(SICP)
7. 概率与计算，Michael Mitzenmacher
8. 数论概论 (FINT)，J.H. Silverman

附录B. 进阶核心课程书目
-------------

1. 计算理论导引，ITOC，M. Sipser
2. Logic in Computer Science：modelling and reasoning about systems，Michael Huth and Mark Ryan
3. 具体数学，GKP
4. 代数，Michael Artin

附录C. 没有列入核心书目的好书
----------------

1. [Algorithms](http://highered.mheducation.com/sites/0073523402/index.html)
2. 挑战程序设计竞赛(第二版)，人民邮电出版社，巫俊泽等译.
3. [编译原理：技术与工具](http://dragonbook.stanford.edu/) （Dragon Book），Addison-Wesley.
4. Introduction to Automata Theory, Languages, and Computation([IALC](http://infolab.stanford.edu/~ullman/ialc.html)).
5. 计算机程序设计艺术([TAOCP](http://www-cs-faculty.stanford.edu/~uno/taocp.html))

---


`@bintou`
`2016-01-10 22:14:43`
`字数 2205`
`阅读 2757`


“大禹治水”到底說了什麼？
=============

`歷史`

---

關於大禹治水的故事，國人通常耳熟能詳，無外乎出自太史公《史記》的故事：在人性光芒萬丈的堯舜禹時代，大禹在堯在位的时候就開始治理洪水，他公而忘私，“劳身焦思，居外十三年，三过家门而不入”。然而，故事的版本有很多，奇怪的是並不爲人所熟知。以下故事我命名爲“野史”，其實不少內容出自典籍，非道聽途說。記錄下來，供世人笑談。

首先提到的一個版本出自著名的《山海經》的《海内经》：

```
黄帝生骆明，骆明生白马，白马是为鲧.

洪水滔天。鲧窃帝之息壤以堙洪水，不待帝命。帝命祝融杀鲧于羽郊。鲧复生禹。帝乃命禹卒布土以定九州。

```

這裏說明了黃帝、鯀與大禹之間的關係，也說明了鯀爲何被殺，大禹的出生，以及大禹受命治水的過程。有一點必須指出，在《山海經》講到治水的事情之前曾經有這樣一句：

```
禹、鲧是始布土，定九州。

```

讓人懷疑，鯀禹兩父子曾經並肩作戰共同治水，而且都是用土去堙洪水。意思就是說，禹治理洪水的技能不會比鯀高到那裏去。

以上故事大家可以理解爲一個遠古神話，似乎沒有值得多說之處。只需要記得如果有國學大師冒用《山海經》之名盛譽大禹之功，你可直接無視之。然而，在《史記》中卻是另一種情形。

```
    《史记·夏本纪》载，“夏禹，名曰文命。禹之父曰鲧，鲧之父曰帝颛顼，颛顼之父曰昌意，昌意之父曰黄帝。禹者，黄帝之玄孙而帝颛顼之孙也。禹之曾大父昌意及父鲧皆不得在帝位，为人臣。当帝尧之时，鸿水滔天，浩浩怀山襄陵，下民其忧。尧求能治水者，群臣四岳皆曰鲧可。尧曰：“鲧为人负命毁族，不可。” 四岳曰：“等之未有贤於鲧者，原帝试之。” 於是尧听四岳，用鲧治水。九年而水不息，功用不成。於是帝尧乃求人，更得舜。舜登用，摄行天子之政，巡狩。行视鲧之治水无状，乃殛鲧於羽山以死。天下皆以舜之诛为是。於是舜举鲧子禹，而使续鲧之业。
    尧崩，帝舜问四岳曰：“有能成美尧之事者使居官？”皆曰：“伯禹为司空，可成美尧之功。”舜曰：“嗟，然！”命禹：“女平水土，维是勉之。”禹拜稽首，让於契、后稷、皋陶。舜曰：“女其往视尔事矣。”
    禹为人敏给克勤；其德不违，其仁可亲，其言可信；声为律，身为度，称以出；亹亹穆穆，为纲为纪。

```

這裏，大禹與黃帝之間跨多了好幾代人，與《山海經》相同的是，鯀與禹絕對還是黃帝的直系子孫。多出兩個重要人物：堯與舜。這個堯，據《史記.五帝本紀》，也是黃帝的直系。仔細梳理可知，鯀應該是堯的堂叔叔，也就是說，堯與禹是叔伯兄弟。可是，這個舜呢，竟然是出於民間的一個單身漢！這個正能量滿滿且廣爲流傳的故事是這樣說的：

```
舜从小受父亲瞽叟、后母和后母所生之子象的迫害，屡经磨难，仍和善相对，孝敬父母，爱护异母弟弟象，故深得百姓赞誉。当时帝尧年事已高，欲选继承人，四岳一致推举舜，于是，尧分别将自己的两个女儿娥皇、女英嫁给舜，让九名男子侍奉于舜的左右，以观其德；又让舜职掌五典、管理百官、负责迎宾礼仪，以观其能。皆治，乃命舜摄行政务。

```

舜真是一個民間單身漢嗎？《史記.五帝本紀》：

```
虞舜者，名曰重华。重华父曰瞽叟，瞽叟父曰桥牛，桥牛父曰句望，句望父曰敬康，敬康父曰穷蝉，穷蝉父曰帝颛顼，颛顼父曰昌意：以至舜七世矣。自从穷蝉以至帝舜，皆微为庶人。

```

天啊，舜的爺爺的爺爺與大禹同輩份，這個世界亂了！大家看不清楚沒關係，記住這個人：“颛顼”，窮蟬和鯀的老爸，禹的親爺爺，堯的叔祖爺爺。大家可以把舜理解爲流落之民間的皇親。這之以前很普通，比如大家熟知的劉備不就是一個有皇家血統的賣鞋佬嗎？總之，這裏得到一個結論：堯舜禹三人沒有任何一個是普通的百姓，都是黃帝的直系後人。

這裏岔開題不講大禹而講舜的身世，有什麼意思嗎？當然了，只要細讀《史記.夏本紀》的故事，你就會發現它令人想象的空間比《山海經》裏面的神話故事要大得多。爲何這麼說，大家請注意鯀治水的始末。

當堯問誰可治水的時候，羣臣都推薦鯀，堯怎麼說？嗯，這個人人品很壞，不聽命令，會毀了自己的族羣，不可以！衆人力薦之下，堯同意讓鯀去治水，結果鯀治水治了多少年？九年！一個治理洪水不力的水利局局長連任九年，也是奇怪！治水不成，堯應該怎麼做？當然是懲罰鯀，至少來個免職吧。情況並非如此，“於是帝堯乃求人，更得舜”。爲什麼是先找接班人？接着舜代理堯巡視天下，“行视鲧之治水无状，乃殛鲧於羽山以死。”。“治水无状”根本就是堯找繼任者的原因，舜又何必巡視然後下手殺人呢？“於是舜举鲧子禹，而使续鲧之业”也頗令人意外。總之，這一系列細節都值得玩味。

如果有人以春秋筆法寫書，大概可以這樣：鯀是能人，治水九年，功高震主，主上不安，找個接口，讓自己的繼任者出手殺人，然又考慮到時局的穩定性，隔代指定接班人，於是成全了大禹治水之美名。

不過，這種猜想實在過於迂腐，而且也過於輕率地認識政治鬥爭的冷酷性。因爲還有另一種可能的真相。《竹书纪年》记载：

```
尧之末年，徳衰，为舜所囚。舜囚尧,复偃塞丹朱,使不与父相见也。舜囚尧于平阳，取之帝位。

```

丹朱是堯的兒子，據說不肖，所以堯不傳位與他。假設上面這一段爲真，那麼舜勢必需要擊殺鯀以鞏固自己的地位。至於舜與禹之間發生了什麼，哪就不得而知，反正《韩非子·说疑第四十四》有這樣一句：

```
舜逼尧，禹逼舜，汤放桀，武王伐纣，此四王者，人臣弑其君者也，而天下誉之.

```

禹是怎麼逼舜的,這有待查證。然而到此打住，讀者自行回味一下大禹的正能量故事，以鼓勵自己對歷史有更深刻的認識吧。借一句名言：也許認識歷史就是爲了更好地認識現在。



---


`@bintou`
`2019-08-15 18:33:07`
`字数 5607`
`阅读 1950`


《给巴黎一位小姐的信》 by 胡利奥·科塔萨尔
=======================

`短篇小说`

---

> 摘自《动物寓言集》，推荐给大家阅读。

安德烈娅，我原本不想搬来您在苏伊帕恰街的公寓。不是因为小兔，更是因为闯入一个封闭的秩序让我痛心。您的家里，薰衣草的香味、白天鹅般纯洁的你舞动手臂、拉腊四重奏里小提琴与中提琴的合奏，停留在空气中，交织出精致细密的网，秩序也渗透其中。生活优雅的人，将环境布置成看得见的灵魂翻版：这里是书（一边是西班牙文的，另一边是法文和英文的），那里是绿色的靠垫，小茶几的这个固定位置放着玻璃烟灰缸——好像肥皂泡切下了一块永远有香味、声音、生长的盆栽、逝去友人的照片、茶具和方糖钳……进入这样的环境让我苦恼。啊！亲爱的安德烈娅！即便全身心地认同这一切，破坏一个女人在她的温馨小屋建立的细致入微的秩序该有多么艰难！拿起一只小金属杯，把它放到桌子的另一边——这么放只是因为搬来的人把英文字典拿了过来，放在这一边手够着方便——会产生多大的愧疚！移动那只杯子，意味着和谐的奥尚方格调中突然出现一抹可怕的红，意味着莫扎特交响乐寂静无声的那一刻，啪！让人一惊，所有低音提琴的弦突然崩断。移动那只杯子，破坏了整个屋子的相互关系，一件物品和另一件物品的相互关系，杯子灵魂和屋子灵魂以及远在他乡屋主灵魂之间无时不在的相互关系。我无法做到用手指碰一本书、微微聚拢灯光投下的区域、打开音乐盒的盒盖时，冒犯和挑衅不像一群麻雀在眼中一闪而过。

您知道我为什么搬到您家来，搬到正午宁静的客厅来。倘若不洞识真相，一切似乎自然而然。您去了巴黎，我住在苏伊帕恰街公寓，安排简单，却各得其所。九月，您会重回布宜诺斯艾利斯，我会搬到另一个住处，那儿也许……不过，我给您写信不是要说这些，写这封信是因为兔子，我觉得应该告诉您关于它们的事儿，是因为我喜欢写信；或许，也是因为下雨了。

我是上周四下午五点搬的家。当时，天，雾气弥漫，我，满心厌烦。一生中，我关上过那么多次箱子，我花了那么多时间无目的地整理行李，以至于上周四那天充满了皮带和阴影。我看到箱子上的皮带，就如同看到皮带投下的阴影，它间接地、十分轻微却又十分可怕地落在我身上。不过，我还是理好箱子，通知佣人过去帮忙，走进电梯。就在一楼和二楼间，我感觉要吐出一只兔子。之前，我没跟您提过，您别认为我不坦诚，谁也不会告诉别人自己时不时会吐出一只兔子。每次都是一个人的时候吐，和许多发生在（或人为安排发生在）绝对隐私时刻的事一样，我选择闭口不提。别怪我，安德烈娅，您别怪我。时不时地，我会突然吐出一只兔子。这不是无法随意选择住处的理由，不是让人自惭形秽、离群索居、沉默寡言的理由。

每当我感觉要吐出一只兔子时，我就把两指张开，呈夹子状，放入嘴中，期待暖暖的茸毛如水果味助消化泡腾片一般从喉咙里冒出来，卫生、迅捷、一蹴而就。我拿出手指，指上夹着小白兔的一双耳朵。小兔看上去很高兴，正常得很，没有缺胳膊少腿，只是个头小，非常小，兔形巧克力大小，不过是白的，一只完整无缺的小白兔。我把它放在掌心，手指轻轻扶起它的茸毛。小兔似乎对降临人间十分满意，动个不停。嘴巴贴着我，静静的，痒痒的，在掌心里蹭来蹭去。它在找吃的。于是，我——当时我还住在郊外，说的是那时的情况——带它来到阳台，把它放进特意种植的三叶草大花盆。小兔竖直耳朵，以迅雷不及掩耳之势一头扑进柔嫩的三叶草丛。这时，我知道可以扔下它，走开，继续过一段无异于众多去农场购买小兔者的日子。

在一楼和二楼间，安德烈娅，似乎是提前预告我在您家的生活状况，我知道要吐出一只兔子，当时我就害怕了（要不，是奇怪了？不，也许是又害怕又奇怪）。搬家前，短短两天前，我刚刚吐出过一只兔子，以为一个月、五周、运气好也许六周内会平安无事。您瞧，小兔子的问题我处理得妥妥当当。我在那个家的阳台上种三叶草，吐出一只兔子，放在三叶草上，一个月之后，当我估摸着没准什么时候……我就把长大的兔子送给莫利纳夫人。她相信人各有癖好，从不乱发议论。这时，另一个花盆里柔嫩的三叶草又渐渐长到合适的大小，而我，不慌不忙地等着早上毛茸茸痒酥酥的小家伙顺着嗓子眼往外冒，新来的小兔重复以前那只小兔的生活和习惯。安德烈娅，习惯是节奏的具体表现形式，是节奏的一部分，帮助我们生活。一旦进入固定不变的循环周期，一切条理化，吐出兔子就没那么可怕。您也许想知道为什么要费这么大的事儿，种三叶草，还要送给莫利纳夫人，立马杀掉不是更省事……唉！您也应该吐只兔子，就一只，两个指头夹着，放在掌心。它是那么的弱不禁风，带着难以言表的光彩霎时俘获您的心。一个月对它而言天差地别。一个月意味着个头大了，毛长了，会跳了，眼神野了，天差地别呀！安德烈娅，一个月意味着一只大兔子，意味着兔子真正长大。可是，开始一分钟，它是温热蠕动的一团雪，包裹的是一个无可替代的小生命……开始几分钟，它是一首诗，以土买一夜的灵感：生于我，融于我……之后，不再是我，茕茕独立，拒人于千里之外，置身于白色、平坦、信封大小的世界里。

无论如何，我当时决意将小兔扼杀在摇篮里。我要在您家里住四个月——运气好一点的话，也许，三个月——喂几勺酒就成。（您知道要想慈悲为怀，只需喂小兔一勺酒，便可立刻置它于死地吗？据说，这样一来，兔肉会更香，尽管我……三勺或四勺酒，之后扔进厕所或包起来扔进垃圾箱。）

电梯通过三楼时，小兔在我掌心里动来动去。萨拉在楼上等我，准备帮我把箱子拿进屋……怎么跟她解释才好？个人癖好？动物商店？我用手帕包住小兔，放入大衣口袋，把大衣松开，免得挤着它。它几乎一动不动。微小的意识恐怕在向它传递着重要的事实：生命是往上一纵，“咔嗒”一声结束；生命也是白色、环绕的低空，有股薰衣草味，在一口温热的井底。

萨拉什么也没看见，已经有一道超级难题令她几乎无所适从：如何将她的秩序意识贯彻到我的衣箱和纸张上。她深思熟虑的解释充斥了“比如”之类的字眼，而我对此丝毫提不起兴趣，找着机会就把自己锁进卫生间：现在动手，干掉它。手绢周围一片温热，小兔雪白无暇，看起来比过去任何一只都美丽百倍。它没看我，只是翕动，只是兴奋，堪称最可怕的注视方式。我把它关进空药箱，回头接着拆行李，脑子有些茫然，但不用痛苦，不用负疚，不用打肥皂洗去小兔的最后一阵抽搐留在手上的感触。

我明白：杀它我下不了手。可就在那天晚上，我吐出了一只小黑兔。两天后，一只小白兔。第四天晚上，一只小灰兔。

您应该很喜欢卧室里漂亮的衣柜，衣柜的门很大，打开门，一切尽收眼底，木板上空空如也，等待着我的衣服。如今，我把它们放在那里。那里面。看起来完全不可能，就算跟萨拉说了，她也绝不会相信。萨拉一点也没怀疑，她不起疑心，是因为我准备工作做到家了。就这么一件事，让我搭进去多少白天黑夜。它时时焚烧着我，让我的内心日益坚强，好比您放在浴缸里的那只海星，每次洗澡，都让人感受到充足的盐分、阳光的灼射和海底的喧嚣。

白天，它们睡觉。一共十只。白天，它们睡觉。门关着，衣柜对它们而言是白夜。在那里，它们乖乖地安然入眠。我出门上班，把卧室钥匙随身带走。萨拉恐怕以为我对她缺乏信任，向我投来狐疑的目光，每天早上我都见她欲言又止，最后选择闭口不言，而我心花怒放。（九点至十点，萨拉打扫卧室，我在客厅里制造声响，放一张班尼·卡特的唱片，声音传遍每个角落。萨拉也爱听宗教短歌和斗牛舞曲。衣柜看上去一片寂静，也许，它确实没有发出任何声响，对于小兔们来说，那是夜晚，应该休息。）

小兔们的一天从晚饭后开始。伴随着方糖钳的叮当作响，萨拉撤去晚餐托盘，向我道了声晚安——没错，她向我道晚安。安德烈娅，最令我觉得苦涩的是她居然向我道晚安——走进自己房间。突然，我孤身一人，独自面对可恶的衣柜，独自面对我的责任和我的悲哀。

我把它们放出来，让它们轻盈地跳进客厅，它们兴奋地闻到了原本藏在我口袋中的三叶草的味道。现在，三叶草星星点点地铺在地毯上，被它们搅乱、移动、霎时消灭在肚子里。它们吃得很好，循规蹈矩，不声不响，那一刻，让我无话可说，只是徒劳地拿着一本书——安德烈娅，我很想读完您家里所有季洛杜的作品，还有您放在书架最底层的洛佩斯的阿根廷史——，坐在沙发上看它们，看它们吃三叶草。

一共十只兔子，几乎全是白的。抬起暖暖的小脑袋，看着客厅的吊灯，它们的“白天”里那三盏永远不动的太阳。它们热爱光线，因为它们的“夜晚”没有月亮，没有星星，没有路灯。它们看着三轮太阳，满心欢喜，在地毯上、椅子上蹦来跳去。十个不起眼的小斑点如时刻转动的星座动个不停，我希望看到它们一动不动地伏在我脚边——有点像造物主做的梦，安德烈娅，造物主们无法实现的梦——而不是在米盖尔·乌纳穆诺的照片后面、淡绿色的花瓶旁边、黑洞洞的写字台下面躲躲闪闪。总是不到十只，总是六只或八只，我问自己，少的那两只究竟躲在哪儿，萨拉会不会因为什么事起床，还想着洛佩斯的阿根廷史我想读里瓦达维亚统治的那一段。

我不知道这样的日子该怎么熬，安德烈娅。您应该记得我是来您家休息的，如果搬家也扰乱了我的生物钟，时不时吐只兔子可不是我的错——不是唯名论，也不是巫术，只是事情不能说变就变。有时，您等着别人扇您右脸一个巴掌，谁知道突然间变了方向——就是这样，安德烈娅，具体情况会有出入，可道理就是这样。

我在晚上给您写信。现在是下午三点，我在它们的晚上给您写信。白天，它们睡觉。办公室里一片大喊大叫的声音、发号施令的声音、皇家打字机的声音、副社长们的声音和油印机的声音，多放松！安德烈娅！多放松！多太平！多恐怖！现在，有人给我打电话，是那些奇怪我晚上太安分没活动的朋友们，是路易斯邀我散步，是豪尔赫约我听音乐会。我几乎不敢回绝他们，只好编些又长又假的借口，身体不好啦，赶翻译稿啦，胡乱搪塞过去。等我回到家，进了电梯——那一段，一楼和二楼之间——便夜复一夜、于事无补、徒劳地希望这一切不是真的。

我尽量不让它们损坏您的物品。它们咬坏了一点点书架底层的书，您会发现被遮得很好，免得萨拉察觉。您很喜欢那盏画满蝴蝶和古代骑士的大肚子瓷灯吧？碰坏的地方基本看不出，我用英国商店买来的特殊水泥修补了一晚上——您知道的，英国商店里有最好的水泥卖——而现在，我就坐在灯旁，免得哪只兔子又对灯伸爪子。（它们喜欢一动不动，看上去几乎是一幅美景。它们也许在怀念遥远的人类，也许在模仿它们的造物主。造物主走来走去，严密注视着它们的一举一动。还有，您恐怕注意过——也许小时候注意过——可以罚小兔子面壁，前爪靠墙，一动不动好几个小时。）

凌晨五点（我躺在绿沙发上，只睡了一小会儿。毛茸茸的脚一跑动，发出一丁点声响，都会把我惊醒），我把它们放进衣柜，打扫卫生。所以，萨拉会发现一切如常。尽管有时我会见她暗自吃惊，盯着什么东西看，发现地毯微微有些褪色，又想开口问我点什么，可是我吹着弗兰克的交响乐变奏，不予理睬。安德烈娅，大清早的，不声不响地清扫植物，这些琐事并不光彩，干嘛非要说给她听？半梦半醒地捡起三叶草的茎，散落的叶子和白毛，磕磕碰碰地撞着家具，迷迷糊糊地困得要命。纪德的翻译拖了，特罗亚的翻译还没弄，要给远方的一位女士回信，她恐怕在问是不是……干嘛还要接着做这个？干嘛还要在电话和采访之间接着写这封信？

安德烈娅，亲爱的安德烈娅，让我宽慰的是只有十只，不再增加了。十五天前，我在手掌上放下最后一只小兔，之后再也没有了，只有十只。在我的白天，它们的黑夜，它们渐渐长大，变丑了，毛长了，进入少年期了，急不可耐了，花样百出了，跳上安提诺乌斯的半身塑像（是安提诺乌斯吧？那个瞎了眼盯着人看的小伙子？），消失在起居室里，弄出很大的声响，我赶紧把它们赶出来，担心萨拉听见，惊恐万分地出现在我面前，没准还穿着睡衣——萨拉一定是这副打扮，穿着睡衣——那样一来……只有十只，您可以想象置身其中的我所能感受到的一丝快乐，还有回家穿越一楼和二楼既定空间时心头越来越多的踏实。

我要出门办事，只好把信放下。微亮的晨曦中，安德烈娅，我在家里接着给你写。真的是第二天了吗，安德烈娅？信纸上空一行对您而言意味着间隔，对我而言意味着一座连接昨日书信和今日书信的桥梁。告诉您，在间隔时间里，一切都乱了套。在您看到的这座桥上，我毫不费力地听到水流中断的声音。对我来说，纸的这一边，信的这一边不再有搁笔办事前的踏实和镇定。在没有悲伤、立体的夜里，沉睡着十一只小兔子，也许就是现在，不，不要现在一之后在电梯里，或者，进门时。无所谓地点了，无所谓是不是现在，无所谓是我残生的哪一刻。

好了，我写这么多是想告诉您糟蹋了您的家并不全是我的错。我把信留在这里，等您回来看，让邮差在巴黎哪个明朗的早晨把信直接交到您手里不太像话。昨天晚上，我把第二个书架的书倒了个方向，它们能够得着了，站着或跳着啃书脊磨牙——不是饿的，我给它们买了足够的三叶草，就放在写字台抽屉里。它们咬破了窗帘、椅垫、奥古斯都·托雷斯自画像的边缘，地毯上到处是兔毛，它们还叫，在灯光下围成圈，崇拜我似的围成圈，突然叫唤起来，我还以为兔子是不会叫的。

我想把地毯上的兔毛收拾干净，把咬破的椅垫边弄平整，把它们重新关进衣柜，可是我做不到。天要亮了，也许，萨拉一会儿就要起床。真奇怪，我不在乎萨拉了。真奇怪，我不在乎看着它们蹦蹦跳跳地去找玩具了。并不全是我的错。等您回来，您会看到许多破损我已经用英国商店买来的水泥修补好了。我尽力了，不想惹您发火……而我，从十只到十一只是一道不可逾越的坎。您瞧：原本十只挺好，有衣柜，有三叶草，有希望，多少事儿都能做成。可是，十一只不行，因为安德烈娅，有十一只就有十二只，有十二只就有十三只。天亮了，寒冷的孤独中有欣喜，有回忆，有您，还有很多很多。苏伊帕恰街上的这座阳台洒满晨曦，迎来都市的第一阵喧嚣。我觉得收拾散落在路面上的十一只死兔子没什么难的。也许，根本没有人会注意到兔子，他们要赶在第一批学生经过之前，运走另一具尸体。

---

20190815



---


`@bintou`
`2016-10-12 00:17:38`
`字数 1337`
`阅读 2247`


程序、竞赛与算法
========

`程序` `竞赛` `算法`

---

最近我抽空关注了一下某些程序设计竞赛的书。我是竞赛盲，没有参加过任何程序竞赛，不过我就喜欢折腾、瞎想，顺便也与几位搞过ACM竞赛的同学探讨探讨。

首先，我就找了某同学推荐的《挑战程序设计竞赛（第2版）》（ 作者: 秋叶拓哉 / 岩田阳一 / 北川宜稔 出版社: 人民邮电出版社 译者: 巫泽俊 / 庄俊元 / 李津羽 出版年: 2013-6）翻看了一下，挺有意思。加上我之前买的刘汝佳的几本竞赛书，我对程序竞赛有了一点点认识。我就想，一本讲竞赛的书与一本算法书有什么区别呢？比如，《算法导论》？

然后我就进行了一些比较，主要是针对《挑战程序设计竞赛》和《算法导论》。我发现，从内容的组织上有非常类似之处：从基本的数据结构出发（堆、栈、树、图），讲解一些基本的算法，然后贪心法、回溯法，进而动态规划，网络流，计算几何，再加上一些数学知识，主要以数论、组合数学为主的知识。尽管类似，但是又有非常明显的区别。（《数据结构》、数论、概率等本身就独立成课，使得分析下去会更复杂。《算法导论》有数据结构的内容，但显然这部分内容并非必须。）

主要体现在，竞赛书的讲解主要针对特定的题目，强调技巧和程序。算法书针对已知难题，强调准确性、系统性和通用性。我列表如下，其中有些结论我心目中不是那么武断，只是写下来就成了这个样子，大家可以探讨：

```
           目标       系统性  理论性  技巧性   关注点    趣味性  学习要求
 算法学习： 学科训练     强      强     较弱    通用难题   较弱      高
 ACM竞赛：  比赛        较弱     弱     强      特定问题   强        高

```

注：难题，我指的是理论上准确定义的无高效算法的那一类问题。有了准确定义之后，世界上就只有一种难题:-) 特定问题，我想说，它们是被设计出来而且必然有答案的“玩具”题，对很多人也许很难，但本质上一定是“容易”的问题。

以上比较还没涉及另一个关键词：程序。竞赛培训书都会讲一点编程，一般也会分析不少的代码，而算法书大多是用伪代码，而不会讲程序。值得注意，竞赛书会涉及编程，但又绝不能替代程序设计的入门教程。所以，我这里列出了三个关键词：程序、竞赛和算法。恰恰竞赛就在“程序”与“算法”的中间，是利用程序和算法思路去解题，当然，需要高IQ、丰富的想象、高超的技巧和有针对性的强化培训。值得注意并且我想强调的是，**竞赛训练并不能替代编程的训练和算法的学习**。但是，很多老师或者同学，就寄希望于程序竞赛来进行程序和算法的学习，或者寄望其可强化学习或作为高阶训练。

计算学科发展了这么几十年，在基础科目上都有非常专门的训练内容，请大家记住这一点，也许你缺乏这些训练，只是你缺乏，而不是教学内容上缺乏。很不幸，我所在的学校，无论是竞赛、编程还是算法的训练都极度不足，不能作为参照物。这种训练绝不能用竞赛的训练来替代，再次不幸，有些同学或者其他转不过这个弯（或者是没足够的认识）！如何学习编程和算法不是本文所讨论的问题。

总之，我现在的建议是：竞赛本身是非常有意思的活动，它帮助了程序设计的训练和算法的学习，激发了同学们的学习兴趣，也有助于培养学习能力、交流能力、团队精神，值得提倡。但是竞赛不能不能替代编程与算法的学科训练。编程与算法是计算机学科的两大基本学科内容，是必修的重点科目，需要系统的训练与学习。

P.S. 想参加ACM比赛的同学们必须看清现实，好好掂量一下:-)



---


`@bintou`
`2017-08-29 19:42:21`
`字数 221`
`阅读 1942`


如何在Linux下格式化U盘
==============

`经验` `笔记`

---

### 查看设备

```


1. sudo fdisk -l

```
### Umount

在/media目录下查看挂载点，比如是“Fse0383”，则

```


1. sudo umount -l Fse0383

```

通常U盘有多个分区，都必须umount多几次。

### 格式化

命令：

```


1. sudo mkfs -V -t vfat /dev/sdb1

```

其中sdb1是fdisk显示的设备名，具体情况具体使用，有多个分区，就多执行几次，比如：

```


1. sudo mkfs -V -t vfat /dev/sdb5

```

---

2017.08.29



---


`@bintou`
`2017-01-25 20:02:47`
`字数 1768`
`阅读 2157`


《生活与命运》--摘抄
===========

`读书` `笔记`

---

*摘录自《生活与命运》-瓦西里.格罗斯曼著，力冈翻译，广西师范大学出版社。*

* 凡是有生命的东西，都各有各的特性。...... 如果强行消除生命的独立性和各自的特点，生命就会消失。 P. 003 [Begin]
* "哪儿有强权，”他对＊＊说，“哪儿就有灾难，就流血。......我不相信什么好事，我只相信人性的良善。” P. 013
* 时间就是这样：不断地流逝，可依然生存着。P. 037
* 托里亚没有信来...... 托里亚还是没有信来。P. 055-061[柳德米拉的独白.]
* 维佳，我相信我的信能到你手里......活下去，活下去，永远活下去...... P. 068- 080 [维克托妈妈的来信]
* ＊＊望着墙上的斯大林像，举起酒杯说："来吧，同志们，为咱们的父亲干一杯，咱们祝他永远健康！” P.087
* 党的信任！ P.088
* 像大地一样辽阔、一样长久的，是痛苦。P.125
* 所有的人在牺牲了儿子的母亲面前都感到羞愧，而且，不论人类历史多么长久，想对她说明自己无愧，都是徒然的。P.138
* 自由是根本，是目的，是基础的基础。没有自由就没有无产阶级革命。P.183
* 人类渴望自由的天性是消灭不了的，可以压抑，但无法消灭。...... 我们时代的曙光、未来的曙光就在这一结论中。P.206
* 这种没有意义的善良（东郭先生给予蛇的善良）正是人的天性，它就是人与其他一切的区别，它就是人的精神所能达到的最高境界。它说明，生存并不就是恶。这种善良是没有语言、没有用心的，它是本能的。是盲从的。P.414
* 人类的历史不是善极力要战胜恶的搏斗，人类的历史是巨大的恶要碾碎人性的种子的搏斗。但是，如果人性就是现在仍然没有被摧残殆尽的话，那么，恶已经不可能取得胜利了。P.415
* 战争的秘密及其悲剧性，就是一个人有权力叫另一个人去死。这种权力所依靠的基础是：人们为了共同的事业，可以赴汤蹈火。P. 510
* \*\*用石头一样的冰冷口气在强调国家肯定无疑会取得胜利，却不知道国家正依靠人们的困难和向往自由的热衷而被保卫着。P. 527
* 一个生命的灵魂保持其独特性，便是自由。宇宙在人的意识中的反映是人的力量的基础，但是，只有当一个人作为一个在时间的长河中永远无人可以摹仿的世界而存在时，人生才幸福，才是自由，才是最高的目的。P.565
* 没有自由的生活！这是疾病。失去自由就等于失去健康。P.643
* 有一种权力，大于不加思考就叫人去死的权力，那就是在叫人去死的时候深思熟虑的权力。P.659
* 他（斯大林）比世界上任何人都懂得：胜利者是不受审判的。P.670
* 新德国的缔造者和领袖一定要脱离人类。他（希特勒）的思想、感情及日常生活只能在人类之上，在人类之外。P.673
* “限制宇宙无限性的界限是有的，那就是生命。......我觉得，可以给生命下定义为自由。生命就是自由。生命的基本原则就是自由。”P.706
* "请告诉我，如果无所不能、无所不在的人类仍然带有我们今天的刚愎自用和利己主义，包括阶级的、民族的、国家的、个人的利己主义，人类的强大将给世界带来什么？......请告诉我，您是否相信善良、道德、慈悲心的进化？人是不是在这个方面也会进化？” P.708
* 人类要过明智的生活，今天的善良和好心肠是不够的。......日益发展的不只是人的力量，还有仁爱心，还有人的精神。P.708
* "老一代的人一定需要信仰一点儿什么：......爸爸信仰自由......，可是我们新一代认为这些都是愚蠢的。总的说，信仰就是愚蠢。应当过没有信仰的生活" P. 770
* 每一个时代都有自己的世界名城。它是时代的灵魂，时代的意志。P. 815
* 世界名城与众不同，在于它有灵魂。战时的斯大林格勒就有灵魂。它的灵魂是自由。P.818
* 渺小的人和高尚的人都有不足之处。他们的区别在于：渺小的人做了好事就要夸耀一辈子；高尚的人做好事，一点也不注意，而长期记在心里的是他所做的坏事。P.862
* 年复一年，每天，每时每刻都需要斗争，保卫自己做人的权利，保持纯洁与善良的权利。在这种斗争中既不需要骄傲，也不需要虚荣，需要的是搏斗。P.863
* 但是在寒冷的树林中比阳光明丽的平原上春意更浓。在这宁静的树林里的悲伤，也比宁静的秋日里的悲伤更沉重。在这无言的静默中，可以听到哀悼逝者的号哭和迎接新生的狂欢...... P. 894 [End]

2017.01.20晨   

2017.01.25晨



---


`@bintou`
`2018-12-23 03:56:43`
`字数 573`
`阅读 1753`


为什么这个证明是错误的？
============

`线性代数`

---

Trace是线性代数中一个重要概念。A是矩阵，，即矩阵对角线上元素的相加。Trace有一个奇妙的属性就是，其中  是矩阵A的特征值。如何证明？有一个很简洁的证明如下，可惜这个证明不对。大家能看出为什么吗？

其中 就是对A的对角化分解，是对角矩阵，其中元素就是特征值。第二个等号使用了Trace的一个性质：。

蛮酷的，可惜，尽管酷，却是一个错误。

### 另一个证明

如果你们愿意，也许可以验证一下这个证明。

对任意矩阵存在非奇异矩阵使得，其中是Joardan正则型( Jordan canonical form)。应用得到，其中是的特征值。

Jordan型(Jordan form)是上三角矩阵，因此它的特征值在对角线，所以，它的trace等于特征值之和。



---


`@bintou`
`2016-11-16 00:19:04`
`字数 2718`
`阅读 2037`


《九三年》-少量文摘
==========

`阅读` `经典`

---

在我看过的所有历史教材中，只有两类人：伟人与败类，前者推动历史的进程，后者被历史的车轮碾碎并被钉上耻辱柱。所以，我从来就无法理解所谓的法国大革命，无法理解将路易十六送上断头台的罗伯斯比尔为何也被送上断头台，区别是：路易十六性命不保是因为国民议会的判决，而革命家罗伯斯比尔之死却未经审判！

1793，中国尚处于乾隆盛世，估计乾隆在江南某个小村微服出访。那一年，华盛顿成了美国第一任总统，而法国国王却丢了脑袋。法国作家雨果最后一部长篇小说《九三年》展示了这一年中革命大风暴，注意，是以法国人的方式：客观地！（我还希望他少一点评价。）

在《九三年》中，我们看到一场一场狂烈的风暴，看到历史进程中人类的苦难，认识历史进程中的缺乏理性悖论迷局，宗教、王权、革命、理想、民主、自由、欲望在这场风暴中纠结不清，个体在这场风暴中的无力挣扎。这一切都是我所见的中文著作中从来不曾出现的内容，而这本小说在出版在十九世纪后期。

一个革命军人在见到一个衣衫褴褛带着三个小孩的妇女时应该说（教育）什么？

*“你说吧，太太，你有家吗？”   

“有过。”“在哪里？”   

“在阿泽。”   

“你为什么不呆在家里？”   

“家被烧掉了。”   

“谁干的？”   

“不知道。是战争。”   

“你从哪里来？”   

“从那里。”   

“你去哪里？”   

“不知道。”   

“说正题吧，你是谁？”   

“不知道。”   

“你不知道你是谁？”   

“我们是逃难的人。”   

“你是哪一派？”   

“不知道。”“是蓝党还是白党？你和谁站在一起？”*

归根结底，他想问：你的政治观点是什么？政治观点......

我问：丹东、马拉、罗伯斯比尔（Kerberos的三个脑袋！）的政治观点是什么？请看：

*“但是要弄清敌人在哪里。”   

“在外面，我把他们赶出去了。”丹东说。   

“在里面，我在监视他们。”罗伯斯比尔说。   

“那我就再把他们赶走。”丹东说。   

“内部的敌人不能赶走。”“那拿他们怎么办？”   

“消灭他们。”“我同意。”丹东说。他又接着说：“我跟你说、罗伯斯比尔，敌人在外面。”   

“我跟你说，丹东，敌人在内部。”   

“他们在边境上，罗伯斯比尔。”   

“他们在旺代，丹东。”   

“你们平静下来，”第三个声音说，“敌人无所不在，你们完蛋了。”*

太精彩了！以下是Kerberos的法国解释版本：

*罗伯斯比尔专心致志地看地图，马拉突然叫了起来：“现在需要一位独裁者，罗伯斯比尔，你知道我要求有一位独裁者。”   

罗伯斯比尔抬起头：“我知道，马拉，或者是你或者是我。”   

“或者是我或者是你。”马拉说。   

丹东咕哝道：“独裁！居然想到独裁！”   

马拉看见丹东皱起眉头，接着说：“听着。我们作最后的努力，达成一致吧。这是形势的要求。我们不是在五月三十一日行动日这件事上达成过一致吗？吉伦特派只是枝节问题，全局问题更重要。你们有些话是正确的，但是我说的是真话，不折不扣的真话，完完全全的真话。南方有联盟派，西方有保皇派，在巴黎，国民公会和公社你争我夺，在边境，居斯蒂后退，迪穆里埃投敌，这一切意味着什么？分崩离析。我们需要什么？统一。统一是得救之路，但是要快。巴黎必须掌握革命的领导权。如果我们浪费一小时，明天旺代分子就可能到达奥尔良，普鲁士人就可能到达巴黎。后一点我同意你，丹东，前一点我同意你，罗伯斯比尔。总之，结论是专政。建立专政，我们三个人代表革命。我们是Kerberos①的三个脑袋，一个脑袋说话，就是你，罗伯斯比尔，一个脑袋咆哮，就是你，丹东⋯⋯”* 　　   

①希腊神话中看守地狱的巨大，有三个脑袋。   

*“还有一个脑袋咬人，就是你，马拉。”丹东说。   

“三个脑袋都咬人。”罗伯斯比尔说。   

总之，结论是专政。建立专政，我们三个人代表革命！！！   

“罗伯斯比尔，在十二月七日的会上你替罗朗夫人辩护，反对维阿尔。”   

“当雅各宾派攻击作时，是我兄弟为你辩护的，马拉，这能证明什么呢？什么也证明不了。”   

“罗伯斯比尔，我们知道你曾在杜伊勒里宫对加拉说：‘我对革命感到厌烦了。’”   

“马拉，十月二十九日，你就是在这里，在这个小酒店里拥抱了巴尔巴鲁。”   

“罗伯斯比尔，你曾对比佐说：‘共和国，这是什么玩意？’”   

“马拉，你曾在这个小酒店里请三个马赛人一同进餐。”   

“罗伯斯比尔，你让巴黎中央菜场的一位搬运工提着木棍护送你。”   

“而你，马拉，八月十日前夜，你让比佐帮你逃往马赛，冒充骑马师。”   

“在九月份的大批处决期间，你藏了起来，罗伯斯比尔。”   

“而你，马拉，你抛头露面。”   

“罗伯斯比尔，你曾把红色无檐帽扔到地上。”*

是的，这就是该死的三巨头的思想！以下的争吵更加精彩！

*丹东神色可怕地站了起来，叫道：“是的，我是婊子，我出卖肉体，但拯救了世界。”   

罗伯斯比尔又啃起指甲来。他既不会大笑，也不会微笑。丹东的闪电式大笑，马拉的刺戳式微笑，他都不会。   

丹东又说：“我像大海，有涨潮和退潮。退潮时人们看见我的浅底，涨潮时人们看见我的浪涛。”   

“你的泡沫。”马拉说。   

“我的风暴。”丹东说。   

马拉像丹东一样站了起来，大发雷霆。倾刻之间，蛇变成了龙。“呵，”他喊道，“呵！罗伯斯比尔！呵！丹东！你们不肯听我的话！好吧，我告诉你们，你们完蛋了！你们的政策陷入绝境，无法再往前走。你们没有出路了，你们的行为关闭了所有的门，只留下坟墓的门了。”   

“这正是我们的伟大。”丹东说。他又耸耸肩。马拉继续说：“丹东，你要当心。韦尔尼奥也长着大嘴和厚嘴唇，眉毛也是气鼓鼓的，像你和米拉博一样也有麻子，但是这并没有阻止五月三十一日的‘行动日’。呵！你在耸肩，有时耸肩会耸掉脑袋的。丹东，我告诉你，你的粗嗓门，松散的领带和靴子，小夜宵，大口袋，这可关系到路易泽特。”   

路易泽特是马拉对断头台的爱称。   

他又接着说：“至于你，罗伯斯比尔，你是温和派，但这也没有用。你擦脂抹粉，衣服笔挺，头发卷卷的，很是讲究，你洋洋得意，傲慢不驯，但你照样会在格雷夫广场被处死。你可以读读布伦瑞克的声明，你也会受到武君者达米安那样的待遇，你现在穿得整整齐齐，就等将来被五马分尸了。”   

“你是科布伦茨亡命贵族的应声虫！”罗伯斯比尔咬着牙说。   

“罗伯斯比尔，我不是任何人的应声虫。我是万事万物的呼声。你们还年轻。你多大，丹东？三十四岁。你呢，罗伯斯比尔，三十三岁。我呢，我一直活着，我是人类古老的痛苦。我有六千岁。”   

“不错，”丹东反驳说，“六千年以来该隐①就藏在仇恨里，就像癞蛤蟆藏在石头里一样。现在石头裂开，该隐跳到人间来了，这就是马拉。”   

①《圣经》中亚当和夏娃的长子，因忌妒杀害其弟。   

“丹东！”马拉喊道，眼中闪过一丝苍白的光。   

“怎么了？”丹东说。*

这三个巨人就这样交谈着。霹雳般的争吵。

九三年，中国需要的不是革命，我们需要的是思想。现在我们不需要思想，我们只要求能容忍思想的土壤。   

<http://book.douban.com/subject/2042629/>



---


`@bintou`
`2019-08-05 18:11:47`
`字数 2537`
`阅读 1782`


关于一道编程题的思考
==========

`编程`

---

### 一道普通的编程题

以下[这道编程题](https://www.jianshu.com/p/74e6b7c1f730)连续三年出现在本科《计算机安全学》的实践作业当中，每年大概会有100名左右的学生被要求用C或者Python实现相关功能。

> 给定以下8\*8的0/1比特矩阵M，
> 
> ```
> 
> 
> 1. 1 0 0 0 1 1 1 1
> 2. 1 1 0 0 0 1 1 1
> 3. 1 1 1 0 0 0 1 1
> 4. 1 1 1 1 0 0 0 1
> 5. 1 1 1 1 1 0 0 0
> 6. 0 1 1 1 1 1 0 0
> 7. 0 0 1 1 1 1 1 0
> 8. 0 0 0 1 1 1 1 1
> 
> ```
> 
> 请编程实现M\*x（矩阵乘向量），x是8比特的0/1向量。即，输入x，输出M\*x的值。其中所有乘法、加法都是mod 2的乘法、加法。编程语言请使用C或者Python。

今天拿出来讨论主要不是因为这道题的结题思路有什么难或多有价值，也没有什么特殊的技巧需要总结，而是因为，大部分同学的程序没有能够体现出程序员应有的基本素养。他们的想法大多与我不同。

### 题解

题目描述的是一种普通的矩阵运算。这个矩阵出现在著名的分组加密算法AES的设计当中，用于生成AES算法中使用的S-box（一般读者并不需要理解什么是S-box）。为方便论述，本文简化了其中关于GF(2^8)的描述，也砍掉了一个xor某常数的过程。不过，过程大致类似。

大部分同学的做法是这样的：

```


1. //AES给出的常数矩阵
2. const bool N[8][8] = {1, 0, 0, 0, 1, 1, 1, 1,
3. 1, 1, 0, 0, 0, 1, 1, 1,
4. 1, 1, 1, 0, 0, 0, 1, 1,
5. 1, 1, 1, 1, 0, 0, 0, 1,
6. 1, 1, 1, 1, 1, 0, 0, 0,
7. 0, 1, 1, 1, 1, 1, 0, 0,
8. 0, 0, 1, 1, 1, 1, 1, 0,
9. 0, 0, 0, 1, 1, 1, 1, 1};
10. //将输入x转化为数组用作矩阵运算
11. for(int i = 0; i < 8; i ++)
12. { xb[i] = (x&1); x >>= 1; }
14. //矩阵乘法
15. bool tmp[8];
16. for(int i = 0; i < 8; i ++)
17. tmp[i] = 0;
18. for(int i = 0; i < 8; i ++)
19. for(int j = 0; j < 8; j ++)
20. tmp[i] ^= (N[i][j] & xb[j]);
21. //输出结果
22. .......

```

程序员把功能实现出来不就好了吗？你告诉我需要一个矩阵乘法，我做出来了有什么不对？没有不对，这个功能是对的。但是，当我们用一种数学的语言去描述功能的时候，我们只是描述，“翻译”成应用的时候需要另一种“语言”。听上去有点玄，其实这才是程序员应有的素养。以下还是回到题目来解释。

#### 矩阵

题目给出的是一个矩阵，每个元素都是0/1比特，8行8列。难道8比特没让程序员们有什么想法？为什么存储8比特的应该是数组而不是一个unsigned char？比如，这个矩阵难道不应该是：

```


1. unsigned char M[] = {0x1F, 0x3E, 0x7C, 0xF8, 0xF1, 0xE3, 0xC7, 0x8F};

```
#### 矩阵乘向量

矩阵乘向量，无非是矩阵列向量的组合。模2加法在这里只是比特按位异或（xor）。大致应该是以下这样一种运算(注意以下代码不是完全正确的C语言程序)：

```


1. res = 0x00;
2. for(int i = 0; i < 8; i ++)
3. res = res ^ (M[i] * xb[i])

```

向量x是不是应该转换为是一个数组xb？答案否定！我们可以通过位移操作得到相应的比特。并且还必须注意一点，当x中的比特为0，那么对应的列就没必要参与操作了。所以，

```


1. res = 0x00;
2. i = 0;
3. //矩阵列组合，直到x小于0
4. while(x > 0)
5. {
6. if(x % 2 == 1) //取最低位比特，并且忽略比特0的加法
7. res ^= M[i] ;
8. i++; //为什么不在上面的i上进行++ ?
9. x /= 2; //可用比特移位操作。但是你认为这样除效率会比移位要差吗？
10. }

```
### 延伸思考

单纯从题目本身看，并不很重要，重要的是要思考。

#### “会”不等同“素养”

归纳一下我想强调的所谓程序员的素养：   

- 熟悉数字的十六进制表达；   

- 熟悉变量的比特运算；   

- 熟悉矩阵的列组合；   

- xor与模2运算的关系；   

- 知道变量最低比特位如何取；   

- 知道整除2就是变量右移一比特；

这些你单独拿出来考试，请问谁不会？都会！哪请问，为什么到了具体编程的时候大部分人不会？会不等同于素养！素养是什么？是对基础知识的融会贯通，是让专业知识溶入你的血液。

#### 关于语言的应用

也许有人会问了，AES的设计者为什么需要这样的矩阵描述，而不是直接给出后面这种描述？你告诉我矩阵是这8个常量不就好了，为什么要我们去“猜”？

答案是，AES的设计者需要一种数学语言来描述这个过程。请注意，是一种需要。为什么？主要两个原因。首先，因为设计人员想展示这个矩阵具有可逆矩阵，可用于求逆S-Box的元素。如果我告诉你这几个常量，而不是展示一个矩阵，那么矩阵的熟悉就难以表达。而现在则简单，你只需要自己验证M矩阵行列式不为0即可。其次，设计者还想传递一个公开的想法，矩阵构造的规律性。大家可以自己验证矩阵每一行每一列之间的关系。

当这种语言描述的目的达到了，那么我们就需要另一种“语言”来执行相关操作，达到既定目标。其实，在实现中，这个矩阵M并不一定真正存在。给定输入b，输出b'满足以下关系定义，这估计才是设计者的真实想法：

![M矩阵的消失](https://upload-images.jianshu.io/upload_images/52389-f879c01b88d8a0f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我们可以使用什么样的比特操作来得到正确的答案呢？答案并不重要，也不是本文想论述的内容。大致如下，但不再分析：

```


1. //ROTL8是8比特变量的循环左移
2. xformed = x ^ ROTL8(x, 1) ^ ROTL8(x, 2) ^ ROTL8(x, 3) ^ ROTL8(x, 4)

```

啥？一条命令完成？？？看到这里，你们会不会觉得我是抛出一个假问题，然后给出了一个假答案？思考才是这个帖子的本意。

多说一句，至此故事并没有结束。AES的构造描述在很多年之后依然有新的研究进展。 文章[“Essential Algebraic Structure Within the AES”](http://en.thehackademy.net/madchat/crypto/papers/aes-crypto.pdf) （by Murphy and Robshaw）关注的不是实现，而是AES的构造与分析，详情不在本文展开，有兴趣可以参考[这里](https://crypto.stackexchange.com/questions/18199/polynomial-representation-of-the-affine-part-of-the-aes-s-box/18215#18215)。

### 总结

数学语言可以有助于我们清楚地表达许多思想，能充分理解数学语言应该是程序员的应有素养。程序设计语言是一种表达思想的工具，它不是单纯用于重述或重现现实的语言，它应该是对数学语言系统化的工具，很好地描述数学，又能体现系统属性，诸如高效性、兼容性等。

如果要简单地看待这篇文章，你只需要记住：编程并不是用程序语言依葫芦画瓢。[SICP](https://www.jianshu.com/p/213888357b65)对此已经做了非常深入的探讨，建议大家阅读。



---


`@bintou`
`2016-01-22 01:59:36`
`字数 4126`
`阅读 2422`


SCOOPING THE LOOP SNOOPER
=========================

`計算理論` `詩歌`

---

**SCOOPING THE LOOP SNOOPER**

*A proof that the Halting Problem is undecidable   

Geoffrey K. Pullum   

(School of Philosophy, Psychology and Language Sciences, University of Edinburgh)*

No general procedure for bug checks will do.   

Now, I won't just assert that, I'll prove it to you.   

I will prove that although you might work till you drop,   

you cannot tell if computation will stop.

For imagine we have a procedure called **P**   

that for specified input permits you to see   

whether specified source code, with all of its faults,   

defines a routine that eventually halts.

You feed in your program, with suitable data,   

and **P** gets to work, and a little while later   

(in finite compute time) correctly infers   

whether infinite looping behavior occurs.

If there will be no looping, then **P** prints out 'Good.'   

That means work on this input will halt, as it should.   

But if it detects an unstoppable loop,   

then **P** reports 'Bad!' — which means you're in the soup.

Well, the truth is that P cannot possibly be,   

because if you wrote it and gave it to me,   

I could use it to set up a logical bind   

that would shatter your reason and scramble your mind.

Here's the trick that I'll use — and it's simple to do.   

I'll define a procedure, which I will call **Q**,   

that will use **P**'s predictions of halting success   

to stir up a terrible logical mess.

For a specified program, say **A**, one supplies,   

the first step of this program called **Q** I devise   

is to find out from P what’s the right thing to say   

of the looping behavior of **A** run on **A**.

If **P**'s answer is ‘Bad!’, **Q** will suddenly stop.   

But otherwise, **Q** will go back to the top,   

and start off again, looping endlessly back,   

till the universe dies and turns frozen and black.

And this program called **Q** wouldn't stay on the shelf;   

I would ask it to forecast its run on itself.   

When it reads its own source code, just what will it do?   

What’s the looping behavior of **Q** run on **Q**?

If **P** warns of infinite loops, **Q** will quit;   

yet **P** is supposed to speak truly of it!   

And if **Q**'s going to quit, then **P** should say ‘Good.’   

Which makes **Q** start to loop! (**P** denied that it would.)

No matter how P might perform, **Q** will scoop it:   

**Q** uses P's output to make **P** look stupid.   

Whatever **P** says, it cannot predict **Q**:   

**P** is right when it’s wrong, and is false when it's true!

I've created a paradox, neat as can be —   

and simply by using your putative **P**.   

When you posited **P** you stepped into a snare;   

Your assumption has led you right into my lair.

So where can this argument possibly go?   

I don't have to tell you; I'm sure you must know.   

A reductio: There cannot possibly be   

a procedure that acts like the mythical **P**.

You can never find general mechanical means   

for predicting the acts of computing machines;   

it's something that cannot be done. So we users   

must find our own bugs. Our computers are losers!

---

In October 2000, after a refereeing delay of nearly a year, an earlier and incorrect version of this poetic proof was published in Mathematics Magazine (73, no. 4, 319–320). But it had an error. I am very grateful to Philip Wadler (Informatics, University of Edinburgh) and Larry Moss (Mathematics, Indiana University) for helping with the development of this corrected version, which is now free of bugs (trust me; you can check it). Thanks also to the late Dr. Seuss for the style, and of course to the pioneering work of Alan Turing (and Martin Davis’s nice simplified presentation) for the content. I had the privilege of reading this aloud at a conference in honour of the memory of Alan Turing at Cambridge University in June 2012. Notice that reading it aloud works best in southern British standard English: the rhyme of the first two lines of the third stanza call for a non-rhotic dialect. Copyright © 2008 by Geoffrey K. Pullum. Permission is hereby granted to reproduce or distribute this work for non-commercial, educational purposes relating to the teaching of computer science, mathematics, or logic, provided this attribution is included. The same holds for the Ukrainian version which you can see if you click here, and the Czech version for which you can click here, and the Polish version for which you can click here. (There was a Belorussian version too, atthis site, but the link seems to be dead.) Poetic restatement of classic computability theory results seems to be huge in the Slavic world for some reason.

原文出自：<http://www.lel.ed.ac.uk/~gpullum/loopsnoop.html>

---

解读一下，帮助理解：

1. 算法P，它的输入是任意程序A及其输入In，P在有限的时间内会停止运行并得出判断：如果程序A在输入In下不死循环则输出Good，否则输出Bad。现在需要证明这种算法不存在。   
   
   简单记为：P(A, In) --> Good/Bad .
2. 假设P存在，构造Q，输入任意程序A，调用P去判断A在输入为A下是否死循环。如果A死循环，则Q结束运行；否则，Q自己进入死循环。   
   
   简单记为：Q(A) : If P(A, A) -->Bad, Stop; else Loop.
3. 现在运行Q，输入是自己本身，即Q，请问答案是什么？ 如果Q死循环，则Q结束运行；如果Q不死循环，则Q进入死循环；矛盾！   
   
   即：Q(Q): If P(Q, Q) -->Bad, Stop; else Loop. 翻译成悖论就是：如果P判断Q在输入为Q不停机的话，则Q立即停机；如果P判断Q在输入为Q停机的话，则Q进入死循环。

这首诗歌的主要意义在于，它确实是一首诗。注意，图灵机的形式化定义是确保在第一步的假设下，之后的所有构造都是合法构造，这一点其实是难点，需要认真体会。这就不是一首诗可以帮忙解决的问题了。《圖靈的祕密》整本書都在講解這個構造，很顯然，嚴格的論證還需要更多的技術細節。推薦大家看看這本書，可浮一白。



---


`@bintou`
`2017-12-19 06:54:41`
`字数 15178`
`阅读 2133`


《新年问候》--[俄]茨维塔耶娃
================

`诗歌`

---

> 《新年问候》，[俄]茨维塔耶娃。不能说这是一个好的版本，但一定是一个独特的版本，一个让人接近于能懂的版本。它是黄灿然、王家新版本和两个英文版本的大杂烩。献给喜欢诗歌的朋友们，新年快乐！让我凭借这首诗歌 “越过这张桌子的无垠海岛，我的杯将碰到你的杯，以无声的一碰。” 新年快乐！

---

### 新年问候

**I.**

新年快乐 ----- 新世界/光 ----- 边缘/王国 ----- 避难所！   

第一封信给你，寄往你那   

----- 误为苍翠的、绿色的 -----   

喧嚣、空旷的新居，   

犹如风神之塔。   

第一封信给你，来自昨日-----   

那里，没有了你 -----   

来自我的家乡，   

家乡-----现在已经是来自众星中的   

一颗......

*译者注，“世界/光”、“边缘/王国”表示一个词，同时具有两种含义.*

想要我告诉你   

我怎么知道的吗？   

没有地震或雪崩的宣示，   

只是某人-----可以是任何人-----说   

他在报纸上读到了它。‘把文章给我-----   

哪里发生的？’‘在山里。   

（我想到探入窗户的松树枝）   

难道你不看报吗？’   

‘报纸呢？’‘我没带。’   

‘哪里发生的？’‘疗养院。’   

（租借来的天堂）‘请告诉我何时发生。’   

‘昨天，或者前天，我记不得。   

你不打算为我们写点什么？’‘不，不写。   

他是家人，我不是犹大。’

**II.**

那么 ----- 即将到来的新年快乐！（明日诞生的新年！） -----   

要我告诉你我做了什么吗，当我得知...... ？   

哦不！......说溜嘴了。坏习惯。   

我不想使用生或死这样愚蠢的字眼。   

我什么也没有做，但确实发生了   

什么，发生得没有   

影子或回声！

那么 ----- 这趟旅行怎样？   

那颗撕裂但未撕碎的心   

怎样？如同乘坐奥尔洛夫快步马，   

你说，疾如飞鹰，   

是不是很惊险 -----或不止？   

还要惬意些？   

那里没有高处，或下降，   

对那骑着真正俄罗斯飞鹰的人来说   

我们与来世有血缘关系：   

在俄罗斯待过的人都在此世   

见过来世。   

我谈起生死带着一丝隐忍的傻笑   

-----你将以你自己去触摸它！   

我谈起生死，带着一个注脚，   

一个星号   

（星球，今夜我的渴望，   

去他的大脑的半球 -----   

我渴望天国！）。

*译者注：星号、星球、天国是不同字眼的同一种指代.*

**III.**

现在，我的朋友，   

不应该忘记：如果   

连着写的字母是俄语而不是德语-----   

那不是因为，如今他们宣称   

什么都会发生，   

不是因为乞丐不能成为选择者，   

不是因为死人的可怜，   

他可以吞噬一切-----   

不眨一眼！不，   

而是因为那个世界-----   

我们的世界-----并非没有语言。   

十三岁时，在新圣母修道院   

我就明白：那是前巴别塔时代的天国，   

全部语言都是一种语言。

无限悲哀。你将不再问我   

俄语里怎么说“巢”。   

独有的巢，整个的巢，唯有这个巢   

用天国（星球）庇护一个俄语的韵脚。

我是不是分心了？但不可能发生   

这样的事情-----对你分心。   

每个意念，每个，Du Lieber，   

音节都引向你-----不管说的   

是什么（虽然对我来说德语比俄语   

还母语，但我想要天使们的母语！）   

你已不在，那里什么都没有，   

没有巢，只有坟墓。   

一切都已改变，然而任何都不曾改变。   

-----你是否已经忘......不，不是我----- ？   

新的世界，赖纳，你感觉怎样？   

最坚定的，最全面的，最有把握的-----   

诗人的、对新世界的第一印象，是否符合   

对那个只给予你一次的星球的最后一瞥？

*译者注：“Du Lieber”，德语，意思是心爱的。*

诗人离弃其灰烬，灵魂离开肉体   

（把这两者分开就是犯罪），   

而你离弃自身，你离开你自己。   

成为宙斯之子并不会更好，   

撕裂自己：就像分开卡斯托尔和波吕丢刻斯，   

撕裂自己：就像大理石被掘出大地，   

既不分离也不相遇，   

只是一次遭遇：   

最初的相会和第一次别离。

*译者注：卡斯托尔和波吕丢刻斯是宙斯的双生子.*

你如何能看清你自己的手，   

看清手上的墨渍痕迹，   

从你那如此遥远（多遥远？）的，   

没有尽头因为没有开始的   

栖息处，在地中海的水晶之上   

-----和其他的浅碟。

一切都已改变，然而任何都不会改变。   

我肯定，在这郊外的我，   

一切都已改变，然而任何都不在改变-----   

尽管我还不知道如何把这封额外信件   

寄给我的收信人-----   

我可以往哪里张望呢，   

当我们把手肘斜倚在包厢的边缘，   

如果不是从今生望向来世，   

如果不是从来世望向今生，   

苦难的今生，长长的苦难。

**IV.**

我生活在贝尔维，一个鸟巢和枝丫的小镇。   

与一个导游交换眼神之后：   

贝尔-维。一座堡垒，其窗口可眺望   

巴黎的完美景观，   

巴黎----- 高卢人幻想的会客室，   

以及稍远处......   

手肘搁在猩红色天鹅绒上俯瞰，   

你将会怎样发笑（我也   

一定会），从你高不可测的住处，   

看着我们的贝尔维们和贝尔韦代雷们。

我百无聊赖。失落。所有细节。忙碌。   

新年正在敲门！   

我该跟谁碰杯，   

为了什么？何种理由？   

吞下这一团团棉花   

充当香槟的泡沫。有什么目的？是的，乐钟。但这   

与我何干.......？

在今夜的喜庆中我该拿   

赖纳之死这内在节奏怎么办？   

也即，如果你，这样一只眼睛，模糊了，   

生便不是生，死便不是死。意义   

消失。要是我们相见，我会抓住它。   

非生非死，而是一个第三者，某个方面，   

它是新的（而在把麦秆铺平之后，   

那多好玩啊，对那个二七年，   

正在来的，和对那正在离去的二六   

年 ----- 以你开始并将以你   

结束），我要为它干杯。   

越过这张桌子的无垠海岛   

我的杯将碰到你的杯，以无声的   

一碰。

越过桌面我看着你的十字架。   

有多少场所 ----- 在城外，有多少空间   

在城外！而还会是对谁呢如果不是对我们 -----   

灌木丛招手示意？场所 ----- 特别是我们的   

而不是任何其他人的！所有的叶子！所有的针！   

有我在的你的场所（有你在的你的场所）。   

（我们大可以约会 -----   

就为了聊聊天。）不在乎地点！想想那多少个月吧！   

多少个星期！多少个无人的   

多雨郊区！多少个早晨！以及仍未   

被夜莺开始的所有一切！

很可能我看得不清楚，因为我深陷洞中，   

很可能你看得更清楚，因为你高高在上。   

我们之间什么也没有真正发生。   

无，如此彻底、纯粹的无，   

无，确实发生过的无。   

如此恰当 -----无需赘述。   

什么也没有 ----- 别期望从日常中会产生   

什么东西（那些因此误入歧途的人   

全错了！）而那又是些别的什么   

界线，你是如何落进去的？   

古老的戒律：   

虽然那里是虚无-----纵使是虚无......   

哦，让它成为某种事物，从远处，甚至   

从影子的阴影处！虚无：那些时刻，日子，   

房屋。甚至一个死囚，戴上锁链，   

也拥有记忆的馈赠：嘴唇！

赖纳，我们是否过于挑剔？   

毕竟，还剩下属于我们的   

光与世界。   

我们只是我们自己的反射。   

除此 ----光与世界----- 还有我们的   

姓名。

**V.**

空旷的郊外快乐，   

新地方快乐，赖纳，   

新世界、新光亮快乐，赖纳！   

使证明成为可能的最远端的海岬快乐，   

新眼睛快乐，赖纳，新耳朵快乐，赖纳！

一切对你而言都是   

障碍：激情和朋友。   

新声音快乐，回声！   

新回声快乐，声音！

多少次在教室的书桌上：   

那些是什么山？那些是什么河？   

它们可爱吗，那些没有游客的风景？   

我说得对吗，赖纳 -----乐园是多山的，   

多风暴的？不是寡妇们所热望的那种 -----   

乐园不止一个，对吗？它上面一定还有另一个   

乐园吗？在阶梯形地势上？我是根据塔特拉山脉判断 -----   

乐园只能是   

一个圆形露天剧场。（帷幔正在落下...... ）   

我对吗，赖纳，上帝是一棵生长的   

候面包树？不是一块金路易 -----   

上帝不止一个，对吗？在他上面一定还有一个   

上帝？

在新地方写作还好吗？   

如果你在，那么诗歌就在：   

因为你本身就是诗歌！   

在那甜美生活中写作还好吗，   

没有一张书桌搁你的肘，或额头搁你的手   

我是说，你的手掌。   

给我写信，想念你的笔迹。   

赖纳，你对新韵脚满意吗？   

我对“韵脚”的理解恰当吗？   

是否有一整排新的韵脚-----   

对死亡的崭新韵脚？

再见，下次再见！   

我们将见面-----我不知道------我们将一起歌唱。   

我不理解的新世界快乐，   

整个大海快乐，赖纳，全然的我，快乐！

祈祷我们不要再错过对方-----   

提早给我写信，   

新的声音轨迹快乐，赖纳！

那里有一架通往天国之梯-----   

铺满新年礼物，   

新的任命快乐，赖纳！

我将举起新年的酒杯，   

-----绝不泼洒任何一滴-----   

举到罗讷河之上，举到拉龙之上，   

那最终的离别之地。   

交给赖纳 ----- 马里亚----- 里尔克 ----- 交到他手里。

*拉龙，里尔克的安葬地。*

---

### New Year’s Greetings

by Tatiana Retivov
------------------

i.m. Rainer Maria Rilke

---

Happy New Year – new sphere – horizon – haven!   

This is my first letter to your new address,   

– notorious region, misunderstood, unsettled –,   

as clamorous and empty as the Aeolian tower;   

my very first letter to you from the yesterday   

in which I suddenly found myself without you,   

my own homeland become one of the stars…   

Shall I tell you how I heard the news?   

No earthquake or avalanche announced it,   

only someone – might have been anyone – said   

he’d read it in a daily paper. ‘Show me the article –   

where did it happen?’ ‘The mountains.   

(I think of pine branches in a window)   

Don’t you ever read newspapers?’   

‘The article?’ ‘I don’t have it with me.’   

‘Where did it happen?’ ‘In a sanatorium.’   

(A rented paradise.) ‘Please tell me when.’   

‘Yesterday, or the day before, I can’t remember.   

Will you write something for us?’ ‘No, I won’t.   

He’s family. I’m not treacherous.’   

Happy New Year, then, which begins tomorrow!   

Shall I tell you what I did when I heard   

of your – no, that’s a slip of the tongue.   

I don’t use silly words like Life and Death –   

So tell me, Rainer, how was your ride?   

How was it when your heart burst open?   

Was it like riding Orlov’s horses – wild   

and fast as eagles fly – as you once told me?   

Did it take your breath away? Was it more intense –   

sweeter? Russian eagles have a blood tie   

with the other world, and in Russia   

you see the other world in this.   

It belongs to us, that long night of stars   

I speak of with a secret smile…   

You timed your crossing well.   

Dear friend,   

if Russian script replaces German letters here   

it’s not because the dead have to put up with   

everything, as a beggar does, – it’s because   

the world you live in now is ours.   

– I knew as much when I was thirteen…   

Am I digressing? No, that isn’t possible.   

Nothing can distract my thoughts from you.   

Every one of them, du Lieber, every syllable   

leads me towards you in whatever language.   

German is as native to me as Russian,   

and most of all the language Angels speak.   

There is no place where you are not.   

Except the grave…   

Do you ever – think about me, I wonder?   

What do you feel now, what is it like up there?   

How was your first sight of the Universe,   

a last vision of the whole planet –   

which must include this poet remaining in it,   

not yet ashes, still a spirit in a body –   

seen from however many miles stretch   

from Creation to eternity, far above   

the Mediterranean in its crystal saucer –   

where else would you look, leaning out   

with your elbows on the edge of your box seat   

if not on this poet, with her many griefs…   

I live in Bellevue: these suburban outskirts,   

have birds’ nests in the branches. Glance   

at your tour guide: Bellevue is a fortress   

with a good view of Paris and its palaces.   

How absurd we must seem as you lean out   

on the crimson velvet edge of your theatre box,   

looking down from an infinite height   

on our Bellevue and Belvederes!   

Skip the details. Here’s an urgent fact.   

The New Year is already on my door step.   

With whom can I clink a glass across   

the table tonight? And with what?   

Cotton wool? I have no champagne froth.   

The New Year is striking. Why am I here?   

What is there to do in this New Year?   

If such an orb of light as you can go out   

then neither life nor death has any meaning.   

I shall only understand when we meet again.   

What joy to end with you, begin with you.   

Let us clink across the table, not with pub   

glasses, but as if our souls fused.   

I look upon your cross. Everywhere   

outside time and place belongs to us.   

Leaves and conifers. Months and weeks   

in rainy city fringes without people!   

And mornings – all of them spent together.   

Of course I see poorly down here in a pit   

Of course you see better from up there.   

Nothing turned out between us. That is the truth:   

Nothing happened. Nothing.   

We know our roles, and both are large enough   

not to mention that. Don’t wait   

for the one who stands out from the crowd   

– or the one who stands inside it either.   

An eternal tune:   

don’t speak of the one on death row   

cut from the same cloth and remembered   

by the same mouth. Only one world   

was ours, and that was where we shone;   

exchanging everything else to do so.   

So, from these outskirts: Happy new world,   

Rainer! Happy new sounds!   

Everything once seemed to stand in your way,   

even passion and friendship. No longer.   

Happy new echoes, Rainer!   

I used to dream at my school desk about rivers   

and mountains. How is your landscape without tourists?   

Was I right, Rainer, to think of heaven as stormy   

and mountainous – not the way widows imagine?   

And not just one heaven, but another over it?   

With terraces? Something like the Tatra?   

Heaven must resemble an amphitheatre.   

Was I right to think of God as a Baobab?   

Is there only one God – or another over Him?   

I know wherever you are, there are poems.   

How do you write without a table for your elbow,   

or even a forehead for your cupped hand?   

Drop me a line in your usual scrawl!   

Death must offer many occasions for poetry.   

Are you pleased, Rainer, with your new verse?   

I can’t go any further, now I’ve learned   

a language with so many new meanings.   

Goodbye. Until we meet each other   

– if we do – face to face. Look   

at the whole earth and the oceans, Rainer.   

Look at all of me.   

If you can, drop me a scribbled line   

– Happy new writing, Rainer – and   

I’ll climb a staircase bearing gifts to you   

hoping to feel your hand on my head,   

I’ll carry my New Year’s glass, without spilling   

a tear-drop, over the Rhone and Rarogne   

– your resting place – which marks our final parting.   

Put this into the hands of Rainer – Maria – Rilke!

---

### New Year’s Greetings

by [Caroline Lemak Brickman](http://hypocritereader.com/contributor/caroline-brickman/)

happy new year—happy new light, new world—happy new edge, new realm—happy new haven!   

a first letter to you in the next—   

the place where nothing ever happens   

(barely even bluffing ever happens), place where roughing,   

rushing ever happens, like Aeolus’s empty tower.   

a first letter to you from yesterday’s   

homeland, now noland without you,   

now already one of the   

stars... and this law of leaving and left, cleaving   

and cleft,   

this claw by which my beloved becomes a name on a list   

(oh him? from ’26?),   

and the has-beens transform to the unhappened.

shall I tell you how I found out?   

not an earthquake, not an avalanche.   

a guy came over—just anyone (you’re my one):   

“really, a regrettable loss. it’s in the Times today.   

will you write an article for him?” where?   

“in the mountains.” (the window opening onto fir branches.   

the bedsheet.) “don’t you read the papers?   

and won’t you write the obit?” no. “but—” spare me.   

aloud: too hard. silently: I won’t betray my Christ.   

“in a sanatorium.” (heaven for hire.)   

what day? “yesterday, day before yesterday, I don’t remember.   

you going to the Alcazar later?” no.   

aloud: family stuff. silently: anything but Judas.

II.   

here’s to the coming year! (you were born tomorrow!)   

shall I tell you what I did when I found out about—   

oops... no, no, I misspoke. bad habit.   

I’ve been putting quotation marks around life and death for a while now,   

like the empty stories we weave. wittingly.

well, I didn’t do anything. but something did   

happen, happened shadowless and echoless,   

happened.   

now, how was the trip?   

how did it tear, did you bear, did it burst   

your heart asunder? astride the finest Orlov racehorses   

(they keep up, you said, with the eagles)   

was your very breath taken, or worse?   

was it sweet? no heights, no falls for you,   

you flew on real Russian eagles,   

you. we have blood ties with that world and with the light:   

it happened here, in Rus, the world and light   

matured on us. the rush is up and running.   

I say life and death with a smirk,   

hidden, so you’ll kiss me to find out.   

I say life and death with a footnote,   

an asterisk (a star, the night I long for,   

fuck the cerebral hemisphere,   

I want the stars).

III.   

now don’t forget, my dear, my friend,   

if I use Russian letters   

instead of German ones, it’s not because   

they say that these days anything will do,   

not because beggars can’t be choosers,   

not because a dead man is a poor one,   

he’ll eat anything, he won’t even blink.   

no, it’s because that world, that light—   

can I call it “ours”?—it isn’t languageless.   

when I was thirteen, in the Novodevichy monastery,   

I understood: it’s pre-Babelian.   

all the tongues in one.

anguish. you will never ask me again   

how to say “nest” in Russian.   

the sole nest, whole nest, nothing but the nest—   

sheltering a Russian rhyme with the stars.

do I seem distracted? no, impossible,   

no such thing as distraction from you.   

every thought—every, Du Lieber,   

syllable—leads to you, no matter what,   

(oh to hell with the native Russian tongue, with German,   

I want the tongue of an angel) there is no place,   

no nest, without you, oh wait there is, just one. your grave.   

everything’s changed, nothing’s changed.   

you won’t forg—I mean, not about me—?   

what’s it like there, Rainer, how are you feeling?   

insistent, surefire, cocksure,   

how does a poet’s first sighting of the Universe   

square with his last glance at this planet,   

this planet you got only once?

the poet gone from his ashes, spirit left the body   

(to split the two would be to sin),   

and you gone from yourself, you gone from you,   

no better to be Zeus-born,   

Castor ripped—you from yourself—from Pollux,   

marble rent—you from yourself—from the earth,   

no separation and no meeting, just   

a confrontation, the meeting and the separation   

first.

how could you see your own hand well enough to write,   

to look at the trace—on your hand—of ink,   

from your perch on high, miles away (how many miles?),   

your perch of endless, because startless, heights,   

well above the crystal of the Mediterranean   

and other saucers.   

everything’s changed, nothing will change   

as far as I’m concerned, here on the outskirts.   

everything’s changed, nothing is changing—   

though I don’t know how to send this extra week’s letter   

to my correspondant—and where do I look now,   

leaning on the rim of a lie—if not from this to that,   

if not from that to this. suffering this. long suffering this.

IV.   

I live in Bellevue. a little city   

of nests and branches. exchanging glances with the guide:   

Bellevue. the fortress with the perfect view   

of Paris—the chamber with the Gallic chimera—   

of Paris—and further still...   

leaning on the scarlet rim,   

how funny they should be to you (to whom?),   

(to me!) they must be funny, funny, from fathomless heights,   

these Bellevues and these Belvederes of ours!

I’m listless. losing it. the particulars. urgency.   

the new year’s knocking at the door. what can I drink to?   

and with whom? and what indeed to drink? instead of champagne bubbles   

I’ll take these wads of cotton into my mouth. there, the stroke—God,   

what am I doing here? what auspices—what am I supposed to do,   

this new year’s noise—your death echoes, Rainer, it echoes and it rhymes.   

if such an eye as you has shut,   

then this life isn’t life, and death’s not death,   

it’s dimming, slipping away, I’ll catch it when we meet.   

no life, no death, okay so some third thing,   

a new one. I’ll drink to that (spreading straw,   

strewing flowers for the 1927th thing,   

bye 1926, what a joy, Rainer, ending   

and beginning with you!), I’ll lean across   

this table to you, this table so big no end in sight,   

I’ll clink your glass with mine, a little clink,   

my glass on yours. not tavern style!   

me on you, flowing together, us giving the rhyme,   

the third rhyme.

I’m looking across the table at your cross:   

how many places on the margins, how much space   

on the edge! and for whom would the shrubbery sway,   

if not for us? so many places—our places,   

and no one else’s! so much foliage! all yours!   

your places with me (your places with you).   

(what would I do with you at a rally?   

we could talk?) so much space—and I want time,   

months, weeks—rainy suburbs   

without people! I want mornings with you, Rainer,   

I want to begin the mornings with you,   

so the nightingales don’t get there first.

it’s probably hard for me to see because I’m down in a hole.   

it’s probably easier for you because you’re up on high.   

you know, nothing ever really happened between us.   

a nothing so purely and simply nothing,   

this nothing that happened, so apt—   

look, I won’t go into detail.   

nothing except—wait for the beat,   

this could be big (first one to miss   

the beat loses the game)—here it comes,   

the beat, which coming beat   

could have been you?   

the beat doesn’t stop. refrain, refrain.   

nothing except that something   

somehow became nothingness—a shadow of something   

became its shade. nothing, that is to say, that hour,   

that day, that home—and that mouth, oh, granted   

courtesy of memory to the condemned.

Rainer, did we scrutinize too hard?   

after all, what’s left: that light, that world   

belonged to us. we’re a reflection of ourselves.   

instead of all of this—that whole light world. our names.

V.   

happy vacant suburb,   

happy new place, Rainer, happy new world, new light, Rainer!   

happy distant point where proof is possible,   

happy new vision, Rainer, new hearing, Rainer.

everything got in your   

way. passion, a friend.   

happy new sound, Echo!   

happy new echo, Sound!

how many times at my schoolgirl’s desk:   

what’s beyond those mountains? which rivers?   

is the scenery nice without tourists?   

am I right, Rainer, rain, mountains,   

thunder? it’s not a widow’s pretension—   

there can’t be just one heaven, there’s bound to be   

another one, rainier, above it? with terraces? I’m judging by the Tatras,   

heaven has to look like an amphitheater. (and they’re lowering the curtain.)   

am I right, Rainer, God’s a growing   

baobab tree? not a Louis d’or?   

there can’t just be one God? there’s bound to be   

another one, rainier, above him?

how’s writing in the new place?   

if you’re there, there must be poetry. you   

are poetry. how’s writing in the good life,   

no table for your elbows, no forehead for your strife,   

I mean your palm?   

drop me a line, I miss your handwriting.   

Rainer, do you delight in the new rhymes?   

am I getting the word rhyme right,   

is there a whole row of new rhymes,   

is there a new rhyme for death?   

and another one, Rainer, above it?   

nowhere to go. language is all learned up.   

a whole row of meanings and consonances   

anew.

goodbye! see you next time!   

we’ll see each other—I don’t know—we’ll sing together.   

happy land I don’t understand—   

happy whole sea, Rainer, happy whole me!   

let’s not miss each other next time! just write me beforehand.   

happy new soundsketch, Rainer!

there’s a staircase in the sky, lined with Gifts.   

happy new ordination, Rainer!

I’ve got them in my palm so they won’t overflow.   

over the Rhone and over Raron,   

over the clear sheer separation,

to Rainer, Maria, Rilke, right into his hands.
----------------------------------------------

*From [new year: a translation](http://hypocritereader.com/26/new-year)*

![新年问候](http://upload-images.jianshu.io/upload_images/52389-dcf61fff6cc512e7.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![小于一](http://upload-images.jianshu.io/upload_images/52389-c840d31c47e4d91e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2017年9月开始整理   

2017年12月18日发布



---


`@bintou`
`2017-11-19 05:54:53`
`字数 11900`
`阅读 1901`


New Year’s Greetings
====================

`诗歌`

---

### New Year’s Greetings

by Tatiana Retivov

---

i.m. Rainer Maria Rilke

---

Happy New Year – new sphere – horizon – haven!   

This is my first letter to your new address,   

– notorious region, misunderstood, unsettled –,   

as clamorous and empty as the Aeolian tower;   

my very first letter to you from the yesterday   

in which I suddenly found myself without you,   

my own homeland become one of the stars…   

Shall I tell you how I heard the news?   

No earthquake or avalanche announced it,   

only someone – might have been anyone – said   

he’d read it in a daily paper. ‘Show me the article –   

where did it happen?’ ‘The mountains.   

(I think of pine branches in a window)   

Don’t you ever read newspapers?’   

‘The article?’ ‘I don’t have it with me.’   

‘Where did it happen?’ ‘In a sanatorium.’   

(A rented paradise.) ‘Please tell me when.’   

‘Yesterday, or the day before, I can’t remember.   

Will you write something for us?’ ‘No, I won’t.   

He’s family. I’m not treacherous.’   

Happy New Year, then, which begins tomorrow!   

Shall I tell you what I did when I heard   

of your – no, that’s a slip of the tongue.   

I don’t use silly words like Life and Death –   

So tell me, Rainer, how was your ride?   

How was it when your heart burst open?   

Was it like riding Orlov’s horses – wild   

and fast as eagles fly – as you once told me?   

Did it take your breath away? Was it more intense –   

sweeter? Russian eagles have a blood tie   

with the other world, and in Russia   

you see the other world in this.   

It belongs to us, that long night of stars   

I speak of with a secret smile…   

You timed your crossing well.   

Dear friend,   

if Russian script replaces German letters here   

it’s not because the dead have to put up with   

everything, as a beggar does, – it’s because   

the world you live in now is ours.   

– I knew as much when I was thirteen…   

Am I digressing? No, that isn’t possible.   

Nothing can distract my thoughts from you.   

Every one of them, du Lieber, every syllable   

leads me towards you in whatever language.   

German is as native to me as Russian,   

and most of all the language Angels speak.   

There is no place where you are not.   

Except the grave…   

Do you ever – think about me, I wonder?   

What do you feel now, what is it like up there?   

How was your first sight of the Universe,   

a last vision of the whole planet –   

which must include this poet remaining in it,   

not yet ashes, still a spirit in a body –   

seen from however many miles stretch   

from Creation to eternity, far above   

the Mediterranean in its crystal saucer –   

where else would you look, leaning out   

with your elbows on the edge of your box seat   

if not on this poet, with her many griefs…   

I live in Bellevue: these suburban outskirts,   

have birds’ nests in the branches. Glance   

at your tour guide: Bellevue is a fortress   

with a good view of Paris and its palaces.   

How absurd we must seem as you lean out   

on the crimson velvet edge of your theatre box,   

looking down from an infinite height   

on our Bellevue and Belvederes!   

Skip the details. Here’s an urgent fact.   

The New Year is already on my door step.   

With whom can I clink a glass across   

the table tonight? And with what?   

Cotton wool? I have no champagne froth.   

The New Year is striking. Why am I here?   

What is there to do in this New Year?   

If such an orb of light as you can go out   

then neither life nor death has any meaning.   

I shall only understand when we meet again.   

What joy to end with you, begin with you.   

Let us clink across the table, not with pub   

glasses, but as if our souls fused.   

I look upon your cross. Everywhere   

outside time and place belongs to us.   

Leaves and conifers. Months and weeks   

in rainy city fringes without people!   

And mornings – all of them spent together.   

Of course I see poorly down here in a pit   

Of course you see better from up there.   

Nothing turned out between us. That is the truth:   

Nothing happened. Nothing.   

We know our roles, and both are large enough   

not to mention that. Don’t wait   

for the one who stands out from the crowd   

– or the one who stands inside it either.   

An eternal tune:   

don’t speak of the one on death row   

cut from the same cloth and remembered   

by the same mouth. Only one world   

was ours, and that was where we shone;   

exchanging everything else to do so.   

So, from these outskirts: Happy new world,   

Rainer! Happy new sounds!   

Everything once seemed to stand in your way,   

even passion and friendship. No longer.   

Happy new echoes, Rainer!   

I used to dream at my school desk about rivers   

and mountains. How is your landscape without tourists?   

Was I right, Rainer, to think of heaven as stormy   

and mountainous – not the way widows imagine?   

And not just one heaven, but another over it?   

With terraces? Something like the Tatra?   

Heaven must resemble an amphitheatre.   

Was I right to think of God as a Baobab?   

Is there only one God – or another over Him?   

I know wherever you are, there are poems.   

How do you write without a table for your elbow,   

or even a forehead for your cupped hand?   

Drop me a line in your usual scrawl!   

Death must offer many occasions for poetry.   

Are you pleased, Rainer, with your new verse?   

I can’t go any further, now I’ve learned   

a language with so many new meanings.   

Goodbye. Until we meet each other   

– if we do – face to face. Look   

at the whole earth and the oceans, Rainer.   

Look at all of me.   

If you can, drop me a scribbled line   

– Happy new writing, Rainer – and   

I’ll climb a staircase bearing gifts to you   

hoping to feel your hand on my head,   

I’ll carry my New Year’s glass, without spilling   

a tear-drop, over the Rhone and Rarogne   

– your resting place – which marks our final parting.   

Put this into the hands of Rainer – Maria – Rilke!

---

### New Year’s Greetings

by [Caroline Lemak Brickman](http://hypocritereader.com/contributor/caroline-brickman/)

happy new year—happy new light, new world—happy new edge, new realm—happy new haven!   

a first letter to you in the next—   

the place where nothing ever happens   

(barely even bluffing ever happens), place where roughing,   

rushing ever happens, like Aeolus’s empty tower.   

a first letter to you from yesterday’s   

homeland, now noland without you,   

now already one of the   

stars... and this law of leaving and left, cleaving   

and cleft,   

this claw by which my beloved becomes a name on a list   

(oh him? from ’26?),   

and the has-beens transform to the unhappened.

shall I tell you how I found out?   

not an earthquake, not an avalanche.   

a guy came over—just anyone (you’re my one):   

“really, a regrettable loss. it’s in the Times today.   

will you write an article for him?” where?   

“in the mountains.” (the window opening onto fir branches.   

the bedsheet.) “don’t you read the papers?   

and won’t you write the obit?” no. “but—” spare me.   

aloud: too hard. silently: I won’t betray my Christ.   

“in a sanatorium.” (heaven for hire.)   

what day? “yesterday, day before yesterday, I don’t remember.   

you going to the Alcazar later?” no.   

aloud: family stuff. silently: anything but Judas.

II.   

here’s to the coming year! (you were born tomorrow!)   

shall I tell you what I did when I found out about—   

oops... no, no, I misspoke. bad habit.   

I’ve been putting quotation marks around life and death for a while now,   

like the empty stories we weave. wittingly.

well, I didn’t do anything. but something did   

happen, happened shadowless and echoless,   

happened.   

now, how was the trip?   

how did it tear, did you bear, did it burst   

your heart asunder? astride the finest Orlov racehorses   

(they keep up, you said, with the eagles)   

was your very breath taken, or worse?   

was it sweet? no heights, no falls for you,   

you flew on real Russian eagles,   

you. we have blood ties with that world and with the light:   

it happened here, in Rus, the world and light   

matured on us. the rush is up and running.   

I say life and death with a smirk,   

hidden, so you’ll kiss me to find out.   

I say life and death with a footnote,   

an asterisk (a star, the night I long for,   

fuck the cerebral hemisphere,   

I want the stars).

III.   

now don’t forget, my dear, my friend,   

if I use Russian letters   

instead of German ones, it’s not because   

they say that these days anything will do,   

not because beggars can’t be choosers,   

not because a dead man is a poor one,   

he’ll eat anything, he won’t even blink.   

no, it’s because that world, that light—   

can I call it “ours”?—it isn’t languageless.   

when I was thirteen, in the Novodevichy monastery,   

I understood: it’s pre-Babelian.   

all the tongues in one.

anguish. you will never ask me again   

how to say “nest” in Russian.   

the sole nest, whole nest, nothing but the nest—   

sheltering a Russian rhyme with the stars.

do I seem distracted? no, impossible,   

no such thing as distraction from you.   

every thought—every, Du Lieber,   

syllable—leads to you, no matter what,   

(oh to hell with the native Russian tongue, with German,   

I want the tongue of an angel) there is no place,   

no nest, without you, oh wait there is, just one. your grave.   

everything’s changed, nothing’s changed.   

you won’t forg—I mean, not about me—?   

what’s it like there, Rainer, how are you feeling?   

insistent, surefire, cocksure,   

how does a poet’s first sighting of the Universe   

square with his last glance at this planet,   

this planet you got only once?

the poet gone from his ashes, spirit left the body   

(to split the two would be to sin),   

and you gone from yourself, you gone from you,   

no better to be Zeus-born,   

Castor ripped—you from yourself—from Pollux,   

marble rent—you from yourself—from the earth,   

no separation and no meeting, just   

a confrontation, the meeting and the separation   

first.

how could you see your own hand well enough to write,   

to look at the trace—on your hand—of ink,   

from your perch on high, miles away (how many miles?),   

your perch of endless, because startless, heights,   

well above the crystal of the Mediterranean   

and other saucers.   

everything’s changed, nothing will change   

as far as I’m concerned, here on the outskirts.   

everything’s changed, nothing is changing—   

though I don’t know how to send this extra week’s letter   

to my correspondant—and where do I look now,   

leaning on the rim of a lie—if not from this to that,   

if not from that to this. suffering this. long suffering this.

IV.   

I live in Bellevue. a little city   

of nests and branches. exchanging glances with the guide:   

Bellevue. the fortress with the perfect view   

of Paris—the chamber with the Gallic chimera—   

of Paris—and further still...   

leaning on the scarlet rim,   

how funny they should be to you (to whom?),   

(to me!) they must be funny, funny, from fathomless heights,   

these Bellevues and these Belvederes of ours!

I’m listless. losing it. the particulars. urgency.   

the new year’s knocking at the door. what can I drink to?   

and with whom? and what indeed to drink? instead of champagne bubbles   

I’ll take these wads of cotton into my mouth. there, the stroke—God,   

what am I doing here? what auspices—what am I supposed to do,   

this new year’s noise—your death echoes, Rainer, it echoes and it rhymes.   

if such an eye as you has shut,   

then this life isn’t life, and death’s not death,   

it’s dimming, slipping away, I’ll catch it when we meet.   

no life, no death, okay so some third thing,   

a new one. I’ll drink to that (spreading straw,   

strewing flowers for the 1927th thing,   

bye 1926, what a joy, Rainer, ending   

and beginning with you!), I’ll lean across   

this table to you, this table so big no end in sight,   

I’ll clink your glass with mine, a little clink,   

my glass on yours. not tavern style!   

me on you, flowing together, us giving the rhyme,   

the third rhyme.

I’m looking across the table at your cross:   

how many places on the margins, how much space   

on the edge! and for whom would the shrubbery sway,   

if not for us? so many places—our places,   

and no one else’s! so much foliage! all yours!   

your places with me (your places with you).   

(what would I do with you at a rally?   

we could talk?) so much space—and I want time,   

months, weeks—rainy suburbs   

without people! I want mornings with you, Rainer,   

I want to begin the mornings with you,   

so the nightingales don’t get there first.

it’s probably hard for me to see because I’m down in a hole.   

it’s probably easier for you because you’re up on high.   

you know, nothing ever really happened between us.   

a nothing so purely and simply nothing,   

this nothing that happened, so apt—   

look, I won’t go into detail.   

nothing except—wait for the beat,   

this could be big (first one to miss   

the beat loses the game)—here it comes,   

the beat, which coming beat   

could have been you?   

the beat doesn’t stop. refrain, refrain.   

nothing except that something   

somehow became nothingness—a shadow of something   

became its shade. nothing, that is to say, that hour,   

that day, that home—and that mouth, oh, granted   

courtesy of memory to the condemned.

Rainer, did we scrutinize too hard?   

after all, what’s left: that light, that world   

belonged to us. we’re a reflection of ourselves.   

instead of all of this—that whole light world. our names.

V.   

happy vacant suburb,   

happy new place, Rainer, happy new world, new light, Rainer!   

happy distant point where proof is possible,   

happy new vision, Rainer, new hearing, Rainer.

everything got in your   

way. passion, a friend.   

happy new sound, Echo!   

happy new echo, Sound!

how many times at my schoolgirl’s desk:   

what’s beyond those mountains? which rivers?   

is the scenery nice without tourists?   

am I right, Rainer, rain, mountains,   

thunder? it’s not a widow’s pretension—   

there can’t be just one heaven, there’s bound to be   

another one, rainier, above it? with terraces? I’m judging by the Tatras,   

heaven has to look like an amphitheater. (and they’re lowering the curtain.)   

am I right, Rainer, God’s a growing   

baobab tree? not a Louis d’or?   

there can’t just be one God? there’s bound to be   

another one, rainier, above him?

how’s writing in the new place?   

if you’re there, there must be poetry. you   

are poetry. how’s writing in the good life,   

no table for your elbows, no forehead for your strife,   

I mean your palm?   

drop me a line, I miss your handwriting.   

Rainer, do you delight in the new rhymes?   

am I getting the word rhyme right,   

is there a whole row of new rhymes,   

is there a new rhyme for death?   

and another one, Rainer, above it?   

nowhere to go. language is all learned up.   

a whole row of meanings and consonances   

anew.

goodbye! see you next time!   

we’ll see each other—I don’t know—we’ll sing together.   

happy land I don’t understand—   

happy whole sea, Rainer, happy whole me!   

let’s not miss each other next time! just write me beforehand.   

happy new soundsketch, Rainer!

there’s a staircase in the sky, lined with Gifts.   

happy new ordination, Rainer!

I’ve got them in my palm so they won’t overflow.   

over the Rhone and over Raron,   

over the clear sheer separation,

to Rainer, Maria, Rilke, right into his hands.
----------------------------------------------

*From [new year: a translation](http://hypocritereader.com/26/new-year)*

![小于一](http://upload-images.jianshu.io/upload_images/52389-c840d31c47e4d91e.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



---


`@bintou`
`2019-08-05 18:13:54`
`字数 2561`
`阅读 1586`


《族长的秋天》的读书笔记
============

`读书笔记`

---

以下内容只是一份笔记，不具有任何解读意义。

> 《族长的秋天》，1975年，加西亚.马尔克斯，轩乐译，南海出版社，2014年6月.

![族长的秋天](http://upload-images.jianshu.io/upload_images/52389-11291c1c0f2decb7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 主要线索

全书被出版者分为6部分（258页）。每一部分不再分段，大概40页（32开）左右，基本没有句号。阅读上最大的障碍是要仔细区分第一人称叙事者为谁，因为“我”在不断变换，故事的叙述者是无缝切换的。似乎每一部分都可以以一个人物作为线索：

第一、**帕特里希奥.阿拉贡内斯**：完美替身，曾经是假冒总统的骗子、吹玻璃的工人。被剧毒标枪刺中而死。

第二、**玛努艾拉.桑切兹**：狂欢节女王、穷人的选美皇后、总统念念不忘的女神。消失于日食之夜。

第三、**罗德里戈.德阿吉拉尔将军**：国防部长、总统卫队司令、国家安全部负责人。试图颠覆政权，最终被烤熟端上餐桌。

第四、**本蒂希翁.阿尔瓦拉多**：总统的母亲、国母、神医、养鸟大师、平民之神、圣人（或者伪圣人）。去世之后总统导演了一出精彩的为自己母亲封圣的大戏。

第五、**莱蒂西娅.纳萨雷诺**：婊子修女、女王、唯一的皇后，粗俗、贪婪、乖戾、伪善，生下一子，最后同时被60只饿狗吞食。

第六、**何塞.伊格纳西奥.萨恩斯.德拉巴拉**：太子党、秘密警察、暗杀者、隐藏的绝对权力、嗜血的恐怖机器、潜在的接班人，只身带着一头恶犬：科尔勋爵（只吃人肠子）。被终结于群众盲目公正的惩罚：被石头砸烂。

### 次要线索

**族长的名字**：老马在《番石榴飘香》中道，《族长的秋天》他三易其稿，第二次的时候是把第一稿全部推翻了，只保留了一个名字，就是族长的名字。在这本书中，族长的名字就出现了一次：

> “一个晚上，他写下了我叫撒迦利亚（Zacarias，耶和华已纪念之意），然后在灯塔忽闪的光亮中念了一遍，又念了一遍又念了很多遍，最终那个被重复多次的名字竟让他觉得遥远又陌生，真他妈见鬼，他自言自语着将纸条撕碎，我就是我，”（P.122）

**萨图尔诺.桑托斯将军**：纯正的印第安人，赤脚，腰间别一把永不离身的甘蔗砍刀，总统的贴身护卫，直到老去，请求一死。

**佛朗西斯卡.里内洛**：高寿，最后被以皇后之礼厚葬。

**德梅特里奥.阿尔窦斯**：教廷的礼仪部顾问、信仰检查官兼列圣申请官，负责调查核实总统母亲封圣之事。

### 不断重复的文学元素

* 没有军衔标志的粗布制服
* 总统卧室的那三把门环、三道门闩、三个插销和移动马桶
* 穿着军靴，戴着金质马刺，弯着手臂垫在脸下当做枕头
* 从总统卧室窗户看出去，海面上那远航舰队司令的三艘三桅船
* 玫瑰花从中的麻风病人和瘫痪患者

### 文字摘录

> P.1. 周末，一些兀鹫钻进了总统府的阳台，啄断了金属窗栅，振翅搅乱了屋内凝滞的时光，礼拜一的黎明时分，城市从几个世纪的昏睡中苏醒，一阵温软的微风拂过，伴着伟大的死尸与腐朽的伟大散发出的气息。（全书第一句。）
> 
> P.18. 他会叹息着说，母亲，祖国是最伟大的发明......
> 
> P.35. 他宣布大赦，在展望未来时有了神奇的想法，这个国家的问题就在于民众有太多空闲的时间思考......
> 
> P.73. 他强忍着太阳穴冰冷的刺痛，只是为了不让人发现他年老的衰残，只是为了让你在他耗尽了一切资源之后，因为爱而爱他而不是因为怜悯而爱他，只有与你在一起时他才这般孤独，我甚至几乎没有气力待下去了，我摩挲着她，苟延残喘，直到真人大小的天使长在屋中敲着我的丧钟飞过，在她为避免海蛀虫把那些玩意儿蛀成粉末而将它们放回各自的匣子时，他喝下了这次探访的最后一口饮料，就一分钟，皇后，他的起身耗尽了自己现在到明天的时间，耗尽了一生的时间，太糟糕了，几乎没有余下一刻能让他最后瞥一眼那无法触碰的少女，她已随着天使长的来临和他的离去而僵在原地，膝头的玫瑰也已枯萎凋亡，他在夜幕初垂时逃离，试图掩盖流言蜚语带来的羞耻......
> 
> P.99. 他妈的，你为什么想死，那外乡人不带一丝羞耻地回答说，为祖国而死是至上的荣耀，阁下，而他带着怜悯的微笑回应他，别傻了，孩子，祖国就是活着......
> 
> P.117. 尊贵的罗德里戈德.阿吉拉尔大将军躺在与他身长相当的银质托盘中被端进了屋，身下还铺着花椰菜与月桂叶组成的配菜，他在调料中腌得瘫软，在烤箱中烤得金黄，身上套着出席庄重场合穿的饰有五颗金杏仁的制服，半袖上佩着一枚枚因英勇无比而被授予的肩章，胸口摆放着十四磅的奖牌，嘴上搁着一小把欧芹，只待切割匠人在这场战友们的宴会上，在惊惧得石化了的客人面前将他们切分、装盘，我们屏息见证了这场精致的分尸与分享仪式，当每个盘子中都盛有一份分量相同、有着松仁与香菜做馅儿的国防部长后，他下达了开饭的命令，祝各位好胃口，先生们。
> 
> P.149.这个国家并不是我由着自己的性子选的，而是像您所看到的一样是他们定好了塞给我的，从最开始就是这样不现实的感觉，这样的狗屎味道，这样的没有历史、只求苟活的小民，都没人问过我就把这个国家强加给我了......
> 
> P.161. 我们没有其他的祖国，只有那个依据他个人的想象和偏好建成的祖国，它拥有被他的绝对意志的构思改变的空间与被校正的时间，它被从他自己记忆中最模糊的源头重建起来......
> 
> P.256. 在他最不想要它降临时，它降临了，在如此多年的贫瘠幻想之后，他开始隐隐明白，人不是在生活，真他妈见鬼，而是在苟活，人开始学习时已经太晚，即便是最博大最了不起的生命也仅能达到学习怎么去活的程度，他从自己喑哑手掌的谜团里、从纸牌隐形的密码中，意识到了自己没有能力去爱，于是企图用权力的孤独罪恶的炽烈祭礼去补偿那无耻的命运，却在无尽燔祭的火焰中沦为自己献祭主张的牺牲品，他以诓骗与罪行养肥了自己，以无情与羞辱培育了自己......
> 
> P.257. 谎言比质疑更舒心、比爱更有用、比真理更持久，他已经并不意外地到达了可耻的臆想境地，无权力却在统治、无荣耀却受赞颂、无威信却被遵从，而此刻，在他秋日的那串飘落的黄叶中，他相信了，他从来就不会是他全部权力的主宰，他注定只能颠倒着认识生命，注定无法参透世事......
> 
> P.258. 他在他秋天的最后几片冰冷树叶的阴暗声响中，飞向了被遗忘的真相的黑暗祖国，他惊恐地抓着死亡长袍上的破布烂线，远离了疯狂人群的呼喊，他们冲上街头唱着欢快的颂歌、庆祝他的死亡，他也将永久地远离那自由的音乐、幸福的焰火和荣誉的钟声，它们正向世界宣告一则好消息，宣告那永恒的无尽时光终于结束了。（至此，全书终。）

---

2019.08.05 转移至此



---


`@bintou`
`2017-02-07 17:59:39`
`字数 437`
`阅读 1824`


《族长的秋天》的六条线索
============

`读书笔记`

---

全书被出版者分为6部分，似乎每一部分都可以以一个人作为线索：

第一、帕特里希奥.阿拉贡内斯：完美替身，曾经是假冒总统的骗子、吹玻璃的工人。死于剧毒。

第二、玛努艾拉.桑切兹：狂欢节女王、穷人的选美皇后、总统念念不忘的女神。消失于日食之夜（妈的，晚上还有日食！）。

第三、罗德里戈.德阿吉拉尔将军：国防部长、总统卫队司令、国家安全部负责人。试图颠覆政权，最终被烤熟端上餐桌。

第四、本蒂希翁.阿尔瓦拉多：总统的母亲、国母、神医、养鸟大师、平民之神、圣人（或者伪圣人）。去世之后总统导演了一出精彩的为自己母亲封圣的大戏。

第五、莱蒂西娅.纳萨雷诺：婊子修女、女王、唯一的皇后，粗俗、贪婪、乖戾、伪善，生下一子，最后双双被饿狗吞食。

第六、何塞.伊格纳西奥.萨恩斯.德拉巴拉：太子党、接班人、秘密警察、暗杀者、隐藏的绝对权力、嗜血的恐怖机器，只身带着一头恶犬：科尔勋爵（只吃人肠子）。被终结于群众盲目公正的惩罚：被石头砸烂。

只是粗略的线索，不具有任何解读意义。



---


`@bintou`
`2015-10-01 01:14:10`
`字数 1483`
`阅读 2122`


健康的基本判定原则
=========

`随便说说`

---

现代人普遍都注重身体的健康：吃健康食品、常做健康运动，但是普通人又常有一个小小的误区，不知道什么是健康。我们看一个人是否健康，通常会说，“这个人健康啊，会吃，会养生！”，或者说“这个人健康，经常跑步打球！” 最近，关心我的同事常说的一句话就是，斌头是很健康的，以前常跑步打球.....我只能苦笑了。看来我们没有把握好健康的基本判定原则啊，也就是说，没有能够把“不健康”在日常的生活中找出来。如果我们总是能发现我们身体不健康的东西，并摒弃它，那么才能真正做到健康。这也是中国古话里常说的“上工治未病”，在没有病的时候就开始治疗。

说到这里，也许大家会说，我每年都体检啊，有病自然就检查出来了。这真是很值得一谈的话题！有一个病人，心脏很不舒服，跑去找医生，医生一看就说，你年纪轻轻的会有啥心脏病啊，死不了！病人坚持说，你给我检查一下呗。好，做个心电图。完了，医生就说，你看看，你看看，一点问题没有......打发病人走了。到晚上，这病人就因为心脏病发作挂了。这是真实的事情，而且这种事情不断在发生。我也碰到过类似的情况，幸运的只是没有出现不幸。难道实验仪器不科学？难道医生要坑你？我不这样理解，我只能说数据、仪器有一定的局限性。科学的方法是重要的手段，但不是所有的手段。反正，我取消了今年的常规身体检查。

还有这样的一个实例，来自《梁冬对话倪海厦》（一个访谈节目），大家看了思考一下，也许有启发（当然，也可能有错误！）。大概说的是对糖尿病的检查，判断一个人是否得了糖尿病通常是检查人体内的血糖成份。两个相同的杯子，一个杯子里盛满水，一个杯子放半杯水，然后分别放一汤匙的白糖，请问哪一杯水的糖份高？当然是半杯水了。那么，两个人一个被检查出血糖高而另一个正常，有没有可能一个人身上的水份少另一个人身上水份多呢？似乎，我们没看到医生要给病人进行“水份检查”。这位医生其实是想说，很多糖尿病人其实血糖并不高，而是身上缺水。如果你只是把糖份减下来而不是把导致所谓“高”的另一个原因医治好，那么其实是治疗错了。进一步他强调，很多糖尿病病人并不需要进行治疗，只要他健康（见下面）我就不治疗。我必须强调一下，我对医学没多大的认识，举这个例子我不一定要认为这位医生一定正确，我只是更欣赏他那种看待病人或者病的方法，即判断人是否健康的几大基本原则。

*1. 饮食是否正常；即一日三餐，定时就饿，饿了就想吃。想吃很重要！   

2. 睡眠；没有失眠，早睡早起，一觉到天亮。晚上定时会醒比较糟糕。   

3. 大小便；大便一日一次，早上为好；小便正常，淡黄色无泡沫。大便不正常是病。   

4. 手足保持温热，即不会经常手冷脚冷。手足温热的人大概就是阳气盛的人吧，不会有心脏病。*

这几大准则能帮你做出一些重大的判断。一旦体检报告这个高哪个高的，你就问自己这几个问题，如果都正常，那就不要担心，数据只说明某些问题，但自己还是健康的啊。信心满满地，乐观地思考一下，千万不要被数据吓倒。

其次，在你生病的时候，医生开了处方，吃了你不知道是否有效，也可以按这个标准去判断。这也是很重要的，比如，感冒通常不吃药也能好，那我怎么知道我吃的只是安慰剂？吃了药下去，很快胃口回来了，手足不冰冷了，睡眠也正常，那么说明药对症，否则说明这药没啥效果。千万不要小看这个啊，如果你把刚才说到的“感冒”推广到其他重症当中，你就会明白了。

最后最重要的就是，通过这些来判断自己是否健康。不要再犯“经常跑步，很健康”这样的错误了，日三省吾身：吃爽了？拉好了？睡足了？手脚热么？我相信，以这个标准，能较准确地发现问题，尽早医治，从而保护自己和家人。



---


`@bintou`
`2017-07-04 05:06:36`
`字数 2294`
`阅读 8695`


写给华南师范大学计算机学院准大一新生的一封公开信
========================

`非鸡汤文`

---

各位同学，大家好！你我彼此还不认识，冒昧给你们写这封信，在你们刚摆脱了高考的残酷束缚即将迎来新的学习生活之际。无论你们此刻是兴奋异常还是稍有失落，都请耐心地听我说几句。因为我知道，在小学、初中、高中督促你们学习的父母大部分已经不再担心你们的学业，或者再也无法找到可以给你们报读的补习班了，所以，立正、稍息，补习开始！

我是一位普通教师，你们未来的老师，即将给大一新生上《计算机科学技术导论》课。之所以我能说以下这些话，是因为我似乎在过去十年的学生中看到了你们未来，仿佛你们即将重复巡演着并无二致的剧情。之所以我必须说以下这些话，是因为，我希望，你们每一位都能实实在在地做好独一无二的自己。因为是普通老师，所以，以下的话没有玄机妙理，没有豪情万丈，只是一些建议。

首先，你们必须抓紧英语的学习。关于英语的学习，我不是专家，专家也说得够多的，也插不上话。为什么要学英语？因为，我大中华五千文明古国，中文博大精深，实在不容易学！学英语干啥？用呗：看英语教材，听英语专业课，进行国际交流。请注意：大部分优秀的教材都是用英文写成的，为了可以读英文教材，我必须努力学习英语。大一的[《计算机科学技术导论》](http://download.csdn.net/detail/scnu_wlb/8165761 "计算机科学")用的就是英文教材。在过去的十年，有数不清的学生问，老师，我看中文的行吗？我都统一答复：你中文太差，看不懂，还是看英文吧。读计算机，需要大量使用英语，但也不要担心所谓的“专业英语“，把基础英语学好再说吧。

**为避免误会，我必须强调：中文的阅读写作也非常重要。**大部分同学的中文不是太好，而是太差。大部分同学中文差并不是因为花多了时间学英语读英语著作写英语文章，而是因为没花时间学中文。相信我，多学英语不会搞糟你的中文能力。

其次，我要开始吧啦吧啦讲一堆你们不懂的术语（此处省略5千字），描述计算机科学的伟大蓝图（此处省略1万字），指明你们未来的发展方向（此处省略5百字）。结论：你们四年后将享受一份工作强度不大、年薪极高的职位：IT精英！当当当～～演讲结束，回到现实。此段可忽略！

再其次，你们在未来的一年将迎来史无前例繁忙的功课，我非常严肃地！说了无数次，考上大学就轻松了，那是你妈骗你的好吧？大一第一学期：高等数学、线性代数、程序设计语言，任意一门都有可能压得你喘不过气，而学这些连计算机科学的门都没摸到呢......任何一个有志的学子，请听我第二个建议：不要被课程追着屁股赶着走，要走在课程的前面。也就是：要预习，要预习，要预习。

预习什么？作为一位靠谱的普通老师，我暂时只推荐以下课程：

* [How to Think Like a Computer Scientist: C version](http://www.gimeko.edu.rs/wp-content/uploads/2016/11/ThinkC.pdf) 或者 [How to Think Like a Computer Scientist: C++ Version](http://www.greenteapress.com/thinkcpp/thinkCScpp.pdf)。两者有微妙的区别，完全没基础的可以看前者。
* [MIT：Linear Algebra](http://v.163.com/special/opencourse/daishu.html), [对应教材](http://download.csdn.net/detail/u013640035/6929197)

也不要贪多，多了也学不来。这些书都是适合阅读自学的，所以推荐给大家，而且Linear Algebra这门课还有视频呢。然而也许会有同学说，怎么还是理论到理论的课程，有没有一些时下最流行的知识？我思量了许久，不知道是否现在可以抛出我的经典答复......算了，等你们见了我再说吧。真心希望有同学可以沉心静气地读两本书，就这么简单。

大学是什么样子？大学无论是什么样子，肯定不是你想像的那样子！从中学到大学，不仅仅是一种身份的转换，而应该是从理想到能力全面脱胎换骨的涅磐重生般的激变。我总是喜欢嘲笑一些同学不是在读大学，而是在读高四高五。因为他们还不懂得自主读书，不是到大学求学，而是到大学等老师求他们学；他们往往能看到自身的不足，但是缺乏勇气去改变自己；他们往往看到了少许的社会阴霾，于是胆怯地蜷起自己游离其外，试图独善其身。鼓起勇气，改变自己！

改变自己的第一步就是需要改变学习方法。大学课程需要大量的阅读。最近我看了一些高中课本，总算明白为何大学生为何不阅读了，我理解是，他们从来没有阅读的训练，高中课本太单薄。所以，第一步就是大量阅读。其次，大量阅读。第三，吧啦吧啦。第四，吧啦吧啦。总结，大量阅读最重要。缺乏第一步，其他的说也白说。

噢，差点忘了给那些苦着脸想对我说“我不喜欢计算机！”的同学打个招呼了。其实，那些所谓“喜欢计算机”的同学也不是真的喜欢，他们以为学计算机可以天天打游戏而已，那么你这号称“不喜欢“的同学也就不值得大惊小怪了，学计算机并不是要你去修电脑铺网线，别担心，计算机专业绝不是你想像的那个样子！二十年前计算机专业非常热门，那是虚热。现在计算机专业似乎冷门，那是假冷。这只能反映国人对大学教育、学科教育的无知，反映了中国职业市场对人才需求的不理性与不成熟（直白而言就是Low）。作为一门学科，无论冷热，我们需要做的是：发现其本质、遵循其发展规律。

[大学教育并非职业教育](https://www.zybuluo.com/bintou/note/314482)，高校计算机教育的发展不应该也不会以IT职业市场的需求为指针。那些只想混张文凭找份工作的同学也许会很失落的，因为他们在大学校园将找不到他们理想的位置。如果你真的不喜欢所谓的IT行业，那你完全可以把读计算机专业看为素质教育，读好了你完全可以自由地选择自己的职业。无论你是喜欢还是不喜欢，你们都需要摆正心态，做好克服困难的准备，迎接挑战。

总结一下，三个学习任务：学英语、学编程、学数学。变换角色，改变心态，大量阅读（如果你问有什么可读，请点[这份推荐](https://www.zybuluo.com/bintou/note/131465)！），雕琢自身，迎接挑战。欢迎来Email: bintou2010@qq.com，欢迎提任何意见，我将及时作出更新和调整。

预祝大家有愉快的大学生涯！

斌头老师   

2015年7月10日下午



---


`@bintou`
`2017-05-06 17:52:37`
`字数 2035`
`阅读 3122`


指数函数与欧拉公式
=========

`高等数学`

---

数学的学习需要直观。比如我们应该问：到底指数函数是怎么想出来的？为什么会等于那么一大堆无穷的级数和？是偶然还是必然？是发明还是发现？

以下内容您只需要知道一些基本的高等数学的常识，比如，一阶导数。也就是说即使高数挂科者也可轻松阅读。

### 直接构造法

在没有这个函数之前，也许数学家是想找一个函数：它的一阶导数刚好是该函数本身。如果把一阶导数看为函数所表示曲线的加速度，那么就是说**这条曲线的加速度函数就是自己本身**。我尚不知道数学家们出于何种动机非要找这样的函数。只是可以猜想，或许欧拉等人很早就发现了这样的函数，比如：

 (公式1）

对公式1做一阶求导，会发现：。求导之后，1没了，变成1， 变成......所以，这个就是我们想要的那个函数，将此函数命名为。并且我们知道。

以上的表达是说，我们想要一个函数，刚好，很容易我们就发现了这个函数，Happy ending。如果数学家们满足于这个状况，也许下面这些内容就没有了。

### 多项式构造法

当然数学家们不仅仅满足于找到这么样一个函数。我们通过公式本身要问的是，是不是所有的曲线（函数）都可以表示成（）（多项式）的累加？是否所有的函数都会有这样的形状？

 （公式2）

如果是，我们如何求出这些系数：？注意，此时假定我们知道这个函数的某种表达（不是上面这种形式），记为。

现在需要一点高阶导数的内容，其实就是一阶导数不断做下去。思考这样的思路：如果在这个点上，，而且， ， ...，即的n阶导数等于的n阶导数，直到无穷，我们能说与 相同吗？似乎我们没有拒绝的理由。考虑一下函数，记住，的导数就是自己本身。

首先，注意到，在的情况下，无论多少次求导，都等于1！

然后，在的情况下，对不断求导得到的是：

，， ， ......， (序列1）

现在要使得这一个数列的每一项都等于1，也就是说，要求：

，

把它们代入公式2，刚好得到公式1。注意，是因为要求在这个点上，。

### 泰勒展式与欧拉公式

到底是那种情况下找到的？我猜是第一种比较直接的方式，后面是一种发现。而且后面这种发现只是欧拉公式的一个阶段性产品。当然，都是猜。因为，是欧拉等人熟知的，所以，有意思的是能否找到其他函数能表示成的累加。比如，、这样的函数跟（多项式）有什么关系吗？

同样的方法，我们知道如何对函数求导,得到它在的数值，就得到这样的序列：

0， 1， 0， -1， 0， 1， 0， -1，...... （序列2）

因为要求序列1与序列2相等，所以，

, , , , ......

很高兴地发现，偶数项全归0了，而奇数项一正一负地摇摆，其实这就得到了大家都很怕的那个所谓的"太乐"展式：

 （公式3）

同样，也可以求得：

 （公式4）

讲到这里，故事的高潮才逐步出现，以上内容其实都还比较简单。只有在这个神奇的数字引入之后，整个世界才开始奔放起来了。所谓，无非是说 。(很崇拜提出这个的人！)如果只是把i理解为一个数，实在没有道理不能把它带入到这个函数当中，是吗？现在，我们考虑！

的展开式我们是知道的，难道不能照葫芦画瓢展开吗？

其实我没干太多事情，只是把带入到公式1当中，然后我们再把展开，因为我们知道，然后我们得到一系列数字，有正有负。关键还有一点，有些没有消掉，我们把不带的归一类，带（只能有一个哟！）的归一类看看：

 （公式5）

把公式5与公式3和公式4对比一下，可知：

这就是著名的欧拉公式！Perfect～

能在张牙舞爪的数学公式与定理中发现直观，体会发现的乐趣，才能触摸数学入门的门道。

本文的内容归功于[MIT的“微积分重点”公开课](http://open.163.com/special/opencourse/weijifen.html)，本人做了一些简单的复述工作。建议大家看看这个公开课视频。



---


`@bintou`
`2019-08-05 18:02:05`
`字数 3129`
`阅读 3148`


《线性代数》重点--从CS的角度
================

> **线性代数**研究有限维向量空间中的**线性操作**。--马克.吐温

### 前言

《线性代数》是计算机专业的基础课，具有重要的理论与实践意义，教学效果的好坏直接影响了学生的长期发展。无论如何强调其重要性都不为过。为此，非常有必要在学习的早期给予学生正确的学习指导。本文试图从计算机专业的角度，对大一新生学习《线性代数》课程给出若干指导与建议，其中包括重点知识的概括等。

### 推荐教材

[Introduction to Linear Algebra](http://math.mit.edu/~gs/linearalgebra/), Gilbert Strang, Wellesley-Cambridge Press, ISBN：0980232775, 9780980232776, 2016.

![GSLAv5](http://upload-images.jianshu.io/upload_images/52389-3fda91b9186b98c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 教学目标

《线性代数》研究有限维向量空间中的**线性操作（线性变换）**的一门学科，主要研究线性操作的表达、化简、分类等。学习线性代数的重要性体现在两个方面：   

- 应用的基础方法   

- 理论的研究工具

除了理论与实践上的意义，人们还通常把《线性代数》中的概念、知识作为一种**通用语言**，广泛地应用在各种问题的描述当中，比如，量子计算。因此，学习《线性代数》就同时要求学生**熟练掌握**相关概念与应用。

### 重要知识点概括

#### 向量

向量（Vector）：向量表示n维空间中的一个点。为了简化，回忆一下大家熟悉的二维空间中的(x, y)。然后，定义两种操作：加法、标量乘。有了点，当然可以组成线、面、体。进而考虑向量的长度、向量之间的夹角（正交性）、向量的平移、向量的投影、向量的翻转等。以上内容都有对应的数学表示。

![向量的操作](http://upload-images.jianshu.io/upload_images/52389-f8459a8f5c03046f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 向量空间

向量空间（Space）：给定一个向量集合V，定义关于向量的加法和乘法，如果对V中元素不断运用加法和乘法得到的元素满足若干属性，则V为一个向量空间。空间的子集如果也形成空间，称为子空间(Subsapce)。对线性代数的研究动机源自于人类试图研究认识高维空间。人类在认识理解高维空间的过程中发现，直观和想象竟然失效，于是只能借助抽象和理论工具。

#### 基

基（Base）：如果V中子集B的向量两两线性独立并张成（Span）V，则称B为V的基。每个有限维向量空间都存在一个Base。就好比生物学家要研究组成生物的最小单元一样，我们要给出构造出空间的最小向量集合，并研究它们的属性。

#### 四大基本子空间

四大基本子空间包括：行空间、列空间、零空间、左零空间。这个知识点可以说是重中之重，是一种理解线性操作的通用工具和语言。通过使用四大基本子空间，许多知识点的表达非常直观。比如：最小二乘法。例子很多，务必体会！

![四大基本子空间](http://upload-images.jianshu.io/upload_images/52389-4bab9f3ac337e74a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/640)

#### 矩阵

矩阵（Matrix）：矩阵是线性操作的一种抽象表达。一般而言，在许多《线性代数》课程中，矩阵操作也许是讲得最多的内容，但矩阵在线性代数中的内涵往往会被忽略。一般而言，这些课程往往先引入线性方程，从线性方程中抽象出矩阵，然后进行高斯消元，求方程的解，求矩阵的逆矩阵等，然而对矩阵的本质解释得非常非常少，或者说没有对矩阵的内涵进行必要的强调。

必须强调的是，把矩阵看为对线性映射的一种抽象表达更接近线性代数的本质。从函数的角度看，如果作用于向量v函数F具有线性性（即线性函数），则这个F函数就可表达为一个矩阵M，称为操作子(或算子，Operator)。线性代数中会重点研究某些具有特定含义的矩阵，比如，单位矩阵、对角矩阵等。到了具体的学科中，比如量子力学，不同的矩阵就表征为不同的操作子：泡利矩阵、哈达玛矩阵等。从更本源上看，研究矩阵的目的是为了研究线性操作的表达、化简、分类等。

矩阵如果用在其他学科，它就是研究工具；在工程中，就是一种实践工具。但是在线性代数中，我们研究的主体就是矩阵本身，需要考察不同操作子所必须具备的属性。因此，以下关于矩阵的概念就非常重要。

#### 行列式

Determinant（行列式）：行列式是一种让人崩溃的翻译。更遗憾的是，我没办法对Determinant给出一种直观，在任何一本课本都难以找到明确的直观。原因我只能归结为，Determinant所包含的信息实在是太多！矩阵的行列式是一个数值，通过它可以发现矩阵的特性，比如说，矩阵是否可逆。想象力在内容过于丰富的时候失去了效力，在此我们必须借助定义，了解行列式所必须遵循的若干性质。

#### 特征值和特征向量

特征值（Eigenvalue）和特征向量（Eigenvector）：如果对矩阵的理解不站在“线性变换”这个角度上看，理解特征值和特征向量是有难度的。但是，如果把矩阵T看成操作子：   

`T u = lambda * u`   

就可以解读为，给定一个向量u，进行T变换，得到一个“不变量”：仅仅是u在某一个方向上的延展，即标量lambda乘u。把上式右边移到左边，利用单位矩阵I，可得：   

`(T - lambda*I )u= 0`   

式子左边的`(T - lambda*I )`还是一个矩阵，使得不为零的向量`u`为`0`，则该矩阵必须是奇异矩阵。满足条件的非`0`向量`u`就是特征向量。

#### 矩阵分解（Factorization）

再次强调，线性代数研究线性操作的表达、化简、分类等。矩阵是线性操作的抽象表达，因此研究矩阵的分解就是研究线性操作的表达、化简、分类。请重点关注以下矩阵分解（Factorization）   

a、LU分解、LDU分解   

b、QR分解   

c、矩阵的特征向量特征值分解   

d、SVD分解

请看Gilbert Strang对[矩阵分解](http://math.mit.edu/~gs/linearalgebra/linearalgebra5_Matrix.pdf)的总结：15种分解。

#### SVD分解

SVD分解具有非常特殊的重要性，值得单独拿出来强调。有科学家赞誉*SVD是线性代数皇冠上的宝石*。首先，SVD这个知识点基本将以上知识点融会贯通，是理解线性操作乃至于理解线性代数的有力工具，就这一点就值得赞叹。再加上，在实际工程应用中，SVD的应用场景数不胜数，更凸显其意义非凡。

#### 小结

以上概念组成了《线性代数》的重点，也基本覆盖了这门课的主要内容。学习线性代数的硬伤在于：**没有对整个知识体系建立准确的概念、思路与直观**。很多同学会问，线性代数有什么用？经典的回答是，很有用，到处都用，奠定基础，锻炼思维，bilibili。

也许**提问本身有问题**。我更愿意大家问：什么是这门课程的研究学习动机（motivation），研究的主体是什么，学习研究的思路应该如何，直观在哪里？**回答也有问题**，任何一门学科源自生活又超越生活，单纯从应用或者理论的角度去看都会非常狭隘。从本源出发指出动机、描述理论的整体框架、在此基础上指出学习的思路与重点等都有助于学生进一步学习。

### 若干建议

#### 1. 注重编程和实践

a、用C语言编程实现相关矩阵操作：矩阵乘法、求逆、高斯消元......   

b、用Sage（[什么是Sage？](http://www.jianshu.com/p/d3e723ec77bb)）练习相关操作；GSLA等书要求普遍是MathLab，但是MathLab不是免费开源软件。   

c、关注相关操作的算法描述（即使在开始做不到，也要在之后练习），算法的复杂性等内容。

#### 2. 学习公开课视频

[MIT公开课：线性代数](http://open.163.com/special/opencourse/daishu.html) （全部带中文字幕）。授课老师就是MIT的Gilbert Strang，听他讲课是一种享受，强烈推荐。

#### 3. 参考书及网络资源

* Introduction to Linear Algebra，Lee W. Johnso 等，机械工业出版社，第5版 。
* Linear Algebra with Applications, Steven J. Leon, 机械工业出版社引进版，第9版， 2017
* Linear Algebra Done Right，Sheldon Axler，第二版，Springer，电子书，或者世界图书出版社引进版。（注：可作为第二阶段学习教材。）
* [The future of linear algebra](http://www.maths.adelaide.edu.au/anthony.roberts/larxxia.php)，电子书。（注：其中强调SVD部分值得看看。）
* [A First Course of Linear Algebra](http://linear.ups.edu/)，电子书。（注：尤其推荐此书中[使用Sage的部分](http://linear.ups.edu/download/fcla-3.50-sage-6.9-primer.pdf)）。

2014年9月起草   

2017年6月修订   

2019年8月转移到此



---


`@bintou`
`2018-11-08 18:00:35`
`字数 364`
`阅读 1535`


某智力题的解题步骤
=========

`未分类`

---

解题步骤

1、校长选定的数字序列之和记为S，则必然是一个唯一的整数。

2、如果某个教授可以猜中这个，是否能写对自己帽子上的数字？答案是：可以！因为，他只是不知道自己帽子上的，而可以看到其他人的数字；然后，代表其他教授帽子上数字的和，代表这位教授帽子上的数字；解同余方程，可以知道。

3、但是，如何确保某个教授能猜中呢？简单，因为落在中，现在有位教授，让他们每个人猜一个即可。准确来说，可以先给每一位教授一个从0到的唯一编号，等校长写完数字，他们用自己的编号作为，计算出，去解那个同余方程，得到，那就是自己帽子上的数字。

4、以上分析表明，必然至少会有一位教授可以准确地猜出自己帽子上的数字。校长必输。



---


`@bintou`
`2018-06-10 17:27:17`
`字数 107`
`阅读 1506`


Some Codes
==========

`未分类`

---

```int quick\_pow(int a, int k)   

{   

int res = 1;   

while( k > 0)   

{   

if ( (k % 2) == 1 )   

res = res \* a;   

a \*= a;   

k = k / 2;   

}   

return res;   

}

```



---


`@bintou`
`2017-11-30 05:42:48`
`字数 2743`
`阅读 1822`


Queue in C/C++
==============

`未分类`

---

```


1. // C program for array implementation of queue
2. /*
3. Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
4. Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
5. Front: Get the front item from queue.
6. Rear: Get the last item from queue.
7. */
8. #include <stdio.h>
9. #include <stdlib.h>
10. #include <limits.h>
12. // A structure to represent a queue
13. struct Queue
14. {
15. int front, rear, size;
16. unsigned capacity;
17. int* array;
18. };
20. // function to create a queue of given capacity.
21. // It initializes size of queue as 0
22. struct Queue* createQueue(unsigned capacity)
23. {
24. struct Queue* queue = (struct Queue*) malloc(sizeof(struct Queue));
25. queue->capacity = capacity;
26. queue->front = queue->size = 0;
27. queue->rear = capacity - 1;  // This is important, see the enqueue
28. queue->array = (int*) malloc(queue->capacity * sizeof(int));
29. return queue;
30. }
32. // Queue is full when size becomes equal to the capacity
33. int isFull(struct Queue* queue)
34. {  return (queue->size == queue->capacity);  }
36. // Queue is empty when size is 0
37. int isEmpty(struct Queue* queue)
38. {  return (queue->size == 0); }
40. // Function to add an item to the queue.
41. // It changes rear and size
42. void enqueue(struct Queue* queue, int item)
43. {
44. if (isFull(queue))
45. return;
46. queue->rear = (queue->rear + 1)%queue->capacity;
47. queue->array[queue->rear] = item;
48. queue->size = queue->size + 1;
49. printf("%d enqueued to queue\n", item);
50. }
52. // Function to remove an item from queue.
53. // It changes front and size
54. int dequeue(struct Queue* queue)
55. {
56. if (isEmpty(queue))
57. return INT_MIN;
58. int item = queue->array[queue->front];
59. queue->front = (queue->front + 1)%queue->capacity;
60. queue->size = queue->size - 1;
61. return item;
62. }
64. // Function to get front of queue
65. int front(struct Queue* queue)
66. {
67. if (isEmpty(queue))
68. return INT_MIN;
69. return queue->array[queue->front];
70. }
72. // Function to get rear of queue
73. int rear(struct Queue* queue)
74. {
75. if (isEmpty(queue))
76. return INT_MIN;
77. return queue->array[queue->rear];
78. }
80. // Driver program to test above functions./
81. int main()
82. {
84. struct Queue* queue = createQueue(1000);
86. enqueue(queue, 10);
87. enqueue(queue, 20);
88. enqueue(queue, 30);
89. enqueue(queue, 40);
91. printf("%d dequeued from queue\n", dequeue(queue));
93. printf("Front item is %d\n", front(queue));
94. printf("Rear item is %d\n", rear(queue));
96. return 0;
97. }

```
```


1. /*
2. The functions supported by queue are :
3. empty() – Returns whether the queue is empty
4. size() – Returns the size of the queue
5. front() – Returns a reference to the first element of the queue
6. back() – Returns a reference to the last element of the queue
7. push(g) – Adds the element ‘g’ at the end of the queue
8. pop() – Deletes the first element of the queue
9. */
10. #include <iostream>
11. #include <queue>
13. using namespace std;
15. void showq(queue <int> gq)
16. {
17. queue <int> g = gq;
18. while (!g.empty())
19. {
20. cout << '\t' << g.front();
21. g.pop();
22. }
23. cout << '\n';
24. }
26. int main()
27. {
28. queue <int> gquiz;
29. gquiz.push(10);
30. gquiz.push(20);
32. cout << "The queue gquiz is : ";
33. showq(gquiz);
35. cout << "\ngquiz.size() : " << gquiz.size();
36. cout << "\ngquiz.front() : " << gquiz.front();
37. cout << "\ngquiz.back() : " << gquiz.back();
39. cout << "\ngquiz.pop() : ";
40. gquiz.pop();
41. showq(gquiz);
43. return 0;
44. }

```

---


`@bintou`
`2017-11-02 06:46:31`
`字数 1756`
`阅读 1686`


PseudoRandomness vs RH
======================

`未分类`

---

PseudoRandomness vs RH
----------------------

```


1. def rand_walk(n):
2. step = 0
3. for i in range(1, n):
4. #temp = randint(0,2)
5. temp = ZZ.random_element(0,3)
6. if temp == 2:
7. step += 1
8. elif temp == 1:
9. step -= 1
10. # Output the result.
11. print "Derivation from orgin", step
12. print "The expectation from the orgin is:", floor(sqrt(n))
14. #Define a rand_walk using RH
15. def rand_walk_rh(n):
16. step = 0
17. for i in range(1, n + 1):
18. fac = factor(i)
19. length = len(fac)
20. stay = false
21. for j in range(length):
22. if fac[j][1] > 1:
23. print i, "don't move"
24. stay = True
25. break
26. if not stay:
27. if is_odd(length):
28. step += 1
29. print i, "move right"
30. else:
31. step -=1
32. print i, "move left"
33. # Output the result.
34. print "Derivation from orgin", step
35. print "The expectation from the orgin is:", floor(sqrt(n))

```
### Python code

```


1. #https://www.quora.com/How-do-I-solve-the-drunkards-walk-or-random-walk-simulation-using-Python-language
2. import random
4. def RandomWalk1(n):
5. # n-length random walk on the number line
6. return [1 if random.random() > 0.5 else -1 for i in xrange(n)]
8. def RandomWalk2(n):
9. # n-length random walk on the number line
10. return [random.choice([-1, 1]) for i in xrange(n)]
12. def RandomWalkFinalPosition(n):
13. return sum(RandomWalk1(n))
15. import numpy as np
17. def RandomWalkNP(n):
18. return np.random.choice([-1, 1], n)
20. def RandomWalkGenerator1():
21. while True:
22. yield 1 if random.random() > 0.5 else -1
24. def RandomWalkGenerator2(n=float('inf')):
25. step = 0
26. while step < n:
27. step += 1
28. yield 1 if random.random() > 0.5 else -1
30. import random
32. def Step(n_dim):
33. move = [0 for i in xrange(n_dim)]
34. dimension_to_move = random.randint(0, n_dim-1)
35. direction = 1 if random.random() > 0.5 else -1
36. move[dimension_to_move] = direction
37. return move
39. def RandomWalkMulti(n_steps, n_dim):
40. return [Step(n_dim) for i in xrange(n_steps)]
42. #https://plot.ly/python/random-walk/
43. #http://mooc.ee/MTAT.03.236/2014_fall/uploads/Main/drunkard1.pdf
44. #https://stackoverflow.com/questions/9421928/another-simple-random-walk-simulation-using-pythontwo-dimensional
45. #https://stackoverflow.com/questions/26195815/python-drunkards-walk

```

---


`@bintou`
`2017-02-09 03:51:20`
`字数 1697`
`阅读 1762`


所谓”一代不如一代“
==========

`未分类`

---

在平常的生活中，一不小心就能听到某些老前辈在感叹，唉，人心不古，一代不如一代。听到这些话的时候自己又仿佛受到了启发，点头称是，嗯，确实一代不如一代。事实真的如此吗？稍微分析一下就知道，所谓“一代不如一代”也许只是一种假象，其实只不过是“一代不欣赏一代”罢了。

我记得有一次与一个外学院的老师聊天，不知如何就讲到本科生研究生的毕业论文之上，他就感叹说，唉，我们很多同事都有感觉，真的一代不如一代，一代难带过一代，现在的学生不知道怎么了，怎么这么差。我忙不迭地点头，是啊是啊，哎呦，我带的学生真实差得......然后大家得到共识之后都很放心地去做自己的事情了。事后我就想，现在的毕业论文差，比90年代、80年代的毕业论文如何呢？现在的学生有那么好的计算机、网络，获取的知识那么丰富，怎么会比那个年代的学生要差呢？暂且不说这些虚的比较，拿硬数据出来说吧。我记得我本科时候，毕业论文是不要求电子版的，大多数是手写。我的本科毕业论文就是手写的，绝对很烂。这丝毫不奇怪，大多数人其实没有电脑。我记得那时的优秀本科毕业设计是用Foxpro写个管理信息系统，可以这么说，现在用Dot.Net做的那套被大部分老师鄙视的管理系统比那时候的先进100倍。我还可以列举一大堆数字来例证现在的学生不比以前的差。

1、现在英语的4\6级通过率比以前高；   

2、现在的学生获得的比赛奖项比以前要高：现在有省级、国家级、国际级，而以前能有省级就非常了不起；   

3、现在同学发表文章的数量与质量比以前要高：以前能有个核心期刊了不起了，而现在什么SCI的都比较普通；   

4、 现在的师资力量、教学资源的丰富是前所未有的；

讲了这么多，那么是什么导致我们会认为“一代不如一代”呢？正如我上面说到的，感觉也许是对的，但是真相也许只是一代不欣赏一代。我不掩饰自己也说过类似“一代不如一代”这样的话，在分析了数据之后，我认为自己这样的感受很可能就源自于我不欣赏现在某些大学生的行为。但是，就“不欣赏 ”而言，实在得不出“不如”这样的结论。而且“不欣赏”往往又源自于个人的感受还停留在过去的年代，似有刻舟求剑之嫌。

比如说，我认为目前的大学生与我们相比有很大的心理劣势，他们往往容易自卑，然后在稍有进步的时候又容易自傲。考虑到，在90年代，SCNU计算机专业一年招生只有50人的规模，研究生一年只有2、3个人的招生规模，那时候的大学生真的是所谓的“天之骄子”，他们的心理优势岂是现在学生可比的呢？那个时候计算机本科毕业的学生就可以进高校做老师，而现在计算机本科毕业的师范生能做中学老师的都不多。社会发展、高校的变革都在迫使人们在改变心态调整心态，还拿过去的心理优势来衡量现在的学生，显然是不客观的标准。

又比如，最近学校闹了一些事情，学生们为争取可以在宿舍装空调搞了一些活动。很多老师会批评现在的学生娇生惯养，吃不得苦（插播一句，这个批评我似乎也常说）。这些批评也许并不错到那里，但是如果转换一下角色，站在学生的角度看，也许就是苛求了。社会进步了，生活水平提高了，大部分同学生活在比较舒适的家庭中，突然要适应一种酷热的环境确实很困难的。问题还在于，这种环境是不是不能改变？批评学生是容易的，转过身去我给自己孩子开了空调。乐观点看，我们可以说，学生们为了争取自己的合法权益使用了非常漂亮的手段与方法：严密的组织、合理的诉求、理性的行为，这就令我们这些老家伙也感觉到自愧不如。

“一代不欣赏一代”也许就是长期以来“一代不如一代”的真实本质。我很记得胡适在提倡白话文运动之后很多饱学之士为了中华文化之传承痛哭流涕上书直言甚至指着胡适的鼻子骂，但历史从来都没有倒退过一步，打住不表！由此可知，只要这个社会还在进步，只能是青出于蓝而胜于蓝，一代胜过一代，勿容置疑。只是在不同的历史时刻“一代不如一代”的慨叹恐怕依然会不绝于耳，为何？因为大部分的人缺乏足够的内省，很难随着时代的变化而调整心态做出响应并尽快更新自己的认识，在对事物进行判断不自觉地使用了“刻舟求剑”之法。

说了这么多......呵呵，分析归分析，以后你们还是难免会招我的白眼：一代不如一代！



---


`@bintou`
`2022-09-01 18:20:18`
`字数 20`
`阅读 4020`


后量子安全认证密钥交换协议的关键技术研究
====================



---


`@bintou`
`2022-11-07 00:40:57`
`字数 486`
`阅读 2993`


《计算机安全学》授课手记
------------

### 2022年9月1日的提醒

关于课程学习有几个提醒，首先，CANS里面的数论部分我应该不会再讲了，没有基础的同学自己先看。第二，古典密码我不详细讲算法，只讲一些概念，建立概念模型。第三，我们主讲的第一个算法是AES。希望大家可以尽快看到AES部分。AES的本质内容是需要用到GF(2^8)，这一部分大家都没有基础，要了解GF(2^8)，最基本的是要掌握群和域的概念，这个大家应该懂。我根据大家的理解进度来授课，有些讲不清楚的问题也许就要跳过。所以，大家看书也需要懂得如何跳，懂得如何先掌握大概的框架，而放掉一些细节。

本周的作业就是要阅读！

### 2022年9月推荐

本学期有AI方向的同学选课，特推荐以下与AI、隐私保护相关的资料供同学们参考。

* 综述：[Privacy Preserving Machine Learning](https://arxiv.org/pdf/1804.11238.pdf)
* 博客：[Privacy Preserving Machine Learning](https://www.microsoft.com/en-us/research/blog/privacy-preserving-machine-learning-maintaining-confidentiality-and-preserving-trust/)
* 博客：[Security and Privacy Issues in Deep Learning](https://arshren.medium.com/security-and-privacy-issues-in-deep-learning-cf7b593be4b7)

### 计算机安全相关的代码推荐

* [计算机安全相关的代码推荐](https://www.zybuluo.com/bintou/note/1697174)
* [Diffie-Hellman和ElGamal代码](https://paste.ubuntu.com/p/3S5gmF3q9P/)

---


`@bintou`
`2016-12-07 06:14:54`
`字数 1150`
`阅读 1877`


Binto对计算机学院08届本科生的毕业演讲
======================

`未分类`

---

今天首先要祝贺你们，我很荣幸地可以在这里告诉你们这番话，尽管我显得是如此的不够格：我还没有老到可以神秘兮兮地给你们走出校门走向社会的弥足珍贵的忠告。

是的，你们还会不断地听到各种不同的忠告，从你的父母到隔壁叔叔阿姨，还有你的新领导、新同事，甚至包括我们在座的几位老师。值得注意的是，这些发自肺腑的金玉良言也可能矛盾重重，让你手足无措。同一个字眼表达的忠告也可以包含不同的内涵与外延。我给你们的“忠告”就是，小心你什么的忠告，仔细思考你得到的忠告。你如何根据你得到的忠告建立自己的行为准则？坚持自己的理想还是妥协于现实？孩子们，在内心深处，没有任何人可以给你最实质的帮助，你们要依靠自己，依靠自己的智慧。

在这一刻，也许你们的心早已冲出了校园，无论这颗心是满怀希望还是失落不堪。在你们奔出校园之际，容我这样不敬地说，你们中的不少人是“逃离”校园。这种“逃兵”现象体现最为突出的是丢书、卖书。你可以卖掉你的棉被衣物，丢弃一两个饭盒调羹，但和不善待一下自己的战利品--书籍呢？那些书你都都看懂了？不需要了？如果你还没有学会爱惜书本，那你就还没有好好地上过大学，你是被大学上了而已。

离校之时，你望着熟悉的校园，大声慨叹：乌拉，不用再考试了！乌拉，不用再上课了！乌拉，见鬼去吧课室、宿舍、饭堂、图书馆。殊不知，这并非胜利者的宣言。大学与社会并不能靠毕业聚餐来截然分割，如果你急于走出校园奔向社会，是否意味着你一直校园生活就不是生活呢？多少次的梦想中，你是否曾经告诉自己，如果我工作了就如何如何，如果我毕业了就如何如何？在你如此憧憬未来的时候为什么你不会好好地享受当时的生活呢？

我禁不住要泼你们一盆冷水，你们“逃”不掉的，大学就是社会，社会就是大学，大学有多烂社会就有多烂，社会有多糟大学就同样有多糟！过去、现在与未来都是你的生活，活好你现在的每一刻吧。

年轻的小伙子、小姑娘们，稳重地踏出坚实的步伐走向你的未来吧，无论你们现在满怀希望还是失望重重。如果你满怀希望，认为世界光明美好，那小心现实会在你不经意的时候幽你一默；如果你非常失望，认为世界漆黑一片毫无前途，那你何不幽现实一默，从而发现更多的惊喜？世界可以是任何样子，但绝对不是你所想象的那样。记住，只有在某天，突然你发现原来世界并非如自己想象，而是充满了矛盾与荒谬，在那一刻你才真正地第一次与这个世界发生了联系，那一刻才是你的成人礼。

最后请允许我讲一个非常不适宜的小故事，加缪的《误会》（略）。我把剧中人的控诉换为这样的设问结束这次讲话：你该如何建立自己的和平与家园呢？

P.S. 吹牛不打稿，没有记录，时隔一周，难复原貌，且凌乱难堪，对不起对不起。大致按照三个关键词：智慧、逃跑、成熟来展开。

2008年6月27日



---


`@bintou`
`2016-12-07 05:44:30`
`字数 640`
`阅读 2574`


喜迎亚运，重树新风！小便入池，大便入坑！
====================

`未分类`

---

我一直错误地以为每一个网络ID的签名档都是一条欲盖弥彰的标语，我真的错了，其实，每一句欲盖弥彰的标语都是一个真实ID在现实世界的签名档。

年少无知时总觉得应该把那些愚蠢的签名档扔进厕所，我又错了，其实，应该把厕所里睿智的标语写入该死的签名档！厕所里的标语通常具有世人难以预见的睿智，如果你把它们当成易经来诠释，应当有无穷的解读。比如以下这条以人为本的标语：

小便入池，大便入坑！
----------

[此处输入链接的描述](http://fmn.rrimg.com/fmn046/20101109/2240/b_large_W1RZ_3c75000268205c40.jpg)

写这标语的人（错，写这签名档的人）冷静地利用了中文的省略法，将自己的控诉给了“小便”与“大便”，让它们入池落坑。尽管貌似冷静，可惜那个不争气的“！”明明白白地出卖了他，其实他愤怒了，或者他曾经愤怒过！他也许踩中了，或者至少被臭到了，或者被恶心了！但他并没有傻到控诉大小便，他厉声警告的是那些大小便的人。

错了！它冷静地潜伏在南方某著名高校的某个所，它孤寂地等待某个欣赏者的出现，等了好多年，等到纸张都枯黄了，难道它只关心那些屎尿？它真正的意义在于每天都睿智地警告一个个来去匆匆的高校学子教师，人应该本份，本份地待在他应该待的地方而不逾矩，否则将害人害己，遗臭万年（至少会臭一阵子）。

亚运就要到了，在这大好的日子里，我心情激动啊！这么好的标语应该还其本来面目，重见天日，在我们精神文明建设与物质文明建设中，在改革开放的新浪潮中发挥其重要的作用！本人不才，将这标语稍做改动，与大家伙共勉：喜迎亚运，重树新风！小便入池，大便入坑！

2010年11月9日



---


`@bintou`
`2017-09-14 04:39:35`
`字数 5846`
`阅读 2451`


太极拳学习笔记
=======

`未分类`

---

### 杨氏老谱秘传太极八法

掤劲义何解 如水负行舟 先实丹田气 次要顶头悬 全体弹簧力 开合一定间 任有千斤重 飘浮亦不难   

捋劲义何解 引导使之前 顺其来势力 轻灵不丢顶 力尽自然空 丢击任自然 重心自维持 莫为他人乘   

挤劲义何解 用时有两方 直接单纯意 迎合一动中 间接反应力 如球撞壁还 又如钱投鼓 跃然击铿锵   

按劲义何解 运用如水行 柔中寓刚强 急流势难当 遇高则膨满 逢洼向下潜 波浪有起伏 有孔无不入   

采劲义何解 如权之引衡 任尔力巨细 权后知轻重 转移只四两 千斤亦可平 若问理何在 杠杆之作用   

挒劲义何解 旋转若飞轮 投物于其上 脱然掷丈寻 君不见漩涡 卷浪若螺纹 落叶堕其上 倏尔便沉沦   

肘劲义何解 方法有五行 阴阳分上下 虚实须辨清 连环势莫当 开花捶更凶 六劲融通后 运用始无穷   

靠劲义何解 其法分肩背 斜飞势用肩 肩中还有背 一旦得机势 轰然如捣碓 仔细维重心 失中徒无功

### 含胸拔背的本质

太极拳的含胸拔背，其实是有一个变化范围的动态姿势，不是固定的、持续不变的，所以，它有一个最基本的姿势作为变化的起始基础，这个基础性的姿势就是自然状态的含胸拔背。综合有关文字资料中一些先辈的阐述，这种自然状态的含胸拔背就是维持最佳符合人体生理活动需要的自然放松的胸背部姿势，人在自然放松站立时，胸段脊柱具有微微后凸的生理弧度，与脊柱其他弧度一起担负着缓冲地面震荡从而保护中枢神经等重要的生理任务。背肌因而舒张，即自然站立状态的人就呈现着基本的拔背姿势；人体的解剖结构中，躯体两边侧中线的连线和颈侧中线至肩头外侧中点的连线有一个微向前的角度，即两肩头的方向是微向着前斜侧方的，或者说：两肩是呈现着微向前裹合的，因而人的锁骨下方呈现出一个三角形的凹窝，这就是说：自然站立状态的人就呈现着基本的含胸姿势，对于没有不良姿势习惯的人来说，会感到这种姿势的胸背部没有任何应力，实际上这时人体胸腔的容量最大，所以，这种自然放松形成的基本的含胸拔背无疑有利于人体健康，有利于人体全身的气血运行、气沉丹田和脚下沉稳。

### 杨澄甫太极拳说十要

杨澄甫宗师的太极拳“十要”说，一直是我们在练习拳架中要刻刻留意处处做到的具体要求，不可有差池。这“十要”说的内容是“虚灵顶劲、含胸拔背、松腰、分虚实、沉肩坠肘、用意不用力、上下相随、内外相合、相连不断、动中求静”

### 如何求得太极拳的大松大软

很多太极拳爱好者练拳数年，却毫无太极拳的味道，动作多以四肢的僵硬曲伸而毫无腰脊的盘带；一搭手非丢即顶，胡抓乱拔，毫无沾粘连随、松沉绵软之意。问其平日练功之法，全然不得而知，真使人痛惜。当听我讲解太极拳练功心法及练功要领后，他们才感到自己走了许多冤枉路，浪费了许多时光。   

　　如何练好太极拳呢？这要从太极拳的动作特点出发。要“一举动，周身俱要轻灵，龙须贯串，气意鼓荡，神宜内敛，无使有缺陷处，无使 有凸凹处，无使有断续处。其根在脚 ，发于腿，主宰于腰，行于手指。由脚而腿百腰，总须完整一气，向前奶后，乃能得机得势。”“凡此皆是意，不在外面，若加以挫劲，其根自断。”要想实现此要求，练要在稳静心性追求大松大软上下功夫。何为“大松大软”？就是自己的身心得到极度放松条件下周身四肢在心意的支配下做各种曲伸开合的支作，使 呼吸深长，支作运行如行云流水，如抽丝拉线。心存静想，外示安逸，虽动犹静，静中处动。我认为找松柔绵软要从以下几主面出发：   

　　一、要学会放松，即稳静主性，安舒松静。因为太极拳是行心用意，内外一体的拳术，往往人在静极默笃之后，灵慧方能始现。但澄定之工夫须在稳葛上云着手，所以我们打拳时须先将身势立稳，重主放正，身心松开，全身不有丝毫拘滞之力，杂念摒除，使 体态归于自然而后出动。动时以心气行运以腰脊领带，静静地将一趟太极拳形容出来。为何说把拳形容 出来呢？因为太极拳中每个拳式的内容都是象形象意富含哲理而又抽象的。只有对每个动作进行象形象意的描述，才能把它尽可以圆满地形容出来或表达出来。所谓“一静无有不静，一动无有不动。动静一源，往复无迹，圆融无碍”，此为太极拳运动之根本。静可以保持大脑神经的清醒、灵敏，培养人的聪明智慧。由此入手，在稳静安舒的练拳中慢慢领司太极拳神明高深的境界，得到灵敏 的感应。   

　　二、身法姿势要正确。拳架要立身中正，虚灵顶劲，松腰塌胯。每着每式要使 “力起于脚，发于腿，主宰于腰，形于手指，由脚 而腿而腰，完整一气，向前退后皆然，若有不得机得势，身便 散乱，其病必于腰腿求之”。所以腰是周身上下相通枢纽，即“命意源头在腰隙”。①立身中正，可保持头容正直，利于虚灵顶劲，转换 灵活，利于气意下沉，稳定下盘重心。②松肩 垂肘，利于气意通达四塞纳河，劲意畅通。若残久两臂就会产生一种内在的沉劲，此劲绵软沉重。这种沉劲外柔内刚，如棉裹铁，入里透内，威力无穷。③气沉丹田，是指练拳时，用意识引导呼吸，将气用意沉下丹田。练习太极拳有素的人，多是采用腹式呼吸，呼吸均匀绵长。初学者切不可着急追求其效果，否则会弄得神形散乱。保持呼吸自然，久之能自然配合动作。④含胸拔背，含胸者，胸略内含，使其松开，以便于气意沉于丹田。挺胸则气塞，上重下轻，脚下无根；含胸则背自拔，使脊背个长，气贴于背。⑤下面再谈谈在练拳时对步法的要求，太极拳的步法要点就是分虚实，全身重心在两脚之间的转换，即上小时，腰收　敛，精神虚虚上领，使 后脚 跟像从被陷入深泥中被 拔出，使后脚缓缓收至前脚侧，随即由身势向下松开将放虎之脚 再缓 缓 迈出，身势随迈出之腿而前送。这就如同载重之船行使在江河之上，起不离水的浮力，沉又不能到水底一样，随着水流碧波荡漾。但太极拳在动时一定要本着心为令，气 旗，腰为轴，四肢跟之随之。总而言之，练太极拳身法要不偏 不倚，步法手法要无过不及，这才是求得习练太极拳正确功架的基本方法。   

　　三、用意不用力。现在有许多人理解不了这句话，认为不用力何能对敌，实不知太极拳的力不是靠肌肉收缩所产生的硬力或拙力。而是慢中求功，通过练体固精，练精化气，练气化神，练神还虚所得到的松弹绵软而又厚重的劲，此劲如棉裹铁，打到对方身上，入里透内。练太极拳时轻松自然，用意不用力，以养虚灵之气势，神明之感庆。拳以所云“意气骨肉臣”，心是身之主，身是心之用，时时刻刻在练拳中寻找体态之舒，身心之合，气贯十指，上下相随，内外一体的感觉。人有经络，如地之沟壑，沟通不塞而水行，经络不闭而气通。如混入僵劲，充满经络，气血停滞，转动则不灵。若不用力而用意，意之所至，气即至焉，气血通畅，周流全身，无时停滞，入则得真正内劲，即太极认中所云“极柔软，然后能极坚刚”也。   

　　四、要反复操练和细心揣摩。当所学着式和要领弄明白后，要反复操练，用心揣摩每个动作的内在含义和韵味，以求得周身各节的配合恰当自如。动作的舒展大方而无拘禁，身心的协调而不散乱，使 其整套动作以意识的牵引而连绵不断。式如行云流水，抽丝挂线，迈步如猫行。要先在心，后在身，腹松静，气敛入骨，神舒体静，刻刻在心，功记一动无有不动，一静无有不静，牵动往来气贴背，内固神，外示安逸，全身意在精神而不在气，在气则滞，有者无力，无气者纯刚，气若车轮，腰如车轴，如能本着以上道理认真追求，必定会成功。十三式势歌诀中云“仔细留心向推求，屈身开合任自由，入门引路需口授，功夫不息法自修”，师傅领进门，修行在个人。

### 太极拳如何练习腰

太极拳以其独特的魅力，吸引无数爱好者为之不断探索。现在，我们不必去看它外在的复杂轨迹，而是直接进入它的核心——腰隙命门处。

腰胯相连处，是人体重心所在，是人体平衡的关键之处。人体重心在运动中只要不超过带脉一圈临界范围，人体就能保持本身的动态平衡。在对抗中的借力平衡是指受力运动中，自身超出了带脉一圈处于不稳定状态时，通过借对方一点点摩擦力而自身中线回到带脉一圈范围内，就如站在开动的公共汽车中稍稍扶一下稳固物自身就保持了平衡一样。

腰隙与丹田如何统一呢?腰隙与丹田处于同一水平面，腰隙靠后，是先天气之本；丹田靠前，是后天气之本，统一的方法是腰隙为开，丹田为合。同时，随着脚下的前踩后蹬，腰胯瞬间拉开的一摇一抖，丹田如气球般一合一压一放，弹性十足，即可整体爆发。发劲时，劲则从脚下传来，经过各个关节的传递，一下子就从手上轻松发出，通体舒畅。下面介绍具体方法如下：

一、腰轴正骨

腰胯的训练应围绕脊椎的横开入手，脊椎中心在腰椎，而腰椎生理弯曲不利于其作为主轴的轴承功能，试想围绕弯曲轴承旋转肯定是晃荡的。所以让腰椎正骨竖立就成了拳家研究的重要课题。

腰轴正骨的特点

1．能带动肩胯的顺利旋转。旋转才能增加身体的稳定性，如陀螺下面的锥尖根本不能稳定重心，但一抽陀螺，旋转就平稳了。

2．能让身体绕轴旋转，成八面支撑之势。单单是周身僵态掤架，是不能八面支撑的。

3．可使肌肉松松地附在骨骼上，利于毛细血管的流通。如此，通过旋转离心力把心脏血液顺利甩向四梢，减轻了心脏的压力，这是最好的养生运动。

4．能使其形圆，形圆则气顺。

5．腰轴正后，化劲时，肩胯散开绕轴回旋；发劲时，肩胯聚合绕轴螺旋。可前后左右移动重心，作自主性平衡的调节。同时配合含胸拔背，身弓撑起，能使我们气沉丹田，下重上轻，势如不倒翁。

训练方法

腰椎正骨的好方法应是塌腰突肾，即让腰椎后搠以填平腰椎生理弯曲。在桩功的训练中，就有以塌腰突’肾为中心作六面膨胀的呼吸，即“腰骨呼吸一气泓”。

正确的腰椎正直要领应是后背、后臀、后脚跟贴墙站桩，作腰椎正骨的六面呼吸。在此状态下，腰椎则会达到正骨为轴的要求。

另外，“虚坐高凳法”也是调节腰椎生理弯曲的好方法。具体方法：坐在一略低于自己臀部的高凳上，似坐非坐，不要坐实，体重均匀放在两脚与臀部三点之间。此时就是处于松胯、塌腰、提小腹的状态，用手摸后腰处的弯曲是填平的。塌腰与松胯是配合着同时做到的。

腰椎塌腰正骨后，接下来就是对开腰的训练。方法是通过“横开竖合”来达到开腰的目的。

二、开腰训练

这里特别提到的是横开双腰肌是最为重要的，也是最为困难的一部分工作，人体体重下传与反向支撑力都集中在腰部，所以形成了人体腰椎的生理弯曲，这个生理弯曲是由于人体长期直立行走而形成的，但太极内劲的上下传导，在此处就由于这个生理弯曲而使内动的上下通路断掉了，所以太极拳提出了塌腰、突肾的要领，即让腰椎拉开后拥、双。肾抽换突出，以此连通内劲上下传导，可以说塌腰、突肾是太极拳的一个核心秘密，但真正要做到塌腰突肾，就必须要有横开双腰肌的基本功架，否则双腰肌与腰椎长期堆积在一块的稳固生理结构，将阻碍拳功的进一步深入。

具体步骤

1．收腮拔顶。凸鼓后颈两筋之间哑门穴，此是副交感神经之处。后脑两筋腾起，以颅颈部骨骼肌的左右、上下、前后的对立平衡，来带动横膈与纵膈的对立平衡。

2．裹肘开肩。凸鼓腋下两窝，肘部劲向下、向侧、向前如盘中滚珠，以此带动脊椎两旁肌的横拉纵隔(横开)，引起横隔下降(竖合)。

3．扭根抽胯。陈式大架凸鼓两膝窝、两腰窝。两腰之间为命门，是交感神经之处。两脚后跟对称向两侧旋辗，以此拉开双肾腰肌。引起以腰椎命门为重心的收放如“∞”循环的背丝扣开合，带动周身收放的“∞”循环的横开竖合。

此法要求双后脚跟横开，由下至上、由内至外，进行开胯、开腰、开肩的运动，拉开脚踝关节韧带肌腱，拉开胯关节问的空间，拉开双腰肌腱，拉开肩关节的空间而使锁骨平展而放。功深时，脊椎两边的肌腱鼓起，脊椎骨凸出在两边肌腱之外。

开腰是比开胯更深入的功法，也是更困难的运动，但又是最重要的要领之一，学者不可忽视之。通过横开脊椎两边肌腱，不仅锻炼了脊椎两边肌腱，而且把脊椎内在空间拉大，更有利于内在脊髓的神经传导功能，而脊髓的植物神经分为交感神经(属阳，兴奋的功能)与副交感神经(属阴，抑制的功能)，是参与本能运动反应的神经系统。即运动反应直接由脊髓神经反馈而不通过大脑的思考，武术运动中一通过大脑思考后的反应就慢了一大拍，是视反应速度为生命的拳家之大忌。

处方1. **复元活血汤**：柴胡10 当归10 天花粉10 桃仁10 红花6 炮山甲6 酒大黄6（后下） 甘草3 （按：药后阿拉伯数字，计量单位为“克”。）方中柴胡疏肝理气，当归养血活血；辅以山甲破瘀通络，桃仁、红花活血祛瘀；酒大黄祛除瘀血，排除郁熟，增强活血祛瘀作用；天花粉清热消肿；甘草缓急止痛，调和诸药；数药合用，使瘀祛新生，气畅血行，瘀肿自愈。主治各种跌打外伤，瘀血肿痛，特别是胸肋胁疼痛，症见外伤后，瘀血留于胁下，痛不可忍或见局部红紫肿。本方用时加黄酒一匙，水煎早晚两次分服。是方笔者常用于各种外伤的血瘀肿痛，尤其是软组织扭挫伤所致的积瘀疼痛等症。方中行气药较少，可酌加川芎、郁金、乳香、没药、土鳖虫等行气活血，使气行血活，增加疗效；用于肋间神经痛、肋软骨炎属于瘀血停滞者；用于因外伤引起的腕、踝关节软组织血肿，伤在上肢加桂枝、桑枝，伤在下肢加牛膝、木瓜，效佳。

处方2. **芍甘汤**：白芍12 炙甘草12 （按：药后阿拉伯数字，计量单位为“克”。） 方中芍药酸苦，甘草甘平，酸甘化阴养血益阴，缓急止痛。主治营阴不足，肝脾不和，症见手足拘挛，筋脉挛缩，脘腹疼痛。本方水煎早晚两次分服。是方笔者多用于腓肠肌痉挛、颈项病、关节病、伤筋流注以及椎间盘突出、骨质增生等。本方适应症多有大筋软短、挛缩和腹肌拘急现象，无不与肝有关，肝主筋，芍甘二药有舒筋解痉功效；本方古称“去杖汤”，治脚弱无力，笔者经验：芍、甘二药用量大于常量，二药比例3比1或4比1，效更佳。

语录
--

杨澄甫《太极拳体用全书》的序里面有一段杨露禅的话，大家怎么看？   

“居，吾语汝。吾之习此而教人者，非以敌人，乃以卫身；非以用世，乃以救国。今之君子，祗知国之弊在贫，而未知国之病在弱也。是故谋国是者，竞筹救贫之策，未闻有振衰起颓之图。惟其通国皆病夫。谁复胜此重任？积弱斯贫，贫实原于弱也。考各国之致强，莫不强民为初步。欧美之雄伟英挺无论矣。即岛国侏儒，亦孰非短小而精悍。以吾国人之鸠形鹄面当之，胜负之决，庸待蓍龟。然则救国之道，自当以救弱为急务。舍此不图，抑亦末矣。余自幼即以救弱为己任。尝见买解者，其精神体魄，固不逊于外人所谓大力士武士道者。余大喜，叩其术，秘不以告。乃知中国自有强身之术，而一弱至此，岂无故哉！嗣闻豫中陈家沟陈氏有内家拳之名，蹑跷往从陈师长兴学。虽不见拒于门强之外，然日居月诸，迄未许窥堂奥。忍心耐守，凡十余稔，师悯余诚，始于月明人静时，举个中妙谛以授予。学成来京师，誓本素志，广授于人。未几，见从吾学者，瘠者肥，羸者腴，而病者健。乃大喜。顾以一人之所授有限，则如愚公之移山，更以诸若父叔辈暨从游者。若志在用世，宁鄙视救世之术而不学乎？”



---

