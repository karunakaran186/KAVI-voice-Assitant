from transformers import AutoModel, BertTokenizerFast
from transformers import DistilBertTokenizer, DistilBertModel
from transformers import RobertaTokenizer, RobertaModel

def Bert():
    
    # Load the BERT tokenizer
    tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
    # Import BERT-base pretrained model
    bert = AutoModel.from_pretrained('bert-base-uncased')
    return tokenizer, bert
def DistilBert():
    
    # Load the DistilBert tokenizer
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    # Import the DistilBert pretrained model
    bert = DistilBertModel.from_pretrained('distilbert-base-uncased')
    return tokenizer, bert

def RobertaBert():
    
    # Load the Roberta tokenizer
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    # Import Roberta pretrained model
    bert = RobertaModel.from_pretrained('roberta-base')
    return tokenizer, bert