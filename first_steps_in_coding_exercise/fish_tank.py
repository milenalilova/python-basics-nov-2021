length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_aquarium = length * width * height
volume_litres = volume_aquarium / 1000
occupied_volume = percent / 100
litres_needed = volume_litres * (1 - occupied_volume)

print(litres_needed)
