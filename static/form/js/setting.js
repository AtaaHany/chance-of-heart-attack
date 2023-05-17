import {Quiz} from './Quiz.js'

export class Setting {
    constructor() {
        this.categoryElement = document.getElementById("category");
        this.difficultyElement = document.getElementsByName("difficulty");
        this.numberOfQuetion = document.getElementById("number");
        this.startBtn = document.getElementById("startBtn");
        this.startBtn.addEventListener ("click" , this.startQuiz.bind(this))
    }

    
      
  async  startQuiz ()
    {
        let amount = this.numberOfQuetion.value;
        let category = this.categoryElement.value;
        let difficulty = [ ...this.difficultyElement].filter(element=> element.checked);
        let url =`https://opentdb.com/api.php?amount=${amount}&category=${category}&difficulty=${difficulty[0].value}`
        let result = await this.fetchUrl(url);
        console.log("result")
        if (result.length>0)
        {
            $("#settings").fadeOut(500,()=> {
                $("#quiz").fadeIn(500)
            })
            new Quiz(result , amount)
        }
        
    }
    async fetchUrl(url) {
        let respones = await fetch(url);
        let data = await respones.json();
        return data.result;

    }