import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot('1023733994:AAFCmwj-kiOfOW57APcXvZqnyBWCZnOMiBU')
i = 1

@bot.message_handler(commands=['start'])
def start_message(message):
    mkhi = open('static/megakokhi.tgs', 'rb')
    bot.send_sticker(message.chat.id, mkhi)
    bot.send_message(message.chat.id, 'Йо, {0.first_name}!'.format(message.from_user, bot.get_me(), parse_mode="html"))

@bot.message_handler(content_types=['text'])
def send_text(message):
    global i
    fst_list = ["🤛","🤛🏻","🤛🏼","🤛🏽","🤛🏾","🤛🏿"] #tralling
    ape_list = ["🙈","🙉","🙊","🐵","🐒"] #tralling
    daddy_list =["кто тебя создал?","кто твой создатель?","кто твой отец?","кто твой папочка?"]
    hi_list = ["привет","здарова","здорова","йо","сап","здравствуй"]
    hian_list = ["Йо","Ну привет","Здарова","Привет","Сап"]
    fck_list = ["🖕", "🖕🏻", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿"]  # tralling
    minia = ["OEZ:42190", "OEZ:42191", "OEZ:42192", "OEZ:42193", "OEZ:42194", "OEZ:42195", "OEZ:42196", "OEZ:42197", "OEZ:42198", "OEZ:42199", "OEZ:42200", "OEZ:42201", "OEZ:42202", "OEZ:42203", "OEZ:42204", "OEZ:42205", "OEZ:42206", "OEZ:42207", "OEZ:42208", "OEZ:42209", "OEZ:42210", "OEZ:42211", "OEZ:42212", "OEZ:42213", "OEZ:42216", "OEZ:42217", "OEZ:42218", "OEZ:42219", "OEZ:42220", "OEZ:42221", "OEZ:42222", "OEZ:42223", "OEZ:42224", "OEZ:42225", "OEZ:42226", "OEZ:42227", "OEZ:42228", "OEZ:42229", "OEZ:42230", "OEZ:42231", "OEZ:42232", "OEZ:42233", "OEZ:42234", "OEZ:42235", "OEZ:42236", "OEZ:42237", "OEZ:42240", "OEZ:42241", "OEZ:42242", "OEZ:42243", "OEZ:42244", "OEZ:42245", "OEZ:42246", "OEZ:42247", "OEZ:42248", "OEZ:42249", "OEZ:42250", "OEZ:42251", "OEZ:42252", "OEZ:42253", "OEZ:42254", "OEZ:42255", "OEZ:42256", "OEZ:42257", "OEZ:42258", "OEZ:42259", "OEZ:42260", "OEZ:42261", "OEZ:41952", "OEZ:41953", "OEZ:41954", "OEZ:41955", "OEZ:41956", "OEZ:41957", "OEZ:41958", "OEZ:41959", "OEZ:41960", "OEZ:41961", "OEZ:41962", "OEZ:41963", "OEZ:41964", "OEZ:41965", "OEZ:41967", "OEZ:41968", "OEZ:41969", "OEZ:41970", "OEZ:41971", "OEZ:41972", "OEZ:41973", "OEZ:41974", "OEZ:41975", "OEZ:41976", "OEZ:41977", "OEZ:41978", "OEZ:41979", "OEZ:41980", "OEZ:41981", "OEZ:41982", "OEZ:41984", "OEZ:41985", "OEZ:41986", "OEZ:41987", "OEZ:41988", "OEZ:41989", "OEZ:41990", "OEZ:41991", "OEZ:41992", "OEZ:41993", "OEZ:41994", "OEZ:41995", "OEZ:41996", "OEZ:41997", "OEZ:41998", "OEZ:41999", "OEZ:42000", "OEZ:42001", "OEZ:42002", "OEZ:42003", "OEZ:42004", "OEZ:42005", "OEZ:42006", "OEZ:42007", "OEZ:42008", "OEZ:42009", "OEZ:42010", "OEZ:42011", "OEZ:42012", "OEZ:42013", "OEZ:42014", "OEZ:42015", "OEZ:42016", "OEZ:42017", "OEZ:42018", "OEZ:42019", "OEZ:42020", "OEZ:42021", "OEZ:42022", "OEZ:42023", "OEZ:42024", "OEZ:42025", "OEZ:42026", "OEZ:42027", "OEZ:42028", "OEZ:42029", "OEZ:42030", "OEZ:42031", "OEZ:42032", "OEZ:42033", "OEZ:42034", "OEZ:42035", "OEZ:42036", "OEZ:42037", "OEZ:42038", "OEZ:42039", "OEZ:42040", "OEZ:42041", "OEZ:42042", "OEZ:42043", "OEZ:42044", "OEZ:42045", "OEZ:42046", "OEZ:42047", "OEZ:42048", "OEZ:42050", "OEZ:42051", "OEZ:42052", "OEZ:42053", "OEZ:42054", "OEZ:42055", "OEZ:42056", "OEZ:42057", "OEZ:42058", "OEZ:42059", "OEZ:42060", "OEZ:42061", "OEZ:42062", "OEZ:42063", "OEZ:42064", "OEZ:42065", "OEZ:42067", "OEZ:42068", "OEZ:42069", "OEZ:42070", "OEZ:42071", "OEZ:42072", "OEZ:42073", "OEZ:42074", "OEZ:42075", "OEZ:42076", "OEZ:42077", "OEZ:42078", "OEZ:42079", "OEZ:42080", "OEZ:42081", "OEZ:42082", "OEZ:42083", "OEZ:42084", "OEZ:42085", "OEZ:42086", "OEZ:42087", "OEZ:42088", "OEZ:42089", "OEZ:42090", "OEZ:42091", "OEZ:42092", "OEZ:42093", "OEZ:42094", "OEZ:42096", "OEZ:42097", "OEZ:42098", "OEZ:42099", "OEZ:42100", "OEZ:42101", "OEZ:42102", "OEZ:42103", "OEZ:42104", "OEZ:42105", "OEZ:42106", "OEZ:42107", "OEZ:42108", "OEZ:42109", "OEZ:42110", "OEZ:42111", "OEZ:42113", "OEZ:42114", "OEZ:42115", "OEZ:42116", "OEZ:42117", "OEZ:42118", "OEZ:42119", "OEZ:42120", "OEZ:42121", "OEZ:42122", "OEZ:42123", "OEZ:42124", "OEZ:42125", "OEZ:42126", "OEZ:42127", "OEZ:42128", "OEZ:42129", "OEZ:42130", "OEZ:42131", "OEZ:42132", "OEZ:42133", "OEZ:42134", "OEZ:42135", "OEZ:42136", "OEZ:42137", "OEZ:42138", "OEZ:42139", "OEZ:42140", "OEZ:42141", "OEZ:42142", "OEZ:42143", "OEZ:42144", "OEZ:42145", "OEZ:42146", "OEZ:42147", "OEZ:42148", "OEZ:42149", "OEZ:42150", "OEZ:42151", "OEZ:42152", "OEZ:42153", "OEZ:42154", "OEZ:42155", "OEZ:42156", "OEZ:42157", "OEZ:42158", "OEZ:42159", "OEZ:42160", "OEZ:42161", "OEZ:41847", "OEZ:41848", "OEZ:41849", "OEZ:41850", "OEZ:41851", "OEZ:41852", "OEZ:41853", "OEZ:41854", "OEZ:41855", "OEZ:41856", "OEZ:41857", "OEZ:41858", "OEZ:41859", "OEZ:41861", "OEZ:41862", "OEZ:41863", "OEZ:41864", "OEZ:41865", "OEZ:41866", "OEZ:41867", "OEZ:41868", "OEZ:41869", "OEZ:41870", "OEZ:41871", "OEZ:41872", "OEZ:41873", "OEZ:42262", "OEZ:42263", "OEZ:42264", "OEZ:42265", "OEZ:42266", "OEZ:42267", "OEZ:42268", "OEZ:42269", "OEZ:42273", "OEZ:42274", "OEZ:42275", "OEZ:42276", "OEZ:42277", "OEZ:42278", "OEZ:42279", "OEZ:42280", "OEZ:42297", "OEZ:42303", "OEZ:42299", "OEZ:42298", "OEZ:42312", "OEZ:42313", "OEZ:42315", "OEZ:42319", "OEZ:42320", "OEZ:42325", "OEZ:42323", "OEZ:42297", "OEZ:42303", "OEZ:42315", "OEZ:42388", "OEZ:42389", "OEZ:42390", "OEZ:42391", "OEZ:42392", "OEZ:42393", "OEZ:42394", "OEZ:42395", "OEZ:42396", "OEZ:42397", "OEZ:42398", "OEZ:42399", "OEZ:42400", "OEZ:42401", "OEZ:42402", "OEZ:42403", "OEZ:42404", "OEZ:42405", "OEZ:42406", "OEZ:42407", "OEZ:42408", "OEZ:42409", "OEZ:42410", "OEZ:42412", "OEZ:42413", "OEZ:42415", "OEZ:42416", "OEZ:42418", "OEZ:42419", "OEZ:42420", "OEZ:42421", "OEZ:42422", "OEZ:42423", "OEZ:42424", "OEZ:42425", "OEZ:42426", "OEZ:42427", "OEZ:42428", "OEZ:42429", "OEZ:42430", "OEZ:42441", "OEZ:42442", "OEZ:42443", "OEZ:42445", "OEZ:42446", "OEZ:42448", "OEZ:42449", "OEZ:42451", "OEZ:42452", "OEZ:42453", "OEZ:42454", "OEZ:42455", "OEZ:42456", "OEZ:42457", "OEZ:42458", "OEZ:42459", "OEZ:42460", "OEZ:42461", "OEZ:42462", "OEZ:42463", "OEZ:42305", "OEZ:42330", "OEZ:42338", "OEZ:42350", "OEZ:42332", "OEZ:42340", "OEZ:42331", "OEZ:42339", "OEZ:42351", "OEZ:42333", "OEZ:42341", "OEZ:42353"]
    minia14 = ["34528", "34529", "34530", "34532", "34533", "34534", "34535", "34536", "34537", "34538", "34539", "34540", "34549", "34550", "34551", "34553", "34554", "34555", "34556", "34557", "34558", "34559", "34560", "34561", "34657", "34659", "34660", "34661", "34662", "34663", "34664", "34665", "34666", "34667", "34676", "34677", "34678", "34680", "34681", "34682", "34683", "34684", "34685", "34686", "34687", "34688", "34872", "34874", "34875", "34876", "34877", "34878", "34879", "34880", "34881", "34882", "34891", "34892", "34893", "34895", "34896", "34897", "34898", "34899", "34900", "34901", "34902", "34903", "33864", "33867", "33868", "33869", "33870", "33871", "33872", "33873", "33874", "33875", "33876", "33877", "33878", "33879", "33882", "33885", "33887", "33888", "33889", "33890", "33891", "33892", "33893", "33894", "33895", "33896", "33897", "33898", "33899", "33900", "33903", "33906", "33908", "33909", "33910", "33911", "33912", "33913", "33914", "33915", "33916", "33917", "33918", "33919", "33920", "33921", "33922", "33923", "33924", "33925", "33926", "33927", "33928", "33929", "33930", "33931", "33932", "33933", "33934", "33935", "33936", "33937", "33938", "33939", "33940", "33941", "33942", "33943", "33944", "33945", "33946", "33947", "33948", "33949", "33950", "33951", "33952", "33953", "33954", "33955", "33956", "34162", "34163", "34164", "33957", "33958", "33959", "33960", "33961", "33962", "33963", "33964", "33965", "33966", "33967", "33970", "33973", "33975", "33976", "33977", "33978", "33979", "33980", "33981", "33982", "33983", "33984", "33985", "33986", "33987", "33988", "33991", "33994", "33996", "33997", "33998", "33999", "34000", "34001", "34002", "34003", "34004", "34005", "34006", "34007", "34011", "34014", "34015", "34016", "34017", "34018", "34019", "34020", "34021", "34022", "34023", "34024", "34025", "34026", "34029", "34032", "34034", "34035", "34036", "34037", "34038", "34039", "34040", "34041", "34042", "34043", "34044", "34045", "34046", "34047", "34050", "34053", "34055", "34056", "34057", "34058", "34059", "34060", "34061", "34062", "34063", "34064", "34065", "34066", "34067", "34068", "34069", "34070", "34071", "34072", "34073", "34074", "34075", "34076", "34077", "34078", "34079", "34080", "34081", "34082", "34083", "34084", "34085", "34086", "34087", "34088", "34089", "34090", "34091", "34092", "34093", "34094", "34095", "34096", "34097", "34098", "34099", "34100", "34101", "34115", "34116", "34117", "34118", "34119", "34120", "34121", "34122", "34123", "34124", "34125", "34126", "34127", "34141", "34142", "34143", "34144", "34145", "34146", "34147", "34148", "34149", "34150", "34151", "34152", "34153", "37214", "37215", "37216", "37217", "37218", "37219", "37220", "37221", "37223", "37224", "37225", "37226", "37227", "37228", "37229", "37230", "34260", "34261", "34263", "34264", "34325", "34326", "34330", "34333", "34335", "37287", "37289", "35664", "35665", "35950", "36787", "35299", "35301", "36788", "36789", "35300", "35302", "35303", "35305", "35307", "36795", "36790", "37258", "36793", "35304", "35306", "35308", "36796", "36791", "36794", "38436", "36797", "36800", "36798", "36801", "36799", "36802", "36806", "36809", "36813", "36817", "36807", "36810", "36814", "36808", "36811", "36815", "36818", "36812", "36816", "35273", "35274", "35277", "35275", "35278", "35276", "35279", "35280", "35283", "35287", "36830", "35281", "35284", "35288", "35282", "35285", "35289", "35291", "35286", "35290", "38938", "34338", "34343", "37284", "34339", "34344", "34341", "34346", "37285", "34342", "34347", "37286"]
    descript = ["LTP-2B-1 In 2 A Icn 6 kA", "LTP-4B-1 In 4 A Icn 6 kA", "LTP-6B-1 In 6 A Icn 6 kA", "LTP-10B-1 In 10 A Icn 6 kA", "LTP-13B-1 In 13 A Icn 6 kA", "LTP-16B-1 In 16 A Icn 6 kA", "LTP-20B-1 In 20 A Icn 6 kA", "LTP-25B-1 In 25 A Icn 6 kA", "LTP-32B-1 In 32 A Icn 6 kA", "LTP-40B-1 In 40 A Icn 6 kA", "LTP-50B-1 In 50 A Icn 6 kA", "LTP-63B-1 In 63 A Icn 6 kA", "LTP-2C-1 In 2 A Icn 6 kA", "LTP-4C-1 In 4 A Icn 6 kA", "LTP-6C-1 In 6 A Icn 6 kA", "LTP-10C-1 In 10 A Icn 6 kA", "LTP-13C-1 In 13 A Icn 6 kA", "LTP-16C-1 In 16 A Icn 6 kA", "LTP-20C-1 In 20 A Icn 6 kA", "LTP-25C-1 In 25 A Icn 6 kA", "LTP-32C-1 In 32 A Icn 6 kA", "LTP-40C-1 In 40 A Icn 6 kA", "LTP-50C-1 In 50 A Icn 6 kA", "LTP-63C-1 In 63 A Icn 6 kA", "LTP-6B-2 In 6 A Icn 6 kA", "LTP-10B-2 In 10 A Icn 6 kA", "LTP-13B-2 In 13 A Icn 6 kA", "LTP-16B-2 In 16 A Icn 6 kA", "LTP-20B-2 In 20 A Icn 6 kA", "LTP-25B-2 In 25 A Icn 6 kA", "LTP-32B-2 In 32 A Icn 6 kA", "LTP-40B-2 In 40 A Icn 6 kA", "LTP-50B-2 In 50 A Icn 6 kA", "LTP-63B-2 In 63 A Icn 6 kA", "LTP-2C-2 In 2 A Icn 6 kA", "LTP-4C-2 In 4 A Icn 6 kA", "LTP-6C-2 In 6 A Icn 6 kA", "LTP-10C-2 In 10 A Icn 6 kA", "LTP-13C-2 In 13 A Icn 6 kA", "LTP-16C-2 In 16 A Icn 6 kA", "LTP-20C-2 In 20 A Icn 6 kA", "LTP-25C-2 In 25 A Icn 6 kA", "LTP-32C-2 In 32 A Icn 6 kA", "LTP-40C-2 In 40 A Icn 6 kA", "LTP-50C-2 In 50 A Icn 6 kA", "LTP-63C-2 In 63 A Icn 6 kA", "LTP-6B-3 In 6 A Icn 6 kA", "LTP-10B-3 In 10 A Icn 6 kA", "LTP-13B-3 In 13 A Icn 6 kA", "LTP-16B-3 In 16 A Icn 6 kA", "LTP-20B-3 In 20 A Icn 6 kA", "LTP-25B-3 In 25 A Icn 6 kA", "LTP-32B-3 In 32 A Icn 6 kA", "LTP-40B-3 In 40 A Icn 6 kA", "LTP-50B-3 In 50 A Icn 6 kA", "LTP-63B-3 In 63 A Icn 6 kA", "LTP-2C-3 In 2 A Icn 6 kA", "LTP-4C-3 In 4 A Icn 6 kA", "LTP-6C-3 In 6 A Icn 6 kA", "LTP-10C-3 In 10 A Icn 6 kA", "LTP-13C-3 In 13 A Icn 6 kA", "LTP-16C-3 In 16 A Icn 6 kA", "LTP-20C-3 In 20 A Icn 6 kA", "LTP-25C-3 In 25 A Icn 6 kA", "LTP-32C-3 In 32 A Icn 6 kA", "LTP-40C-3 In 40 A Icn 6 kA", "LTP-50C-3 In 50 A Icn 6 kA", "LTP-63C-3 In 63 A Icn 6 kA", "LTS-1B-1 In 1 A Icn 10 kA", "LTS-2B-1 In 2 A Icn 10 kA", "LTS-4B-1 In 4 A Icn 10 kA", "LTS-6B-1 In 6 A Icn 10 kA", "LTS-8B-1 In 8 A Icn 10 kA", "LTS-10B-1 In 10 A Icn 10 kA", "LTS-13B-1 In 13 A Icn 10 kA", "LTS-16B-1 In 16 A Icn 10 kA", "LTS-20B-1 In 20 A Icn 10 kA", "LTS-25B-1 In 25 A Icn 10 kA", "LTS-32B-1 In 32 A Icn 10 kA", "LTS-40B-1 In 40 A Icn 10 kA", "LTS-50B-1 In 50 A Icn 10 kA", "LTS-63B-1 In 63 A Icn 10 kA", "LTS-05C-1 In 0 Icn 10 kA", "LTS-1C-1 In 1 A Icn 10 kA", "LTS-16C-1 In 1 Icn 10 kA", "LTS-2C-1 In 2 A Icn 10 kA", "LTS-4C-1 In 4 A Icn 10 kA", "LTS-6C-1 In 6 A Icn 10 kA", "LTS-8C-1 In 8 A Icn 10 kA", "LTS-10C-1 In 10 A Icn 10 kA", "LTS-13C-1 In 13 A Icn 10 kA", "LTS-16C-1 In 16 A Icn 10 kA", "LTS-20C-1 In 20 A Icn 10 kA", "LTS-25C-1 In 25 A Icn 10 kA", "LTS-32C-1 In 32 A Icn 10 kA", "LTS-40C-1 In 40 A Icn 10 kA", "LTS-50C-1 In 50 A Icn 10 kA", "LTS-63C-1 In 63 A Icn 10 kA", "LTS-05D-1 In 0 Icn 10 kA", "LTS-1D-1 In 1 A Icn 10 kA", "LTS-16D-1 In 1 Icn 10 kA", "LTS-2D-1 In 2 A Icn 10 kA", "LTS-4D-1 In 4 A Icn 10 kA", "LTS-6D-1 In 6 A Icn 10 kA", "LTS-8D-1 In 8 A Icn 10 kA", "LTS-10D-1 In 10 A Icn 10 kA", "LTS-13D-1 In 13 A Icn 10 kA", "LTS-16D-1 In 16 A Icn 10 kA", "LTS-20D-1 In 20 A Icn 10 kA", "LTS-25D-1 In 25 A Icn 10 kA", "LTS-32D-1 In 32 A Icn 10 kA", "LTS-40D-1 In 40 A Icn 10 kA", "LTS-50D-1 In 50 A Icn 10 kA", "LTS-63D-1 In 63 A Icn 10 kA", "LTS-6B-1N In 6 A Icn 10 kA", "LTS-8B-1N In 8 A Icn 10 kA", "LTS-10B-1N In 10 A Icn 10 kA", "LTS-13B-1N In 13 A Icn 10 kA", "LTS-16B-1N In 16 A Icn 10 kA", "LTS-20B-1N In 20 A Icn 10 kA", "LTS-25B-1N In 25 A Icn 10 kA", "LTS-32B-1N In 32 A Icn 10 kA", "LTS-40B-1N In 40 A Icn 10 kA", "LTS-50B-1N In 50 A Icn 10 kA", "LTS-63B-1N In 63 A Icn 10 kA", "LTS-2C-1N In 2 A Icn 10 kA", "LTS-4C-1N In 4 A Icn 10 kA", "LTS-6C-1N In 6 A Icn 10 kA", "LTS-8C-1N In 8 A Icn 10 kA", "LTS-10C-1N In 10 A Icn 10 kA", "LTS-13C-1N In 13 A Icn 10 kA", "LTS-16C-1N In 16 A Icn 10 kA", "LTS-20C-1N In 20 A Icn 10 kA", "LTS-25C-1N In 25 A Icn 10 kA", "LTS-32C-1N In 32 A Icn 10 kA", "LTS-40C-1N In 40 A Icn 10 kA", "LTS-50C-1N In 50 A Icn 10 kA", "LTS-63C-1N In 63 A Icn 10 kA", "LTS-6D-1N In 6 A Icn 10 kA", "LTS-8D-1N In 8 A Icn 10 kA", "LTS-10D-1N In 10 A Icn 10 kA", "LTS-13D-1N In 13 A Icn 10 kA", "LTS-16D-1N In 16 A Icn 10 kA", "LTS-20D-1N In 20 A Icn 10 kA", "LTS-25D-1N In 25 A Icn 10 kA", "LTS-32D-1N In 32 A Icn 10 kA", "LTS-40D-1N In 40 A Icn 10 kA", "LTS-50D-1N In 50 A Icn 10 kA", "LTS-63D-1N In 63 A Icn 10 kA", "LTS-1B-2 In 1 A Icn 10 kA", "LTS-2B-2 In 2 A Icn 10 kA", "LTS-4B-2 In 4 A Icn 10 kA", "LTS-6B-2 In 6 A Icn 10 kA", "LTS-8B-2 In 8 A Icn 10 kA", "LTS-10B-2 In 10 A Icn 10 kA", "LTS-13B-2 In 13 A Icn 10 kA", "LTS-16B-2 In 16 A Icn 10 kA", "LTS-20B-2 In 20 A Icn 10 kA", "LTS-25B-2 In 25 A Icn 10 kA", "LTS-32B-2 In 32 A Icn 10 kA", "LTS-40B-2 In 40 A Icn 10 kA", "LTS-50B-2 In 50 A Icn 10 kA", "LTS-63B-2 In 63 A Icn 10 kA", "LTS-05C-2 In 0 Icn 10 kA", "LTS-1C-2 In 1 A Icn 10 kA", "LTS-16C-2 In 1 Icn 10 kA", "LTS-2C-2 In 2 A Icn 10 kA", "LTS-4C-2 In 4 A Icn 10 kA", "LTS-6C-2 In 6 A Icn 10 kA", "LTS-8C-2 In 8 A Icn 10 kA", "LTS-10C-2 In 10 A Icn 10 kA", "LTS-13C-2 In 13 A Icn 10 kA", "LTS-16C-2 In 16 A Icn 10 kA", "LTS-20C-2 In 20 A Icn 10 kA", "LTS-25C-2 In 25 A Icn 10 kA", "LTS-32C-2 In 32 A Icn 10 kA", "LTS-40C-2 In 40 A Icn 10 kA", "LTS-50C-2 In 50 A Icn 10 kA", "LTS-63C-2 In 63 A Icn 10 kA", "LTS-05D-2 In 0 Icn 10 kA", "LTS-1D-2 In 1 A Icn 10 kA", "LTS-16D-2 In 1 Icn 10 kA", "LTS-2D-2 In 2 A Icn 10 kA", "LTS-4D-2 In 4 A Icn 10 kA", "LTS-6D-2 In 6 A Icn 10 kA", "LTS-8D-2 In 8 A Icn 10 kA", "LTS-10D-2 In 10 A Icn 10 kA", "LTS-13D-2 In 13 A Icn 10 kA", "LTS-16D-2 In 16 A Icn 10 kA", "LTS-20D-2 In 20 A Icn 10 kA", "LTS-25D-2 In 25 A Icn 10 kA", "LTS-32D-2 In 32 A Icn 10 kA", "LTS-40D-2 In 40 A Icn 10 kA", "LTS-1B-3 In 1 A Icn 10 kA", "LTS-2B-3 In 2 A Icn 10 kA", "LTS-4B-3 In 4 A Icn 10 kA", "LTS-6B-3 In 6 A Icn 10 kA", "LTS-8B-3 In 8 A Icn 10 kA", "LTS-10B-3 In 10 A Icn 10 kA", "LTS-13B-3 In 13 A Icn 10 kA", "LTS-16B-3 In 16 A Icn 10 kA", "LTS-20B-3 In 20 A Icn 10 kA", "LTS-25B-3 In 25 A Icn 10 kA", "LTS-32B-3 In 32 A Icn 10 kA", "LTS-40B-3 In 40 A Icn 10 kA", "LTS-50B-3 In 50 A Icn 10 kA", "LTS-63B-3 In 63 A Icn 10 kA", "LTS-05C-3 In 0 Icn 10 kA", "LTS-1C-3 In 1 A Icn 10 kA", "LTS-16C-3 In 1 Icn 10 kA", "LTS-2C-3 In 2 A Icn 10 kA", "LTS-4C-3 In 4 A Icn 10 kA", "LTS-6C-3 In 6 A Icn 10 kA", "LTS-8C-3 In 8 A Icn 10 kA", "LTS-10C-3 In 10 A Icn 10 kA", "LTS-13C-3 In 13 A Icn 10 kA", "LTS-16C-3 In 16 A Icn 10 kA", "LTS-20C-3 In 20 A Icn 10 kA", "LTS-25C-3 In 25 A Icn 10 kA", "LTS-32C-3 In 32 A Icn 10 kA", "LTS-40C-3 In 40 A Icn 10 kA", "LTS-50C-3 In 50 A Icn 10 kA", "LTS-63C-3 In 63 A Icn 10 kA", "LTS-05D-3 In 0 Icn 10 kA", "LTS-1D-3 In 1 A Icn 10 kA", "LTS-16D-3 In 1 Icn 10 kA", "LTS-2D-3 In 2 A Icn 10 kA", "LTS-4D-3 In 4 A Icn 10 kA", "LTS-6D-3 In 6 A Icn 10 kA", "LTS-8D-3 In 8 A Icn 10 kA", "LTS-10D-3 In 10 A Icn 10 kA", "LTS-13D-3 In 13 A Icn 10 kA", "LTS-16D-3 In 16 A Icn 10 kA", "LTS-20D-3 In 20 A Icn 10 kA", "LTS-25D-3 In 25 A Icn 10 kA", "LTS-32D-3 In 32 A Icn 10 kA", "LTS-40D-3 In 40 A Icn 10 kA", "LTS-50D-3 In 50 A Icn 10 kA", "LTS-63D-3 In 63 A Icn 10 kA", "LTS-2B-3N In 2 A Icn 10 kA", "LTS-4B-3N In 4 A Icn 10 kA", "LTS-6B-3N In 6 A Icn 10 kA", "LTS-8B-3N In 8 A Icn 10 kA", "LTS-10B-3N In 10 A Icn 10 kA", "LTS-13B-3N In 13 A Icn 10 kA", "LTS-16B-3N In 16 A Icn 10 kA", "LTS-20B-3N In 20 A Icn 10 kA", "LTS-25B-3N In 25 A Icn 10 kA", "LTS-32B-3N In 32 A Icn 10 kA", "LTS-40B-3N In 40 A Icn 10 kA", "LTS-50B-3N In 50 A Icn 10 kA", "LTS-63B-3N In 63 A Icn 10 kA", "LTS-6C-3N In 6 A Icn 10 kA", "LTS-8C-3N In 8 A Icn 10 kA", "LTS-10C-3N In 10 A Icn 10 kA", "LTS-13C-3N In 13 A Icn 10 kA", "LTS-16C-3N In 16 A Icn 10 kA", "LTS-20C-3N In 20 A Icn 10 kA", "LTS-25C-3N In 25 A Icn 10 kA", "LTS-32C-3N In 32 A Icn 10 kA", "LTS-40C-3N In 40 A Icn 10 kA", "LTS-50C-3N In 50 A Icn 10 kA", "LTS-63C-3N In 63 A Icn 10 kA", "LTS-6D-3N In 6 A Icn 10 kA", "LTS-8D-3N In 8 A Icn 10 kA", "LTS-10D-3N In 10 A Icn 10 kA", "LTS-13D-3N In 13 A Icn 10 kA", "LTS-16D-3N In 16 A Icn 10 kA", "LTS-20D-3N In 20 A Icn 10 kA", "LTS-25D-3N In 25 A Icn 10 kA", "LTS-32D-3N In 32 A Icn 10 kA", "LTS-40D-3N In 40 A Icn 10 kA", "LTN-UC-2C-1 In 2 A Icn 10 kA", "LTN-UC-4C-1 In 4 A Icn 10 kA", "LTN-UC-6C-1 In 6 A Icn 10 kA", "LTN-UC-8C-1 In 8 A Icn 10 kA", "LTN-UC-10C-1 In 10 A Icn 10 kA", "LTN-UC-13C-1 In 13 A Icn 10 kA", "LTN-UC-16C-1 In 16 A Icn 10 kA", "LTN-UC-20C-1 In 20 A Icn 10 kA", "LTN-UC-25C-1 In 25 A Icn 10 kA", "LTN-UC-32C-1 In 32 A Icn 10 kA", "LTN-UC-40C-1 In 40 A Icn 10 kA", "LTN-UC-50C-1 In 50 A Icn 10 kA", "LTN-UC-63C-1 In 63 A Icn 10 kA", "LTN-UC-2C-2 In 2 A Icn 10 kA", "LTN-UC-4C-2 In 4 A Icn 10 kA", "LTN-UC-6C-2 In 6 A Icn 10 kA", "LTN-UC-8C-2 In 8 A Icn 10 kA", "LTN-UC-10C-2 In 10 A Icn 10 kA", "LTN-UC-13C-2 In 13 A Icn 10 kA", "LTN-UC-16C-2 In 16 A Icn 10 kA", "LTN-UC-20C-2 In 20 A Icn 10 kA", "LTN-UC-25C-2 In 25 A Icn 10 kA", "LTN-UC-32C-2 In 32 A Icn 10 kA", "LTN-UC-40C-2 In 40 A Icn 10 kA", "LTN-UC-50C-2 In 50 A Icn 10 kA", "LTN-UC-63C-2 In 63 A Icn 10 kA", "LVN-80B-1 In 80 A Icn 10 kA", "LVN-100B-1 In 100 A Icn 10 kA", "LVN-125B-1 In 125 A Icn 10 kA", "LVN-80C-1 In 80 A Icn 10 kA", "LVN-100C-1 In 100 A Icn 10 kA", "LVN-125C-1 In 125 A Icn 10 kA", "LVN-80D-1 In 80 A Icn 10 kA", "LVN-100D-1 In 100 A Icn 10 kA", "LVN-80B-3 In 80 A Icn 10 kA", "LVN-100B-3 In 100 A Icn 10 kA", "LVN-125B-3 In 125 A Icn 10 kA", "LVN-80C-3 In 80 A Icn 10 kA", "LVN-100C-3 In 100 A Icn 10 kA", "LVN-125C-3 In 125 A Icn 10 kA", "LVN-80D-3 In 80 A Icn 10 kA", "LVN-100D-3 In 100 A Icn 10 kA", "PS-LT-1100", "PS-LT-1100-MN", "PS-LT-2000", "PS-LT-0200", "SV-LT-X060 Ue AC/DC 60 V", "SV-LT-X400 Ue AC 400 V / DC 110 V", "SP-LT-A230 Ue AC 230 V", "SP-LT-D024 Ue DC 24 V", "SP-LT-D110 Ue DC 110 V", "OD-LT-VU02 для LTS", "OD-LT-VP01 для LTS", "PS-LT-1100", "PS-LT-1100-MN", "SP-LT-A230 Ue AC 230 V", "LFE-16-2-010AC In 16 A Inc 6 kA", "LFE-25-2-030AC In 25 A Inc 6 kA", "LFE-40-2-030AC In 40 A Inc 6 kA", "LFE-25-2-100AC In 25 A Inc 6 kA", "LFE-40-2-100AC In 40 A Inc 6 kA", "LFE-25-2-300AC In 25 A Inc 6 kA", "LFE-40-2-300AC In 40 A Inc 6 kA", "LFE-25-4-030AC In 25 A Inc 6 kA", "LFE-40-4-030AC In 40 A Inc 6 kA", "LFE-63-4-030AC In 63 A Inc 6 kA", "LFE-80-4-030AC In 80 A Inc 6 kA", "LFE-25-4-100AC In 25 A Inc 6 kA", "LFE-40-4-100AC In 40 A Inc 6 kA", "LFE-63-4-100AC In 63 A Inc 6 kA", "LFE-25-4-300AC In 25 A Inc 6 kA", "LFE-40-4-300AC In 40 A Inc 6 kA", "LFE-63-4-300AC In 63 A Inc 6 kA", "LFE-80-4-300AC In 80 A Inc 6 kA", "LFE-40-4-500AC In 40 A Inc 6 kA", "LFE-63-4-500AC In 63 A Inc 6 kA", "LFN-16-2-010AC In 16 A Inc 10 kA", "LFN-25-2-030AC In 25 A Inc 10 kA", "LFN-40-2-030AC In 40 A Inc 10 kA", "LFN-25-2-100AC In 25 A Inc 10 kA", "LFN-40-2-100AC In 40 A Inc 10 kA", "LFN-25-2-300AC In 25 A Inc 10 kA", "LFN-40-2-300AC In 40 A Inc 10 kA", "LFN-25-4-030AC In 25 A Inc 10 kA", "LFN-40-4-030AC In 40 A Inc 10 kA", "LFN-63-4-030AC In 63 A Inc 10 kA", "LFN-80-4-030AC In 80 A Inc 10 kA", "LFN-25-4-100AC In 25 A Inc 10 kA", "LFN-40-4-100AC In 40 A Inc 10 kA", "LFN-63-4-100AC In 63 A Inc 10 kA", "LFN-25-4-300AC In 25 A Inc 10 kA", "LFN-40-4-300AC In 40 A Inc 10 kA", "LFN-63-4-300AC In 63 A Inc 10 kA", "LFN-80-4-300AC In 80 A Inc 10 kA", "LFN-40-4-500AC In 40 A Inc 10 kA", "LFN-63-4-500AC In 63 A Inc 10 kA", "LFN-16-2-010A In 16 A Inc 10 kA", "LFN-25-2-030A In 25 A Inc 10 kA", "LFN-40-2-030A In 40 A Inc 10 kA", "LFN-25-2-100A In 25 A Inc 10 kA", "LFN-40-2-100A In 40 A Inc 10 kA", "LFN-25-2-300A In 25 A Inc 10 kA", "LFN-40-2-300A In 40 A Inc 10 kA", "LFN-25-4-030A In 25 A Inc 10 kA", "LFN-40-4-030A In 40 A Inc 10 kA", "LFN-63-4-030A In 63 A Inc 10 kA", "LFN-80-4-030A In 80 A Inc 10 kA", "LFN-25-4-100A In 25 A Inc 10 kA", "LFN-40-4-100A In 40 A Inc 10 kA", "LFN-63-4-100A In 63 A Inc 10 kA", "LFN-25-4-300A In 25 A Inc 10 kA", "LFN-40-4-300A In 40 A Inc 10 kA", "LFN-63-4-300A In 63 A Inc 10 kA", "LFN-80-4-300A In 80 A Inc 10 kA", "LFN-40-4-500A In 40 A Inc 10 kA", "LFN-63-4-500A In 63 A Inc 10 kA", "PS-LT-1100-K", "MSO-32-1 In 32 A", "MSO-63-1 In 63 A", "MSO-125-1 In 125 A", "MSO-32-1N In 32 A", "MSO-63-1N In 63 A", "MSO-32-3 In 32 A", "MSO-63-3 In 63 A", "MSO-125-3 In 125 A", "MSO-32-3N In 32 A", "MSO-63-3N In 63 A", "MSO-125-3N In 125 A"]
    if message.text.lower() in minia14:
        bot.send_message(message.chat.id, minia[minia14.index(message.text.lower())])
        bot.send_message(message.chat.id, descript[minia14.index(message.text.lower())])
       
    elif len(message.text.lower()) == 1:
        bot.send_message(message.chat.id, "😒")
 
    #elif message.text.lower() in minia7:
        #bot.send_message(message.chat.id, minia[minia7.index(message.text.lower())])

    elif message.text.lower() in hi_list:
        bot.send_message(message.chat.id, str(random.choice( hian_list )))

    elif message.text.lower() in fst_list:
        bot.send_message(message.chat.id, '🤜🏾')

    elif message.text.lower() in fck_list:
        if i < 3:
            bot.send_message(message.chat.id, '🖕🏾')
            i += 1

        elif i == 3:
            bot.send_message(message.chat.id, '😡')
            i += 1

        else:
            i = 1
            bot.send_message(message.chat.id, '{0.first_name}! Иди на хуй'.format( message.from_user, bot.get_me(), parse_mode = "html" ))

    elif message.text.lower() == "эски":
        bot.send_message(message.chat.id, str(random.choice(ape_list)))

    elif message.text.lower() in daddy_list:
        bot.send_message(message.chat.id, '@e_rocket')

    elif message.text.lower() == "тиай":
        sti = open('static/sticker.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)

    else:
        bot.send_message(message.chat.id, 'Чо каво, сучара!?')


bot.polling(none_stop = True)
