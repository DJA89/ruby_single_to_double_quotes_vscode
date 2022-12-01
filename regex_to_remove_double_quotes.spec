
describe "Deleting some double quotes" do
  # find and replace to substitute ruby double quotes with single quotes where applicable
  # on find put the following regex without backquotes
  # `^((?:(?:[^"'])|(?:'(?:[^\\']|(?:\\.))*'))*)"((?!(?:(?:[^\\"])|(?:\\[^"]))*(?:(?:#\{.*\})|'))(?:(?:[^\\"])|(?:\\[^"]))*)"`
  # on replace put `$1'$2'` without backquotes

  INTERPOLATION = 'some string to interpolate'.freeze

  context "with dobule quotes" do
    context "without interpolation" do
      it "substitutes them with single quotes" do
        expect("").to eq('')
      end
    end

    context 'with multiple double-quoted strings in a row' do
      context 'they can all be substituted' do
        it 'substitutes them one at a time' do
          puts "this can be substituted"; expect("also this").to eq('also this')
        end
      end

    context 'at least one of them cannot be substituted' do
      it 'only substitutes until it finds one that it cannot' do
        puts "nice string"; puts "This isn't going to get substituted"; expect("neither will this :(").to_not eq('neither will this :(')

        # note, this last example _would_ work with the following regex in theory:
        # `^((?:(?:(?:[^'"])|(?:'(?:[^\\']|(?:\\.))*'))|(?:(?:(?:[^'"])|(?:"(?:[^\\"]|(?:\\.))*"))))*)"((?!(?:(?:[^\\"])|(?:\\[^"]))*(?:(?:#\{.*\})|'))(?:(?:[^\\"])|(?:\\[^"]))*)"`
        # but it crashes my VSCode, so probably not a good idea to use it
        # as it is, only the first double-quoted regex in each line is considered on each find

        # note 2, it is possible to look for strings from the back of the line and then this example would work,
        # but strings between other double-quoted strings wouldn't work
        # I'd use something like this:
        # `"((?!(?:(?:[^\\"])|(?:\\[^"]))*(?:(?:#\{.*\})|'))(?:(?:[^\\"])|(?:\\[^"]))*)"((?:(?:[^"'])|(?:'(?:[^\\']|(?:\\.))*'))*)$`
        # with `'$1'$2`
        # also, if I could have infinite capture groups then this could also be possible
        # but I haven't found a way of doing so
      end
    end

    context "with single quotes" do
      it "doesn't substitute them" do
        expect("'").to_not eq('\'')
      end
    end

    context "with #{INTERPOLATION}" do
      it "does not remove them" do
        expect("#{INTERPOLATION}").to_not eq('#{INTERPOLATION}')
      end
    end

    context "with \"" do
        it 'does not substitute it' do
            # Yes, this would be too complicated
            expect("\"").to_not eq('"')
        end
    end

    context 'between single quotes' do
      it 'does nothing' do
        expect(' "good string here" right?').to_not eq(' \'good string here\' right?')
      end
    end

    context 'after something with single quotes' do
      it 'does substitute it' do
        puts 'nice string'; expect("this string").to eq('this string')
      end

      context 'with single-quoted string having a \' in it' do
        it 'does substitute it' do
          puts 'I\'m a weird string'; expect("this string").to eq('this string')
        end
      end
    end
  end

  context 'without double quotes' do
    it 'does nothing' do
      expect('').to eq('')
    end
  end
end
