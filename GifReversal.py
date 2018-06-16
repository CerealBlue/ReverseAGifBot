from PIL import Image, ImageSequence
im = Image.open('test.gif')
frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
frames.reverse()
frames[0].save('testReverse.gif', save_all=True, append_images=frames[1:])
