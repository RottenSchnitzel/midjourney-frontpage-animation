# Midjourney Frontpage animation

This is an attempt to copy the midjourny frontpage. It is a work in progress.


1. First the images get converted to a json file by executing `prepare_array.py`.
2. Then the resulting jsons are used as mappings where characters should be displayed or not.
3. For performance reasons I may need to prerender the spiral spin so the browser just needs to iterate over the large array in order to spin the spiral.
4. Some characters are randomly replaced with others so it feels more moving.

I am happy for any suggestions to improve the animation. Contributions are welcome too.