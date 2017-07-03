var searchBar = new Vue({
    el: '#searchBar',
    data: {
        seen: true,
        value: '',
        searchArgs: {
            pattern: /[`~\!@$%\^&\*\(\)\-\+\=\{\}\[\]\\\|;\:'",<\.>\/\? ]/g,
            finish: true,
            over500ms: true,
            temp: {word: '', type: ''},
            searchTypeList: ['全部', '名称', '作者'],
            searchType: '全部',
        },
    },
    methods: {
        search: function(){
            if (!this.searchArgs.finish || !this.searchArgs.over500ms){
                return false
            }
            this.searchArgs.finish = false
            this.searchArgs.over500ms = false
            setTimeout("searchBar.over500ms()", 500)
            this.searchArgs.temp['word'] = this.value
            this.searchArgs.temp['type'] = this.searchArgs.searchType
            $('#searchResult [comic]').hide()
            var value = this.value.replace(this.searchArgs.pattern, '')
            if (value){
                if (this.searchArgs.searchType === '全部' || this.searchArgs.searchType === '名称'){
                    $('#searchResult [comic*=' + value + ']').show()
                }
                if (this.searchArgs.searchType === '全部' || this.searchArgs.searchType === '作者'){
                    $('#searchResult [author*=' + value + ']').show()
                }
            }
            this.searchArgs.finish = true
            if (this.searchArgs.over500ms && (this.searchArgs.temp['word'] !== this.value || this.searchArgs.temp['type'] !== this.searchArgs.searchType)){
                this.search()
            }
        },
        over500ms: function(){
            this.searchArgs.over500ms = true
            if (this.searchArgs.finish && (this.searchArgs.temp['word'] !== this.value || this.searchArgs.temp['type'] !== this.searchArgs.searchType)){
                this.search()
            }
        },
        changeSearchType: function(){
            this.searchArgs.searchTypeList.push(this.searchArgs.searchTypeList.shift())
            this.searchArgs.searchType = this.searchArgs.searchTypeList[0]
            this.search()
        },
    }
})

var searchResult = new Vue({
    el: '#searchResult',
    data: {
        seen: true,
        index: index,
        extLink: extLink,
    },
    methods: {
        isEmptyObject: jQuery.isEmptyObject,
        showMenu: function(item){
            if (extLink[item['编号']]){
                console.log('have loaded file')
                return false
            }
            let headElement = document.getElementsByTagName("head")[0]
            let scriptElement = document.createElement("script")
            let src = 'generate/' + item['编号'] + '.js'
            scriptElement.src = src
            headElement.appendChild(scriptElement)
        },
        showPage: function(key, dict){
            console.log(dict)
            console.log(dict[key])
            searchBar.seen = false
            searchResult.seen = false
            comicViewer.episode = dict
            comicViewer.episode_num = key
            comicViewer.pics = dict[key]
            comicViewer.pics_num = 0
            comicViewer.page_num = 0
            comicViewer.seen = true
        },
    },
})

var comicViewer = new Vue({
    el: '#comicViewer',
    data: {
        seen: false,
        episode: null,
        episode_num: null,
        pics: null,
        pics_num: 0,
        page_num: 0,
    },
    computed: {
        img_src: function(){
            if (this.pics && this.pics.length !== 0) {
                return this.pics[this.pics_num][this.page_num]
            } else {
                return ''
            }
        },
        is_special: function(){
            return isNaN(Number(this.episode_num))
        }
    },
    methods: {
        pre_page: function(){
            console.log('pre page')
            if (this.page_num === 0) {
                console.log('first page')
            } else {
                this.page_num -= 1
            }
        },
        next_page: function(){
            if (this.page_num + 1 < this.pics[this.pics_num].length){
                console.log('next page')
                this.page_num += 1
            } else {
                this.next_episode()
            }
        },
        pre_episode: function(){
            if (this.is_special) {
                console.log('special episode')
                return false
            }
            this.page_num = 0
            this.episode_num = Number(this.episode_num)
            if (this.episode_num === 1) {
                console.log('first episode')
            } else {
                console.log('pre episode')
                this.episode_num = String((episode_num - 1))
                this.pics = this.episode[this.episode_num]
            }
        },
        next_episode: function(){
            if (this.is_special) {
                console.log('special episode')
                return false
            }
            this.page_num = 0
            this.episode_num = String((Number(this.episode_num) + 1))
            if (!this.episode[this.episode_num]) {
                console.log('last episode')
                searchBar.seen = true
                searchResult.seen = true
                this.seen = false
                return false
            } else {
                console.log('next episode')
                this.pics = this.episode[this.episode_num]
            }
        },
    },
})

var viewer = $('#comicViewer img')
$('html').on('keyup', function(event) {
    if (!viewer.is(':visible')) {
        return false
    }
    if (event.which === 37) {          // left
        comicViewer.pre_episode()
    } else if (event.which === 38) {   // up
        comicViewer.pre_page()
    } else if (event.which === 39) {   // right
        comicViewer.next_episode()
    } else if (event.which === 40) {   // down
        comicViewer.next_page()
    } else if (event.which === 27) {   // esc
        searchBar.seen = true
        searchResult.seen = true
        comicViewer.seen = false
    }
})