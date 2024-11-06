Title: Soft Robotics:
Date: 2020-06-11 08:00
Modified: 2020-06-25 10:50
Category: Chinese
<!--Password: jiefeng-->

# Soft Robotics: 灵活的微型机械手臂，人工肌肉驱动的仿生软体机械手臂实现新突破！

- 本文由机器人大讲堂微信公众号进行了推送。： https://mp.weixin.qq.com/s/-sP5DRDOUrZwOG5OaDQC6w

### 导读：
<figure>
<img src="{static}/images/movie.gif" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>

以前很长的一段时间里，机器人领域的研究大多集中在工业机器人上，人们往往追求更加精确可控的重复运动，而不太在意机器人的灵活性和体积。这就导致那些在科幻电影里边能够随意变换形状的灵活的机械臂和微型机器人，迄今为止也都仅仅停留在正在研发的就基础阶段。想要让机器人工作，那就需要一个可以产生力的驱动器。这种驱动器，类似人或者动物的肌肉，可以输出可控的力和位移。同时这个驱动器应该是柔软的，并且能够像肌肉一样可以变形。这种驱动器，我们称之为“柔性驱动器”， 也称人工肌肉或仿生肌肉，它能在外界刺激（如，电流、热、化学、磁场等）的作用下产生收缩，从而模拟动物肌肉的驱动特性。螺旋卷绕驱动器（Twisted-and-Coiled Actuator）是一种将聚合物纤维(例如，缝纫线，鱼线 等尼龙材料)扭转后螺旋卷绕而制成的新型人工肌肉，由于其形状是螺旋形而得名，我们以下简称“螺旋驱动器”。螺旋驱动器能量密度高，同等质量下输出的力是动物肌肉的一百倍，且成本低，。现在的螺旋驱动器一般用导电的尼龙缝纫线制作，如动画所示，可以直接在加电流之后（1A左右）收缩并提升一个重物， 或者伸长顶起一个物体。

<figure>
<img src="{static}/images/s2_shorter.gif" style="float:left; width:150px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>

<!-- <figure>
 <img src="{static}/images/scheme_TCA_soft.png" style="float:left; width:150px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;"> 
</figure> -->

近日，发表在国际著名机器人期刊《软体机器人》（Soft Robotics）的一篇论文，提出了将这种人工肌肉进行改进，从而驱动软体机器人,实现各种形式的灵活运动， 如弯曲，扭转等。研究者用这种人工肌肉驱动具有不同变形功能的模块：一个微小的软体夹爪，一个扭转的机械手腕，和一个可以向任何方向灵活弯曲的机械臂。将这些模块组合在一起，形成了一个厘米级的软体机械臂，这个机械臂可以灵活抓取将物体，并且将其准确地放置到预定的位置。文中所描述的软体机器人将在电子器件，精密仪器组装，食品，药品等方面有广泛的应用。 当然，由于这个螺旋驱动器是柔软的，所以可以被放置成各种形状，从而实现各种各样的运动。

### 螺旋驱动器的工作原理
<figure>
<img src="{static}/images/1_demo_1.gif" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:1em; padding-left:0.1px;">
</figure>

我们通过一个例子解释螺旋驱动器的工作原理。当我们用双手捏住一根鱼线（尼龙线）两端拉直并捻动它，就会看到这个鱼线的纤维成为了螺旋状。但是如果松开一端，鱼线就自然向反方向扭转恢复到原来的形状。所以我们需要施加一定的扭矩，防止鱼线扭转。当我们加热这个鱼线的时候，由于鱼线截面的变大，它内部的纤维为了保持原来的长度，就会向反方向扭转，从而产生更大的力去克服人手施加的扭矩。一个更直观的理解是，如果我们在一个圆柱体上缠绕一根不可伸长的线，并把这个线的两段固定在这个圆柱体上，如果这个圆柱体的直径增大了，这时候这个线必须要对这个圆柱体造成一个扭转去保持它原来的长度。

当把这个扭转（捻）过的鱼线缠绕在一个柱体上成为螺旋状，这个加热带来的扭转的形变就会变成线性的收缩或者是伸长。当然，我们也可以用更简单的方法，就是在刚开始捻的时候，就一直捻下去，直到这个鱼线自己形成螺旋状。但是这种方法就只能制作收缩型人工肌肉。动画中一位研究人员展示了这种制作方法，他在一根鱼线的底端挂了一个重物，然后用电机持续扭转鱼线，直到它完全成为螺旋状，然后用一个细杆防止底端反转。当他用热风吹这个人工肌肉的时候，我们可以明显看到重物被提升了，当其冷却之后，重物又恢复到了原来的位置。


### 螺旋驱动器的改进
<figure>
<img src="{static}/images/s1_shorter.gif" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>

