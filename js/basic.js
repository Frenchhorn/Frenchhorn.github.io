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
        index: window.index,
        extLink: window.extLink,
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
            let src = (noGit) ? 'https://frenchhorn.github.io/' : ''
            src += 'generate/' + item['编号'] + '.js'
            scriptElement.src = src
            headElement.appendChild(scriptElement)
        },
        showPage: function(key, dict){
            console.log(dict[key])
            searchBar.seen = false
            searchResult.seen = false
            comicViewer.args.pics = dict[key]
        },
    },
})

var comicViewer = new Vue({
    el: '#comicViewer',
    data: {
        seen: true,
        args: {
            pics: null,
            source: 0,
            num: 0,
        }
    },
    methods: {
        next: function(){
            console.log('next page')
            if (this.args.num + 1 < this.args.pics[this.args.source].length){
                this.args.num += 1
            } else {
                this.args.num = 0
            }
        }
    },
})