from software_renderer import Software_Renderer
import timeit
import cProfile

def q1():
    # sweeping
    print(
        timeit.timeit(
            """GL = Software_Renderer('render.bmp')\nGL.glInit()\nGL.glCreateWindow(1920, 1080)\nGL.glViewPort(0, 0, 1920, 1080)\nGL.glClear()\nGL.glColor(1, 1, 1)\nGL.glLoadObj('deer.obj', (2000, 1200, 0), (0.5, 0.5, 0.5), 0.8, False)\nGL.glFinish()""",
            number=1,
            setup="from software_renderer import Software_Renderer"
        )
    )

    # barycentric
    print(
        timeit.timeit(
            """GL = Software_Renderer('render.bmp')\nGL.glInit()\nGL.glCreateWindow(1920, 1080)\nGL.glViewPort(0, 0, 1920, 1080)\nGL.glClear()\nGL.glColor(1, 1, 1)\nGL.glLoadObj('deer.obj', (2000, 1200, 0), (0.5, 0.5, 0.5), 0.8, True)\nGL.glFinish()""",
            number=1,
            setup="from software_renderer import Software_Renderer"
        )
    )

def q5_profile():
    GL = Software_Renderer('render.bmp')
    GL.glInit()
    GL.glCreateWindow(1920, 1080)
    GL.glViewPort(0, 0, 1920, 1080)
    GL.glClear()
    GL.glColor(1, 1, 1)
    GL.glLoadObj('deer.obj', (2000, 1200, 0), (0.5, 0.5, 0.5), 0.8, False)
    GL.glFinish()

def q6_profile():
    GL = Software_Renderer('render.bmp')
    GL.glInit()
    GL.glCreateWindow(1920, 1080)
    GL.glViewPort(0, 0, 1920, 1080)
    GL.glClear()
    GL.glColor(1, 1, 1)
    GL.glLoadObj('deer.obj', (2000, 1200, 0), (0.5, 0.5, 0.5), 0.8, True)
    GL.glFinish()

def q5():
    print('profiling q5')
    cProfile.run("q5_profile()")

def q6():
    print('profiling q6')
    cProfile.run("q6_profile()")

# uncomment/comment any of these to run each
# 'q' stands for 'question' in the question list provided.

q1()
q5()
q6()

