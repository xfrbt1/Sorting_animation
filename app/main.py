from animation.animation import SortingAnimation
from config import mix, ARRAY_TEST

if __name__ == "__main__":
    mix()
    animation = SortingAnimation(ARRAY_TEST, 1)
    animation.run()

    mix()
    animation = SortingAnimation(ARRAY_TEST, 2)
    animation.run()

    mix()
    animation = SortingAnimation(ARRAY_TEST, 3)
    animation.run()
