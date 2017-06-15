# The UW eScience DSSG blog website

To create a new post:

- Clone this repo.
```
    git clone https://github.com/uwescience/DSSG2017
```

- Posts need to be added as new markdown files in the `_posts` directory. 
  File names need to be something like `2017-06-16-example-post.md`. Note that 
  the details in the header need to be something like:

      ---
      layout: post
      title:  "Example Post"
      date:   2017-06-16
      author: Valentina Staneva
      ---

  with your name, the title you want for your post, and the date you are
  writing it.

- The site is automatically rendered at [http://uwescience.github.io/DSSG2017/](http://uwescience.github.io/DSSG2017/)

- To test how the website looks locally before publishing, you need to set up [Jekyll](https://jekyllrb.com/) (a static website generator). For more information about the markdown syntax
  that you can use to write posts, add links, images, etc., refer to the
  example post that is already there, and to the
  [Jekyll documentation](https://jekyllrb.com/docs/home/)
  
- Images go into the `assets/images` directory.

  Using Markdown Syntax:

  ``` 
  ![picture ]({{ site.url }}/assets/images/picture.png)
  ```

  Using HTML Syntax:
  ```
  <img src="{{site.url}}/assets/images/picture.png" align="left" style="margin: 0 10px 10px 0">
  ```



## Copyright & License

The template used for this website is Kasper, released under the following
license:

Copyright (C) 2013 Ghost Foundation - Released under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
