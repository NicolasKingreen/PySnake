from random import randint
import pygame


UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)


class SnakeSegment:

    def __init__(self, cell_position):
        self.set_pos(cell_position)

    def __repr__(self):
        return f"{self.cell_position}"

    def set_pos(self, cell_pos):
        self.cell_position = self.cell_x, self.cell_y = cell_pos

    def move(self, move_vector):
        new_x = self.cell_x + move_vector[0]
        new_y = self.cell_y + move_vector[1]
        self.set_pos((new_x, new_y))
        
class Snake:

    STARTING_LENGTH = 3

    def __init__(self, head_cell_position):
        self.color = (122, 158, 126)
        self.head_color = (49, 73, 60)
        self.last_color = (179, 239, 178)
        self.segments = []
        head_cell_x, head_cell_y = head_cell_position
        for segment_n in range(Snake.STARTING_LENGTH):
            new_segment_cell_position = head_cell_x - segment_n, head_cell_y
            self.add_segment(new_segment_cell_position)
        self.head = self.segments[0]

        self.move_direction = RIGHT

    def add_segment(self, cell_position):
        new_segment = SnakeSegment(cell_position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].cell_position)

    def set_move_direction_up(self):
        if self.move_direction != DOWN:
            self.move_direction = UP

    def set_move_direction_down(self):
        if self.move_direction != UP:
            self.move_direction = DOWN

    def set_move_direction_right(self):
        if self.move_direction != LEFT:
            self.move_direction = RIGHT

    def set_move_direction_left(self):
        if self.move_direction != RIGHT:
            self.move_direction = LEFT

    def update(self):
        for segment_n in range(len(self.segments)-1, 0, -1):
            self.segments[segment_n].set_pos(self.segments[segment_n-1].cell_position)
        self.head.move(self.move_direction)

    def draw(self, screen, cell_width):
        for segment in self.segments:
            if segment is self.head:
                color = self.head_color
            elif segment is self.segments[-1]:
                color = self.last_color
            else:
                color = self.color
            segment_draw_x = segment.cell_x * cell_width
            segment_draw_y = segment.cell_y * cell_width
            pygame.draw.rect(screen, color, (segment_draw_x, segment_draw_y, 
                int(cell_width * 0.9), int(cell_width * 0.9)))


class Food:

    def __init__(self):
        self.color = (0, 26, 35) 

    def refresh(self, screen_cell_width, screen_cell_height):
        self.cell_x = randint(0, screen_cell_width)
        self.cell_y = randint(0, screen_cell_height)
        self.cell_position = self.cell_x, self.cell_y
        print(f"New food position: {self.cell_position}")

    def draw(self, screen, cell_width):
        pygame.draw.circle(screen, self.color, ((self.cell_x + 0.5) * cell_width, (self.cell_y + 0.5) * cell_width), 
                int(cell_width / 2 * 0.75))

