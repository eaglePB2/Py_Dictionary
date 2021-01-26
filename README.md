## Python Dictionary

“用于解码档案使用，一次性，需要自己改一下里面的代码。”

平常在考古一些网站的时候，里面的js有时候因为作者的一些需求（或者js的个性）还有莫名其妙的扰乱造成其他人无法好好的读代码的关系，于是就做了这套python系统一键翻译 至少让里面的代码好读一点。

这次使用的例子是采用了Eric Gurt的Plazma Burst 2 Level Editor 的javascript档，其中就有一些行列：

    var lil='O0', lIl='2d',lll='right_panel',...

把那整套系统丢进dictionary档，然后用notepad++移除","和开关引号，并且把里面的一些“=”也替换掉或者让切割标准换成另一种符号也行（例如“|”，我觉得没什么人会用到这个符号），例子如下：

    var lil|O0, lIl|2d,lll|right_panel,...
然后把整个代码丢进去，再用py档跑了一下 然后就大功告成了~
