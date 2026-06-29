---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Mathematical Physics

:::{figure} _static/site_logo.png
:::

:::{note} What is this? 
This is a student's notebook on the topic of **Mathematical Physics** with a mix of **Numerical methods for ODE/PDE**. The primarily purpose of writing this is:
1. If you are taking mathematical physics like me you might find some exercises I collected here useful; I also documented some of my confusion about the subject(though might appear trivial to you) here that you might have encountered as well. 
2. In classes like **Numerical Analysis**, **Numerical Methods for PDEs**, dispite a lot of the problems arise from physical sciences, the physical background is often left untouched. Even worse, the analytical method for model problems is also rarely talked about due to limited class time. Although the analytical and numerical methods on the same problem is likely orthogonal, I believe there is some virtue in learning analytical techniques. The main reason being analytical techniques unravel core strucutre of the problem which might be utillised to speed up numerical algorithms in good hands.
:::



## Feature
:::{tip} Numerical Methods 
My interest primarily lies among numerical methods and numerical climate modeling, hence the emphasis of this notebook is going to be on traditional mathematical physics with a detailed discussion on numerical algorithms whenever appropriate. In particular, the PDE chapter is organized into specific problems each treated with an equal empahsis on corresponding numerical and analytical methods.
:::

:::{tip} Executable Code Cells 
This note book includes code cells that is runnable in real-time. This provides more interactive visualization, as well as better reading 
exprience since readers doesn't need to copy code snippet and run in their own kernel. To run the code, always click the power buttom when 
onto a page in this notebook. The underlying binder service would spwan a docker container which takes a minute or so. After the container is 
up and running, one would see every code cell turning into an executable cell. 

```{code-cell}
    print("This is an online mathematical physics note with executable python code!")
```
Sometimes other standard compiled coding language such as julia and c++ would be used, please run these locally.
:::


## Disclaimer
:::{attention} AI-free Creation
I'm a believer of the idea that AI brings huge cognitive debt and cumbers the learning process. This notebook is hence created AI free(however, conceptual consulting is quite frequent, they are truely valuable resource too when it comes to learning, contradictoraily). Code snippet is generally AI-free. That being said, **claude-code** is extensively used to debug and for brainstorming new ideas.
:::


:::{error} Error and Mistakes Everywhere!
This is just a lecture note by a student who is a total beginer in physics, and not too much better in Mathematics and CS(A lot to learn!). Also as a second-language speaker in English[^mt], typos and mistakes in spelling is somewhat unavoidable.

Therefore mistakes should be expected among every rendered equation/sentence. I would greatly appreciate reporting mistakes via github or my email hytang2@illinois.edu.
:::



[^mt]: My mother tongue is Wu Chinese(ISO639-3 : wuu)(枫桥话-吴语临绍小片) and Madarin(普通话)