以往的螺旋驱动器有一个致命的缺点：它在自然状态下是处于收缩状态 （圈与圈之间紧密相连）， 往往需要一个预拉力，将圈与圈之间拉开距离后，才能在驱动后进行收缩。这种预拉力的需求，使得这种驱动器很难被运用到柔软的软体机器人。 因为这个预应力会直接导致软体机器人有一个初始形变，而这种形变往往是不需要的。

研究人员通过改进制作方法，使得这种驱动器具有了自由行程。也就是，在自然状态下，不需要任何预拉力，螺旋驱动器的圈与圈之间都有间隙存在，因此螺旋驱动器在受热之后都能进行收缩，并在温度降低之后恢复到原来的状态。这种改进可以使得人工肌肉得到更加广泛应用，比如说，它能够克服被动力，例如摩擦力，去拉动一个物体。而在改进以前，这种人工肌肉只能够克服主动力，如重力。这种改进的最大的优点就是使得人工肌肉能够被运用到软体机器人上。同时，由于这种人工肌肉本身就是柔软的，和软体机器人有很好的兼容性。


### 运动可编程软体模块
<figure>
<img src="{static}/images/s3_shorter.gif" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>

<figure>
<img src="{static}/images/s4_shorter.gif" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>

<figure>
<img src="{static}/images/s5_shorter.gif" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>
由于这种人工肌肉本身的柔韧性，它可以被安置在一个柔软的软体（硅胶）内，并且可以是任意的形状：比如圆弧状，螺旋状，直线状等等。取决于这些不同的形状，当螺旋驱动器被驱动的时候，就会驱动这个软体，因此实现不同的运动 （变形）。如动画所示，当螺旋驱动器是一个弧状的U形的时候就可以驱动软体实现平面的弯曲，由此驱动一个常闭的夹爪。当是螺旋形的时候，就可以产生转动，驱动一个扭转的模块（像机械臂的手腕）。当是三个平行线的时候，驱动其中任意一个螺旋驱动器是就可以使得这个柱体弯曲（类似大臂），也可以通过控制其中任意两个人工肌肉输出力的比例从而控制其弯曲的方向。 总之，理论上我们可以实现任意的运动，对于简单形式的运动，我们能够直观感觉，人工肌肉应该被安置成一个什么样的形状，但是对于复杂的运动，就需要通过建立数学模型，去预测这些人工肌肉应该被放置成什么样的形状。 


### 人工肌肉驱动的微型机械臂

<figure>
<img src="{static}/images/scheme_TCA_soft.png" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>
<figure>
<img src="{static}/images/s6_shorter.gif" style="float:left; width:300px; padding-top:1em; padding-right:1.5em; padding-bottom:20px; padding-left:0px;">
</figure>
更加复杂的运动可以通过将简单的模块组合在一起来实现。 例如，我们把上文介绍的三种模块组合在一起，就可以组装成一个软体机械臂。动画中显示了这个软体机械臂的一个应用场景：一个机械臂可以转动自己的手腕，使得夹爪和要夹的面平行，然后夹爪打开，抓住物体，随后整个机械臂升高到一定的高度，最后大臂转动将物体放入到指定的容器中。

### 自感知功能

同时，类似于动物的肌肉，这种人工肌肉同时具有自感知的功能。当我们用传统的驱动器，如电机，去驱动机器人的时候，往往需要很多的传感器去检测运动，实现运动的控制。人工肌肉的这种自感知功能为其运动控制提供了很好的基础，使得我们能够在不借助外部传感器的情况下，控制它的运动。接下来的一个动画，展示了由这种自感知功能的螺旋驱动器驱动的软体手指，当人用手触摸这个软体手指两次的时候，这个手指感受到了外界的刺激，从而按照预定的程序弯曲60°并保持这个形状一定的时间。如果这个软体手指仅仅被触摸一次，则不做出任何反应。



### 完整视频
<iframe width="560" height="315" src="https://www.youtube.com/embed/M3MFRgYEnIk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

##### 作者信息


论文由科罗拉多州立大学（CSU）的赵建国教授团队完成，第一作者是CSU的博士生孙杰锋（[Jiefeng Sun](https://jiefengsun.github.io)），合作者有CSU的 Brandon Tighe，和哈工大的刘英想教授。

##### 相关论文：

- Sun, J., Tighe, B., Liu, Y., & Zhao, J. (2020). Twisted-and-Coiled Actuators with Free Strokes Enable Soft Robots with Programmable Motions. Soft Robotics.
- Sun J, Tighe B, & Zhao J (2020). Integrated Actuation and Self-Sensing for Twisted-and-Coiled Actuators with Applications to Innervated Soft Robots. In 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). Accepted. 
- Sun, J., Pawlowski, B., & Zhao, J. (2018). Embedded and controllable shape morphing with twisted-and-coiled actuators. In 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 5912-5917). IEEE.



