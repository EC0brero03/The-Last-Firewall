init -1 python:
    import pygame

    class STD_Item(renpy.Displayable):
        def __init__(self, myimage, x, y, w, h, **kwargs):
            super(STD_Item, self).__init__(**kwargs)
            self.myimage = Transform(renpy.displayable(myimage), crop=(x, y, w, h))
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.left = False
            self.right = False

        def visit(self):
            return [self.myimage]

    class SpotTheDifference(renpy.Displayable):
        def __init__(self, child, diff_items, scale=1.0, **kwargs):
            super(SpotTheDifference, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.diff_items = diff_items
            self.scale = scale
            self.width = 0
            self.height = 0
            self.x_offset = 0
            self.y_offset = 0

        def render(self, width, height, st, at):
            scaled_child = Transform(self.child, zoom=self.scale)
            child_render = renpy.render(scaled_child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            
            self.x_offset = (width / 2) - self.width
            self.y_offset = (height / 2) - (self.height / 2)

            render = renpy.Render(width, height)
            render.blit(child_render, (self.x_offset, self.y_offset))
            render.blit(child_render, (self.width + self.x_offset, self.y_offset))

            for i in self.diff_items:
                scaled_item = Transform(i.myimage, zoom=self.scale)
                diff_render = renpy.render(scaled_item, width, height, st, at)
                if i.left:
                    render.blit(diff_render, (i.x * self.scale + self.x_offset, i.y * self.scale + self.y_offset))
                if i.right:
                    render.blit(diff_render, (i.x * self.scale + self.width + self.x_offset, i.y * self.scale + self.y_offset))

            score = self.count_differences()
            score_txt = Text("Differences left: %d" % score, size=24)
            score_img = renpy.render(score_txt, width, height, st, at)
            render.blit(score_img, (width/2 - 100, self.height + self.y_offset + 10))
            return render

        def count_differences(self):
            return sum(1 for i in self.diff_items if i.left != i.right)

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                for i in self.diff_items:
                    ix, iy = i.x * self.scale, i.y * self.scale
                    iw, ih = i.w * self.scale, i.h * self.scale

                    if (self.x_offset + ix <= x <= self.x_offset + ix + iw) and \
                        (self.y_offset + iy <= y <= self.y_offset + iy + ih):
                        if i.left != i.right:
                            i.left = i.right
                            renpy.redraw(self, 0)
                    elif (self.width + self.x_offset + ix <= x <= self.width + self.x_offset + ix + iw) and \
                        (self.y_offset + iy <= y <= self.y_offset + iy + ih):
                        if i.right != i.left:
                            i.right = i.left
                            renpy.redraw(self, 0)

                if self.count_differences() == 0:
                    return "win"

        def visit(self):
            return [self.child] + [i.myimage for i in self.diff_items]

        def randomizeItems(self, difference_count):
            for i in self.diff_items:
                state = renpy.random.choice([True, False])
                i.left = i.right = state
            random_pool = list(self.diff_items)
            renpy.random.shuffle(random_pool)
            count = 0
            for i in random_pool:
                if count < difference_count:
                    i.left, i.right = True, False
                    count += 1

    class afterImage(renpy.Displayable):
        def __init__(self, child, diff_items, scale=1.0, **kwargs):
            super(afterImage, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.diff_items = diff_items
            self.scale = scale

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)
            render = renpy.Render(*child_render.get_size())
            render.blit(child_render, (0, 0))
            for i in self.diff_items:
                if i.left:
                    scaled_item = Transform(i.myimage, zoom=self.scale)
                    diff_render = renpy.render(scaled_item, width, height, st, at)
                    render.blit(diff_render, (i.x * self.scale, i.y * self.scale))
            return render

        def visit(self):
            return [self.child] + [i.myimage for i in self.diff_items]