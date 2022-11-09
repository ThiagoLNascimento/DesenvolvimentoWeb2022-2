/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(function () {

   let x = 0

   $("div.card-title").each(function(){

      $(this).append(
         `<div style="display: inline">
            <span id="like${x}" data-like="8"></span>
            <a href="#" class="mr-2" style="text-decoration: none">
               <i class="far fa-thumbs-up"></i>
            </a>
            <a href="#" style="text-decoration: none">
               <i class="far fa-thumbs-down"></i>
            </a>
            <span id="dislike${x}" data-dislike="3"></span>
            
         </div>`)
      
      let like = $(`#like${x}`).data("like")
      let dislike = $(`#dislike${x}`).data("dislike")

      $(`#like${x}`).addClass("badge badge-secondary")
      $(`#dislike${x}`).addClass("badge badge-secondary")
      
      $(`#like${x}`).text(like)
      $(`#dislike${x}`).text(dislike)

      $(`#like${x}`).click(function(){
         let thumbsUp = $(this).next().children()
         let thumbsDown = $(this).next().next().children()

         if(thumbsUp.hasClass("far") && thumbsDown.hasClass("far")){
            $(this).data("like", $(this).data("like") + 1)
            $(this).text($(this).data("like"))
            thumbsUp.addClass("fas")
            thumbsUp.removeClass("far")
         }
         else if(thumbsUp.hasClass("fas") && thumbsDown.hasClass("far")){
            $(this).data("like", $(this).data("like") - 1)
            $(this).text($(this).data("like"))
            thumbsUp.addClass("far")
            thumbsUp.removeClass("fas")
         }
         else if(thumbsUp.hasClass("far") && thumbsDown.hasClass("fas")){
            $(this).data("like", $(this).data("like") + 1)
            $(this).text($(this).data("like"))
            thumbsUp.addClass("fas")
            thumbsUp.removeClass("far")
            $(this).next().next().next().data("dislike", $(this).next().next().next().data("dislike") - 1)
            $(this).next().next().next().text($(this).next().next().next().data("dislike"))
            thumbsDown.addClass("far")
            thumbsDown.removeClass("fas")
         }

      })

      $(`#dislike${x}`).click(function(){
         let thumbsUp = $(this).prev().prev().children()
         let thumbsDown = $(this).prev().children()

         if(thumbsDown.hasClass("far") && thumbsUp.hasClass("far")){
            $(this).data("dislike", $(this).data("dislike") + 1)
            $(this).text($(this).data("dislike"))
            thumbsDown.addClass("fas")
            thumbsDown.removeClass("far")
         }
         else if(thumbsDown.hasClass("fas") && thumbsUp.hasClass("far")){
            $(this).data("dislike", $(this).data("dislike") - 1)
            $(this).text($(this).data("dislike"))
            thumbsDown.addClass("far")
            thumbsDown.removeClass("fas")
         }
         else if(thumbsDown.hasClass("far") && thumbsUp.hasClass("fas")){
            $(this).data("dislike", $(this).data("dislike") + 1)
            $(this).text($(this).data("dislike"))
            thumbsDown.addClass("fas")
            thumbsDown.removeClass("far")
            $(this).prev().prev().prev().data("like", $(this).prev().prev().prev().data("like") - 1)
            $(this).prev().prev().prev().text($(this).prev().prev().prev().data("like"))
            thumbsUp.addClass("far")
            thumbsUp.removeClass("fas")
         }
      })

      x = x + 1
   })

});