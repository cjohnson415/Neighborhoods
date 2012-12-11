// Stanford TMT Example 1 - Loading data
// http://nlp.stanford.edu/software/tmt/0.4/

// tells Scala where to find the TMT classes
import scalanlp.io._;
import scalanlp.stage._;
import scalanlp.stage.text._;
import scalanlp.text.tokenize._;
import scalanlp.pipes.Pipes.global._;

import edu.stanford.nlp.tmt.stage._;
import edu.stanford.nlp.tmt.model.lda._;
import edu.stanford.nlp.tmt.model.llda._;

val source = CSVFile("forsale.csv") ~> IDColumn(1);

val tokenizer = {
  SimpleEnglishTokenizer() ~>            // tokenize on space and punctuation
  CaseFolder() ~>                        // lowercase everything
  WordsAndNumbersOnlyFilter() ~>         // ignore non-words and non-numbers
  MinimumLengthFilter(5)                 // take terms with >=3 characters
}

val text = {
  source ~>                              // read from the source file
  Columns(2,3) ~> Join(" ") ~>            // select column containing text
  TokenizeWith(tokenizer) ~>             // tokenize with tokenizer above
  TermCounter() ~>                       // collect counts (needed below)
  TermMinimumDocumentCountFilter(10) ~>  // filter terms in <10 docs
  TermDynamicStopListFilter(20) ~>
  DocumentMinimumLengthFilter(5)
}

// display information about the loaded dataset
println("Jobs Words:");
println(text.description);

println();
println("------------------------------------");
println();

println("Terms in the stop list:");
for (term <- text.meta[TermStopList]) {
  println("  " + term);
}
